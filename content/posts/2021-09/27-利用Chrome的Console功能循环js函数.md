---
title: "利用Chrome的Console功能循环js函数"
date: 2021-09-27T21:03:07+08:00
draft: false
tags: ['2021-09','tech']
---

## 代码

```js
var autoTouch = setInterval(function(){
   save();
 },2000);
autoTouch;
```

每两秒就会执行一次sava()函数。

setInterval() 方法可按照指定的周期（以毫秒计）来调用函数或计算表达式。

setInterval() 方法会不停地调用函数，直到 clearInterval() 被调用或窗口被关闭。由 setInterval() 返回的 ID 值可用作 clearInterval() 方法的参数。
