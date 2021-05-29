# pinpong


## 简介

借助于pinpong库，直接用Python代码就能给各种常见的开源硬件编程。pinpong库是一个基于Firmata协议开发的Python硬件控制库。其原理是给开源硬件烧录一个特定的固件，使开源硬件可以通过串口与电脑通讯，执行各种命令。pinpong库的名称由“Pin”和“Pong”组成，“Pin”指引脚，“pinpong”为“乒乓球”的谐音，指信号的往复。目前pinpong库支持Arduino、掌控板、micro:bit等开源硬件，同时支持虚谷号、树莓派和拿铁熊猫等。

pinpong库的设计，是为了让开发者在开发过程中不用被繁杂的硬件型号束缚，而将重点转移到软件的实现。哪怕程序编写初期用Arduino开发，部署时改成了掌控板，只要修改一下硬件的参数就能正常运行，实现了“一次编写处处运行”。

官方文档：https://pinpong.readthedocs.io/

github：https://github.com/DFRobot/pinpong-docs