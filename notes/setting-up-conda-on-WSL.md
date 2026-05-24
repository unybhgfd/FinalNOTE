```bash
# Enter new UNIX username: unybhgfd
# New password:


# 移动wsl. 这里假设只有一个发行版
# 退出bash
exit
# 打开powershell
wsl --shutdown
# 导出
wsl --export Ubuntu-24.04 E:/WSL/Ubuntu-24.04.tar
# 删除原发行版
wsl --unregister Ubuntu-24.04
# 在新位置导入
wsl --import ubuntu2404 E:\WSL E:\WSL\Ubuntu-24.04.tar
# 进入wsl
wsl
cd ~
# 设置默认用户为unybhgfd
echo -e "\n[user]\ndefault = unybhgfd" | tee -a /etc/wsl.conf


# apt换清华源
# 写入设置
echo -e "Types: deb\nURIs: https://mirrors.tuna.tsinghua.edu.cn/ubuntu\nSuites: noble noble-updates noble-backports\nComponents: main restricted universe multiverse\nSigned-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg\n\n# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释\n# Types: deb-src\n# URIs: https://mirrors.tuna.tsinghua.edu.cn/ubuntu\n# Suites: noble noble-updates noble-backports\n# Components: main restricted universe multiverse\n# Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg\n\n# 以下安全更新软件源包含了官方源与镜像站配置，如有需要可自行修改注释切换\nTypes: deb\nURIs: http://security.ubuntu.com/ubuntu/\nSuites: noble-security\nComponents: main restricted universe multiverse\nSigned-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg\n\n# Types: deb-src\n# URIs: http://security.ubuntu.com/ubuntu/\n# Suites: noble-security\n# Components: main restricted universe multiverse\n# Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg\n\n# 预发布软件源，不建议启用\n\n# Types: deb\n# URIs: https://mirrors.tuna.tsinghua.edu.cn/ubuntu\n# Suites: noble-proposed\n# Components: main restricted universe multiverse\n# Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg\n\n# # Types: deb-src\n# # URIs: https://mirrors.tuna.tsinghua.edu.cn/ubuntu\n# # Suites: noble-proposed\n# # Components: main restricted universe multiverse\n# # Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg\n" | sudo tee /etc/apt/sources.list.d/ubuntu.sources
# (可选) 静默update
sudo apt update -qq


# 中文语言包
# 下载apt包
sudo apt install language-pack-zh-hans
# 设置, 这里要选择zh-cn-utf8
sudo dpkg-reconfigure locales
# 然后退出重启系统
exit
wsl --shutdown
wsl
cd ~
# 看看是不是中文
apt --help


# 其他需要的包可以安装了先
sudo apt install xmake cmake aria2 unzip ffmpeg


# conda配置
# 从https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/?C=M&O=D 找到第一个xxx-Linux-x86_64.sh
# 这个有几gb, 如果下载太快那估计是被清华tuna屏蔽了, 需要用浏览器下载
curl -C - -o anaconda_install.sh --progress-bar -L https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2025.12-2-Linux-x86_64.sh
# 安装
chmod +x anaconda_install.sh
sudo bash ~/anaconda_install.sh -b -u -p ~/anaconda
# 进入base
source ~/anaconda/bin/activate
# 修改bashrc
conda init --all
# 重启bash
exit
wsl
cd ~
# conda换源, 关闭auto activate功能
echo -e "auto_activate: false\nchannels:\n  - defaults\nshow_channel_urls: true\ndefault_channels:\n  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main\n  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r\n  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2\ncustom_channels:\n  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud\n  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud\n  auto: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/\n" | tee ~/.condarc
# pip换源
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
# 退出base环境
conda deactivate


# git配置
git config --global user.name "unybhgfd"
git config --global user.email "unybhgfd@outlook.com"
# 记住账号密码
git config --global credential.helper store


# 使用windows的字体配置
echo -e '\n<?xml version="1.0"?>\n<!DOCTYPE fontconfig SYSTEM "fonts.dtd">\n<fontconfig>\n   <dir>/mnt/c/Windows/Fonts</dir>\n</fontconfig>' | sudo tee /etc/fonts/local.conf -a
sudo fc-cache -fv
```
