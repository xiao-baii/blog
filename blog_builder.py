# -*- coding: utf8 -*-
from datetime import datetime
import pytz
import os


article_date = datetime.now(tz=pytz.timezone('Asia/Shanghai')).isoformat(timespec='seconds')
article_name = input("创建文章名：")
pwd = os.path.join("/Users/xiaobai/Documents/blog/content/posts", datetime.now().strftime("%Y-%m"))
if not os.path.isdir(pwd):
    os.mkdir(pwd)
article_pwd = os.path.join(pwd, datetime.now().strftime("%d") + "-" + article_name + ".md")
if os.path.isfile(article_pwd):
    print("已有相同文章")
    exit()
f = open(article_pwd, 'w')
article_content = "---\ntitle: " + article_name + "\ndate: " + article_date + "\ndraft: true\ntags:['" + datetime.now().strftime("%Y-%m") + "', '']\n---\n"
f.write(article_content)
f.close()