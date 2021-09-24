---
title: mac使用homebrew安装jdk
date: 2021-09-11T14:22:52+08:00
tags:  ['2021-09','tech']
---


## Homebrew安装jdk
因为电脑上没有jdk需要安装一个，首先去homebrew仓库里搜索jdk但是很奇怪，感觉都不是官方的。于是我去百度搜索，找到这个命令
```
brew cask install homebrew/cask-versions/adoptopenjdk8
//但是无法使用，进行报错搜索后发现homebrew已经丢弃这种用法
//目前正确用法
brew install --cask homebrew/cask-versions/adoptopenjdk8
```
如果下载速度比较慢挂个终端代理就好。
