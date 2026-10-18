#!/usr/bin/env python3
"""每分钟监视 MCSManager 实例状态变化。"""

import json
import os
import sys
import time

import requests

CONFIG_FILE = os.path.join(os.path.expanduser("~"), ".mcsm_read_config.json")
POLL_INTERVAL = 60
INSTANCE_STATUS = {
    -1: "忙碌",
    0: "已停止",
    1: "停止中",
    2: "启动中",
    3: "运行中",
}


class MCSMClient:
    def __init__(self, base_url, apikey, timeout=15):
        self.base_url = base_url.rstrip("/")
        self.apikey = apikey
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json; charset=utf-8",
            "X-Requested-With": "XMLHttpRequest",
        })

    def _call(self, path, params=None):
        request_params = dict(params or {})
        request_params["apikey"] = self.apikey
        response = self.session.get(
            self.base_url + path,
            params=request_params,
            timeout=self.timeout,
        )
        response.raise_for_status()
        try:
            result = response.json()
        except ValueError as exc:
            raise RuntimeError(f"响应非 JSON：{response.text[:200]}") from exc
        if isinstance(result, dict) and "status" in result:
            if result["status"] != 200:
                raise RuntimeError(f"API 错误 [{result['status']}]：{result.get('data')}")
            return result.get("data")
        return result

    def _list_instances_on_daemon(self, daemon_id):
        result = self._call(
            "/api/service/remote_service_instances",
            {"daemonId": daemon_id, "page": 1, "page_size": 100},
        )
        if isinstance(result, dict):
            instances = result.get("data", []) or []
        elif isinstance(result, list):
            instances = result
        else:
            instances = []
        return [instance for instance in instances if isinstance(instance, dict)]

    def list_instances(self):
        try:
            daemons = self._call("/api/service/remote_services_list")
        except (requests.RequestException, RuntimeError, ValueError):
            daemons = []

        instances = []
        if isinstance(daemons, list) and daemons:
            for daemon in daemons:
                daemon_id = daemon.get("uuid") if isinstance(daemon, dict) else None
                if not daemon_id:
                    continue
                try:
                    daemon_instances = self._list_instances_on_daemon(daemon_id)
                except (requests.RequestException, RuntimeError, ValueError):
                    continue
                for instance in daemon_instances:
                    instance["_daemonId"] = daemon_id
                    instances.append(instance)
            if instances:
                return instances

        user = self._call("/api/auth/", {"advanced": "true"})
        references = user.get("instances", []) if isinstance(user, dict) else []
        for reference in references:
            if not isinstance(reference, dict):
                continue
            daemon_id = reference.get("daemonId") or reference.get("serviceUuid")
            instance_id = reference.get("instanceUuid")
            if not daemon_id or not instance_id:
                continue
            instance = dict(reference)
            instance["_daemonId"] = daemon_id
            instances.append(instance)
        return instances


def load_client():
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as config_file:
            config = json.load(config_file)
    except FileNotFoundError as exc:
        raise RuntimeError(f"找不到配置文件：{CONFIG_FILE}，请先运行 MCSManager-Read.py 配置 API Key") from exc
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"读取配置文件失败：{exc}") from exc

    url = config.get("url")
    apikey = config.get("apikey")
    if not url or not apikey:
        raise RuntimeError(f"配置文件缺少 url 或 apikey：{CONFIG_FILE}")
    return MCSMClient(url, apikey)


def instance_key(instance):
    return instance.get("_daemonId", ""), instance.get("instanceUuid", "")


def display_name(instance):
    config = instance.get("config") or {}
    return (
        config.get("nickname")
        or instance.get("nickname")
        or instance.get("instanceUuid")
        or "(未命名)"
    )


def status_text(instance):
    status = instance.get("status")
    try:
        status = int(status)
    except (TypeError, ValueError):
        return f"未知 ({status})"
    return INSTANCE_STATUS.get(status, f"未知 ({status})")


def print_all_statuses(instances):
    print(f"\n实例状态（共 {len(instances)} 个）：")
    for instance in instances:
        print(f"  {display_name(instance)} [{instance_key(instance)[1]}]: {status_text(instance)}")
    sys.stdout.flush()


def main():
    try:
        client = load_client()
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        return 1

    print(f"开始监视 MCSManager 实例状态，每 {POLL_INTERVAL} 秒检查一次。按 Ctrl+C 退出。")
    previous_statuses = None
    try:
        while True:
            try:
                instances = client.list_instances()
                current_statuses = {
                    instance_key(instance): instance.get("status")
                    for instance in instances
                }
                if previous_statuses is not None and current_statuses != previous_statuses:
                    changed = {
                        key for key in previous_statuses.keys() | current_statuses.keys()
                        if previous_statuses.get(key) != current_statuses.get(key)
                    }
                    if changed:
                        sys.stdout.write("\a\033]9;4;2;100\a")  # 100% 进度红条
                        sys.stdout.flush()
                        print_all_statuses(instances)
                previous_statuses = current_statuses
            except (requests.RequestException, RuntimeError, ValueError) as exc:
                print(f"查询实例状态失败：{exc}", file=sys.stderr, flush=True)
            time.sleep(POLL_INTERVAL)
    except KeyboardInterrupt:
        print("\n已停止监视。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
