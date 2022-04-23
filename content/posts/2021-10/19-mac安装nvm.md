---
title: "Mac安装nvm"
date: 2021-10-19T13:16:28+08:00
draft: false
tags: ['2021-10','tech']
---

## 安装

### 使用brew

* `brew install nvm`

* `touch ~/.zshrc`或其他shell配置

* 添加

  ```bash
  export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
  [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
  ```



**安装完成！**



### 自行安装

* 打开终端

* `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash`

  如果出现如下问题，请挂代理后重试

  ![问题](https://images.mua.blue/images/2021/10/19/2021-10-19-13.23.39.png)

* 执行完毕后输入`nvm --version`即可查看到当前版本

  ![](https://images.mua.blue/images/2021/10/19/2021-10-19-13.28.31.png)

  如果出现`nvm: command not found`，可照着官方给出的方法解决

  * 根据自己默认shell创建一个配置文件，比如我使用的是`zsh`，则`touch ~/.zshrc`
  * 再次运行安装命令



**安装完成！**



## 用法

要下载、编译和安装最新版本的节点

```bash
nvm install node #node 是最新版本的别名
```

要安装特定版本的node

```bash
nvm install 14.7.0 #版本号
```

列出nvm可用的版本

```bash
nvm ls-remote
```

查看已安装的版本

```bash
nvm ls
```

切换版本

```bash
nvm use 14
nvm use node #不知道是直接当前电脑里最新版本还是会安装官方最新版本
```

**注意**：use只是在当前终端切换版本，想永久切换需要使用`nvm alias default 14`



M1可能在安装低版本node时会报错

![](https://images.mua.blue/images/2021/10/19/2021-10-19-14.03.48.png)

那是因为低版本没有适配M1芯片，解决方法：

```bash
env /usr/bin/arch -x86_64 /bin/zsh --login
#进入罗塞塔模式
nvm install 14
#这时可成功安装
#在终端里退出罗塞塔模式
exit
```



