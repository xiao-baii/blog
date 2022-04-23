---
title: "记安装halo过程"
date: 2020-03-28T14:28:37+08:00
draft: false
tags: ['tech','2020-03']
---

## 环境安装

根据halo官网的[开发文档](https://docs.halo.run)进行配置，因为官网开发文档是基于**CentOS 7.x** 为例，而我使用的是ubuntu16，所以安装jdk指令与官网不一样。通过查找资料`sudo apt install openjdk-8-jdk`安装jdk1.8。
验证安装成功：`java -version`
你会看到这样的输出:

```
openjdk version "1.8.0_162"
OpenJDK Runtime Environment (build 1.8.0_162-8u162-b12-1-b12)
OpenJDK 64-Bit Server VM (build 25.162-b12, mixed mode)
```
## 安装halo
同样根据halo官网的[开发文档](https://docs.halo.run)进行安装，然后配置文件。
## 部署到服务器
在放到服务器上我栽了很多跟头，我重装了两三次系统，后面发现阿里云可以使用快照，而且一个小时只需要几厘钱，可以大大节约我测试安装时间，以后安装新软件就可以先去阿里云备份。

第一次部署完成后，发现只有主页是可以不加8xxx端口的其它网页会加端口访问，这让我强迫症犯难，通过修改halo的网站链接发现无法访问动态资源。

后面通过多次尝试，发现是nginx配置的问题，bt面板刚开始会自动配置出
```
server
{
    listen 80;
    server_name xxxxx;
    index index.php index.html index.htm default.php default.htm default.html;
    root xxxxxxxx;
    
    #SSL-START SSL相关配置，请勿删除或修改下一行带注释的404规则
    #error_page 404/404.html;
    #SSL-END
    
    #ERROR-PAGE-START  错误页配置，可以注释、删除或修改
    #error_page 404 /404.html;
    #error_page 502 /502.html;
    #ERROR-PAGE-END
    
    #PHP-INFO-START  PHP引用配置，可以注释或修改
    include enable-php-56.conf;
    #PHP-INFO-END
    
    #REWRITE-START URL重写规则引用,修改后将导致面板设置的伪静态规则失效
    include xxxxx;
    #REWRITE-END
    
    #禁止访问的文件或目录
    location ~ ^/(\.user.ini|\.htaccess|\.git|\.svn|\.project|LICENSE|README.md)
    {
        return 404;
    }
    
    #一键申请SSL证书验证目录相关设置
    location ~ \.well-known{
        allow all;
    }
    
    location ~ .*\.(gif|jpg|jpeg|png|bmp|swf)$
    {
        expires      30d;
        error_log off;
        access_log /dev/null;
    }
    
    location ~ .*\.(js|css)?$
    {
        expires      12h;
        error_log off;
        access_log /dev/null; 
    }
    access_log  xxxx;
    error_log  xxxx;
}
```
后面我将这些删掉按照开发文档的进行配置就可以反向代理访问动态资源
```
server
{
    listen 80;
    server_name xxxxx;
    index index.php index.html index.htm default.php default.htm default.html;
    root xxxxxxx;
    
    location /{
        proxy_set_header HOST $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        proxy_pass http://127.0.0.1:xxx/;
    }
    access_log  xxxxx;
    error_log  xxxxx;
}
```