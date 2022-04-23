---
title: Mac禁用谷歌浏览器自动更新
date: 2021-12-16T23:08:04+08:00
tags: ['2021-12','tech']
---


## 原文
From reading Chrome is Bad, it seems in some situations the updater (also known as keystone) can chew up CPU cycles. Whilst I’m not 100% convinced keystone continuously chews CPU, its launchctl configuration suggests it runs at least once an hour. Given I don’t use Chrome as my main browser, this is undesirable behaviour for me.

With that in mind, I’ve decided to disable the background services rather than delete Chrome entirely. (I need it occasionally.) Stopping/unloading the services and fettling the config files to do nothing achieves this aim (and stops Chrome re-enabling them next launch), whilst leaving Chrome fully functional when needed.

1.Unload the currently loaded services
```
launchctl unload -w ~/Library/LaunchAgents/com.google.keystone.xpcservice.plist
launchctl unload -w ~/Library/LaunchAgents/com.google.keystone.agent.plist
```

2.Empty the config files, so if launchd ever tries to launch them they’ll just error out
```
echo > ~/Library/LaunchAgents/com.google.keystone.xpcservice.plist
echo > ~/Library/LaunchAgents/com.google.keystone.agent.plist
```

3.Change ownership and permissions of these files so only root can write to the files
```
chmod 644 ~/Library/LaunchAgents/com.google.keystone.xpcservice.plist
chmod 644 ~/Library/LaunchAgents/com.google.keystone.agent.plist
sudo chown root ~/Library/LaunchAgents/com.google.keystone.xpcservice.plist
sudo chown root ~/Library/LaunchAgents/com.google.keystone.agent.plist
```
Now when I want to update Chrome once in a blue moon when I need it, I can navigate to [chrome://settings/help][1] to update (or from the UI, Chrome -> About Chrome.)

## 翻译
从阅读Chrome是坏的，在某些情况下，更新程序（也称为基石）似乎可以咀嚼CPU周期。虽然我不是100%相信Keystone会持续咀嚼CPU，但其launchctl配置表明它每小时至少运行一次。鉴于我不使用Chrome作为主浏览器，这对我来说是不受欢迎的行为。

考虑到这一点，我决定禁用后台服务，而不是完全删除Chrome。（我偶尔需要它。）停止/卸载服务并固定配置文件什么都不做，可以实现这一目标（并阻止Chrome在下次启动时重新启用它们），同时在需要时让Chrome完全正常工作。

1.卸载当前加载的服务
```
launchctl unload -w ~/Library/LaunchAgents/com.google.keystone.xpcservice.plist
launchctl unload -w ~/Library/LaunchAgents/com.google.keystone.agent.plist
```

2.清空配置文件，因此，如果启动尝试启动它们，它们只会出错
```
echo > ~/Library/LaunchAgents/com.google.keystone.xpcservice.plist
echo > ~/Library/LaunchAgents/com.google.keystone.agent.plist
```
3.更改这些文件的所有权和权限，以便只有根可以写入文件
```
chmod 644 ~/Library/LaunchAgents/com.google.keystone.xpcservice.plist
chmod 644 ~/Library/LaunchAgents/com.google.keystone.agent.plist
sudo chown root ~/Library/LaunchAgents/com.google.keystone.xpcservice.plist
sudo chown root ~/Library/LaunchAgents/com.google.keystone.agent.plist
```
现在，当我想在需要时一月更新Chrome时，我可以导航到[chrome://settings/help][1]进行更新（或从UI，Chrome->关于Chrome。）
[1]: chrome://settings/help
