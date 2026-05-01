在 VSCode WSL 中配置 Vue 3 + TypeScript + Vite 开发环境

```bash
cd ~

# 下载工具
sudo apt install npm

#初始化项目
git clone https://gitee.com/unybhgfd/XESChat.git
cd xeschat
git checkout master
ls -a
npm install --force
```

然后下载插件：`vue.volar`

运行 `npm run build` 后，发现 Vite 需要更新版本的 node.js，可是我们刚刚 `apt install` 的就是最新版本...为了安装新版本 node.js，我们需要先安装 NVM，即 Node.js Version Manager。[在官网用命令安装](https://github.com/nvm-sh/nvm#install--update-script)。运行完命令记得 `source ~/.bashrc`。

安装完 NVM 后运行命令 `nvm install 20` 就能更新 node.js 了。
