---
title: "Chevereto图床安装"
date: 2021-09-25T18:23:24+08:00
draft: false
---

## 起因

在写一篇md的时候突然想插入图片，可是本地图片插入后hugo无法正确的生成文章到服务器，这时候就需要使用url图片了。于是我在网上找到了Chevereto。



## 安装

**方法1：** [Chevereto-Free Github](https://github.com/chevereto/Chevereto-Free)根据官方文档或者网上教程进行安装。

**方法2：**[nmtan/chevereto](https://hub.docker.com/r/nmtan/chevereto)使用docker安装

因为docker安装起来非常方便，所以我选择**方法2**进行安装Chevereto。如果没有安装docker and docker-compose可以去看我之前的文章。

[nmtan/chevereto](https://hub.docker.com/r/nmtan/chevereto)中的overview里已经给出了docker-compose.yml，我们可以直接拿来使用。

* 创建一个空目录，创建docker-compose.yml

* 编写docker-compose.yml

```yaml
#docker-compose.yml
version: '3'

services:
  db:
    image: mariadb
    volumes:
      - ./database:/var/lib/mysql:rw
    restart: always
    networks:
      - private
    environment:
      MYSQL_ROOT_PASSWORD: chevereto_root
      MYSQL_DATABASE: chevereto
      MYSQL_USER: chevereto
      MYSQL_PASSWORD: chevereto

  chevereto:
    depends_on:
      - db
    image: nmtan/chevereto
    restart: always
    networks:
      - private
    environment:
      CHEVERETO_DB_HOST: db
      CHEVERETO_DB_USERNAME: chevereto
      CHEVERETO_DB_PASSWORD: chevereto
      CHEVERETO_DB_NAME: chevereto
      CHEVERETO_DB_PREFIX: chv_
    volumes:
      - ./images:/var/www/html/images:rw
      - ./php.ini:/usr/local/etc/php/php.ini:ro #这个配置文件是为了修改上传2M的限制
    ports:
      - 8004:80

networks:
  private:
```

* 编写php.ini

```php
memory_limit = 256M;
upload_max_filesize = 100M;
post_max_size = 100M;
```

* 使用`docker-compose up -d`跑起来。

* 宝塔面板创建一个网站![](https://images.mua.blue/images/2021/09/25/wbomY4.png)

* 配置反向代理![](https://images.mua.blue/images/2021/09/25/qU7pZd.png)

* 接着就可以打开网站进行安装，因为docker已经帮我们配置好了mysql和Chevereto之间的连接，我们只需要创建管理员账号。

* **(可选)**登上管理员账号，打开仪表盘->设置->网站![](https://images.mua.blue/images/2021/09/25/LbEyI9.png)

  将https改为强加，紧接着我们来到宝塔面板给域名申请一个ssl证书，这样和网站传输的数据就会比较安全。

* **(可选)**修改上传限制，打开仪表盘->设置->图片上传![](https://images.mua.blue/images/2021/09/25/fIoukO.png)

  前提是前面用php.ini对php进行配置了。

**enjoy!**



## 安装时踩的坑

1. 没有在仪表盘配置好https协议，就申请好证书使用https协议进行访问，导致静态文件的链接还是http，浏览器报错不加载http协议的静态文件。其中有一个问题还是没有解决，开始我是根据nmtan/chevereto仓库里的高级配置。

   ```php
   $val = getenv('CHEVERETO_HTTPS');
   if ($val !== false) {
       /*
        * Specify whether user should connect to Chevereto via HTTPS instead of HTTP
        * Please note that Chevereto has excellent mechanism to detect this
        * already - https://github.com/Chevereto/Chevereto-Free/blob/0184f27a97daa55ec3b07560c5dd619d22abc907/lib/G/G.php#L113
        * So 99% of the time you won't have to bother with this. The only
        * usecase that I can image where you need to set this is if you have
        * a misconfigured reverse proxy that somehow doesn't include the
        * `http-x-forwarded-proto` header into the forwarded requests
        */
       $settings['https'] = strtolower(trim($val)) === 'true';
   }
   ```

   在docker-compose.yml里加了一个环境变量`CHEVERETO_HTTPS:1`可是没用。



2. 修改上传限制，将php.ini配置好后还是限制为2M，后来发现原来chevereto里也要改。先改php限制再改chevereto限制。

