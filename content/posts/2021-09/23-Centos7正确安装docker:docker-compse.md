---
title: "Centos7正确安装docker/docker-compse"
date: 2021-09-23T16:11:53+08:00
draft: false
tags: ['2021-09','tech']
---
# Centos7正确安装docker/docker-compse

## 安装docker

1. ```bash
   yum -y update
   ```

   先升级，yum有两个升级命令`update`和`upgrade`

   > yum -y update：升级所有包同时，也升级软件和系统内核；
   >
   > yum -y upgrade：只升级所有包，不升级软件和系统内核，软件和内核保持原样。

   > -y 代表着当安装包时询问你`Is this OK[y/d/N]`，就会自动选择`y`，不需要你再手动选择。

   出现Complete!即为更新完成

2. ```bash
   yum -y install docker
   ```

3. ```bash
   docker -v
   ```

   > 出现Docker version 1.13.1, build 7d71120/1.13.1相似结果即成功安装

   > 启动：sudo systemctl start docker
   >
   > 设置开机启动：sudo systemctl enable docker

## 安装docker-compose

1. ```bash
   pip3 install --upgrade pip
   #加上--upgrade为升级包而不是安装包
   ```

2. ```bash
   pip3 install docker-compose
   ```

   而我在最新版本启动docker-compose报错

   ```bash
   $ docker-compose up
   Building tomcat
   unknown flag: --iidfile
   See 'docker build --help'.
   ERROR: Service 'tomcat' failed to build
   ```

   谷歌后解决方法为**降级**

   ```bash
   rm -f /usr/local/bin/docker-compose
   pip install docker-compose==1.26.2
   ```



### 运行时可能会出现的问题

1. ```bash
   Creating network "xxxxx" with the default driver
   ERROR: Failed to Setup IP tables: Unable to enable SKIP DNAT rule:  (iptables failed: iptables --wait -t nat -I DOCKER -i br-c7abf8aa9caa -j RETURN: iptables: No chain/target/match by that name.
    (exit status 1))
   ```

   解决方法：

   1. `systemctl stop docker`
   2. `systemctl start docker`


