记录一次完全没配置过编程环境，无 N 卡的电脑中 Ubuntu (WSL 2) 中 Python 机器学习环境配置。

> A.K.A. 挑战在我妈的电脑上学机器学习

先下个 PowerShell...下完了。默认界面好丑，换成 Catppuccin 的 Lattle（亮色）和 Mocha（暗色）主题。我们根据 [GitHub 上的配置流程](https://github.com/catppuccin/windows-terminal?tab=readme-ov-file#usage)复制配置到 PowerShell 的配置文件。然后进设置 > 配色方案 > 右键配色方案 > 设为默认，然后保存，接着在外观-应用程序外观里选择要的外观，然后保存，大功告成。

在命令行输入 `wsl --install --web-download` 一键配置 WSL 2，这个命令会[默认安装 Ubuntu 发行版](https://learn.microsoft.com/zh-cn/windows/wsl/basic-commands#install)，其中 `--web-download` 选项使程序从 GitHub 而不是微软应用商店下载。

在等待安装时，先把 VSCode 装了，安装时改了安装路径（C 盘快满了），还选择了“创建桌面快捷方式”。VSCode 插件先只安装 Catppuccin 的主题和图标。

过了一个晚上，emm...输出如下：
```text
请求的操作需要提升。
正在下载: 适用于 Linux 的 Windows 子系统 2.6.3
正在安装: 适用于 Linux 的 Windows 子系统 2.6.3
已安装 适用于 Linux 的 Windows 子系统 2.6.3。
操作成功完成。
无法从“https://raw.githubusercontent.com/microsoft/WSL/master/distributions/DistributionInfo.json”提取列表分发。操作超时
错误代码: Wsl/InstallDistro/WININET_E_TIMEOUT
```

我们到应用商店找到 Ubuntu 然后安装。安装完打开应用会弹出一个终端窗口然后我们按照指引输入用户名和密码：
```text
Installing, this may take a few minutes...
Please create a default UNIX user account. The username does not need to match your Windows username.
For more information visit: https://aka.ms/wslusers
Enter new UNIX username: unybhgfd
New password:
Retype new password:
passwd: password updated successfully
Installation successful!
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

unybhgfd@Constance:~$
```

在我们[配置了 Anaconda](http://123.60.188.246/discussion-detail/2966) 之后：
``` bash
cd ~
# 创建环境
conda create --name myenv python=3.12
# 激活环境
conda activate myenv
# 安装需要的包
pip install tensorflow-cpu numpy matplotlib pylint
# 创建项目
mkdir learnml && cd learnml
git config --global init.defaultBranch main
git init
# 项目设置
mkdir .vscode
mkdir src
echo -e '{\n    "files.encoding": "utf8",\n    "python.analysis.extraPaths": [\n        "./src"\n    ],\n    "pylint.args": [\n        "--max-line-length=120"\n    ],\n    "python-envs.defaultEnvManager": "ms-python.python:conda",\n    "python-envs.defaultPackageManager": "ms-python.python:conda",\n    "python-envs.pythonProjects": [],\n}' | tee ./.vscode/settings.json
echo -e "tmp*\n__pycache__" | tee ./.gitignore
echo -e "import
```

然后我们打开 VSCode，点左下角的“远程”按钮，选择 WSL，等安装完插件左下角应该就能显示连上了“WSL: ubuntu”，然后打开我们的项目文件夹。

我们还要设置VSCode，先 Ctrl + Shift + P 打开用户设置，修改 JSON 文件：
```JSON
{
    "workbench.colorTheme": "Catppuccin Latte",
    "workbench.iconTheme": "catppuccin-latte",
    "files.trimTrailingWhitespace": true, // 自动清除行尾空格
    "json.schemaDownload.trustedDomains": {
        "https://esm.sh": true, // Catppuccin 主题需要让这个受信任
    },
    "files.encoding": "utf8", // 默认文件编码
    "editor.editContext": false, // 修复输入法问题
}
```

我们接着安装这些插件：
* `ms-python.python`。
* `ms-python.pylint`，当然你也可以装 Flake8。

这些是可选的，建议安装：
* `usernamehw.errorlens`：在代码后面显示错误

装完 Ctrl + Shift + P 选择“Select Interpreter”，然后选择你的 Anaconda 环境

然后我们用示例代码看看 linter 和 TensorFlow 能不能正常运行：
```python
import tensorflow as tf
import timeit


# 打印 TensorFlow 版本
print(f"TensorFlow Version: {tf.__version__}")

# 创建随机张量
cpu_a = tf.random.normal([10000, 1000])
cpu_b = tf.random.normal([1000, 2000])

def cpu_run():
    # with tf.device('/cpu:0'):
    result = tf.matmul(cpu_a, cpu_b)
    return result

# 初始化阶段的时间
cpu_time_init = timeit.timeit(cpu_run, number=10)
# 实际运行时间
cpu_time_run = timeit.timeit(cpu_run, number=10)

print('Initialization Time on CPU:', cpu_time_init)
print('Run Time on CPU:', cpu_time_run)

```
