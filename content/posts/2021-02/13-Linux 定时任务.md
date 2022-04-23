---
title: "Linux定时任务"
date: 2021-02-13T14:28:37+08:00
draft: false
tags: ['tech','2021-02']
---

## 定时任务

因为今天写了一个学习通自动签到服务需要部署到centos服务器下，这里我就要啰嗦一下，开始服务器使用的是ubuntu系统，结果使用网上的部署flask教程部署不成功，还是我太菜了，网上的教程也都是一个模(**mu**)子刻出来的，于是我只能换成centos系统了，因为宝塔面板里的python一键部署工具只支持centos。

部署完成后就是让任务每隔多久执行一次了，从百度上找到Linux自带的Crontab，看了一下觉得已经可以解决绝大部分定时问题了。

配置文件中的每一行具有六个栏位，这六个栏位的意义为:

| 意义 | 分钟 | 小时 | 日期 | 月份 | 星期 | 命令    |
| :--- | ---- | ---- | ---- | ---- | ---- | ------- |
| 范围 | 0-59 | 0-23 | 1-31 | 1-12 | 0-7  | command |

其中星期取值为0和7时均代表星期日.

前五栏除了可以取上表中的这些值外,还可以取下面这些特殊参数:

>- ***** 取值范围内的所有数字
>- **/** 每过多少个数字
>- **-** 从X到Z
>- **，**散列数字

```
crontab [-u username]　　　　//省略用户表表示操作当前用户的crontab
    -e      (编辑工作表)
    -l      (列出工作表里的命令)
    -r      (删除工作)
```

例如我需要在星期一到星期五早上八点到下午十点每三分钟执行一次

```
*/3 8-12 * * 1-5 python /www/wwwroot/xuexi/sign1.py
*/3 14-22 * * 1-5 python /www/wwwroot/xuexi/sign1.py
```

**错误纠正**

在星期一到星期五早上八点到下午十点每三分钟执行一次应该是

```
*/5 8-11 * * 1-5 python /www/wwwroot/xuexi/sign1.py
*/5 14-21 * * 1-5 python /www/wwwroot/xuexi/sign1.py
```

因为中间两小时是没有课的而我不知道`*/5 8-12,14-22 * * 1-5 python /www/wwwroot/xuexi/sign1.py`这个行不行的通，所以我使用了两条。

期间还出现了`"/tmp/crontab.XXXXcz4Lql":1: bad minute`后面通过其他人解决方法发现是格式不对在每三分钟这一列没有加`*`只有`/3`

**运行日志**

发现需要程序输出的日志

百度了一下找到

```
*/3 8-11 * * 1-5 python /www/wwwroot/xuexi/sign1.py > sign.log 2>&1 #后台挂起同时输出日志
```

经过测试发现日志只记录最后一次输出的

想要记录每一次输出的只需要

```
*/3 8-11 * * 1-5 python /www/wwwroot/xuexi/sign1.py >> sign.log 2>&1
```



## 参考链接

语法报错：<https://www.cnblogs.com/grimm/p/6872303.html>

Crontab使用：<https://www.runoob.com/w3cnote/linux-crontab-tasks.html>

<https://segmentfault.com/a/1190000006797330>