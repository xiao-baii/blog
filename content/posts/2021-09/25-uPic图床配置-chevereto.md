---
title: "uPic图床配置-Chevereto"
date: 2021-09-25T18:23:45+08:00
draft: false
tags: ['2021-09','tech']
---
## 安装uPic

1. Homebrew:
   
   ```bash
   brew install --cask upic
   ```

2. 手动:

   前往作者的[Github](https://github.com/gee1k/uPic/releases)下载。

具体功能可以查看[作者博客](https://blog.svend.cc/upic/)



## 配置uPic

**参数:**

* API 地址: 填写上面准备好的 `[上传服务地址]`
* 请求方式: `POST`
* 使用 Base64: `勾选`
* 文件字段名: `source`
* URL 路径: 上传完成后获取图片链接的路径。`['image', 'url']`
* Content-Type: `multipart/form-data; charset=utf-8;`
* key: 填写上面准备好的 `[API Key]`
* action: `upload`

![第一步](https://images.mua.blue/images/2021/09/25/2021-09-25-18.36.02.png)

![第二步](https://images.mua.blue/images/2021/09/25/2021-09-25-18.40.46.png)



## 最后

**enjoy!!!**
