# pinpong编程入门


## 1.pinpong简介

pinpong是一个专用于开源硬件控制的Python库。借助于pinpong库，直接用Python代码就能给各种常见的开源硬件编程。pinpong库基于Firmata协议开发，其原理是给开源硬件烧录一个特定的固件，使开源硬件可以通过串口与电脑通讯，执行各种命令。

pinpong库的名称由“Pin”和“Pong”组成，“Pin”指引脚，“pinpong”为“乒乓球”的谐音，指信号的往复。目前pinpong库支持Arduino、掌控板、micro:bit等开源硬件，同时支持虚谷号、树莓派和拿铁熊猫等。

pinpong库的设计，主要用于物联网和人工智能，用于具备传感和控制功能的信息系统开发。在pinpong库的支持下，开发者在开发过程中不用被繁杂的硬件型号束缚，而将重点转移到软件的实现。哪怕程序编写初期用Arduino开发，部署时改成了掌控板，只要修改一下硬件的参数就能正常运行，实现了“一次编写处处运行”。

## 2.课程简介

本课程为谢作如在调试pinpong库时编写，严格说是用于培训和教学的编程笔记。

## 3.配套硬件

### 3.1.调试硬件

Win10电脑（MacOS）、arduino UNO

### 3.2.部署硬件

- 选择1：虚谷号（虚谷号上自带了Arduino UNO）
- 选择2：RockPI、mini pinpong board（其实就一块小的Arduino）

### 3.3.扩展模块

- 按钮模块 * 1
- 光线传感器 * 1
- 温湿度传感器 * 1
- 蜂鸣器 * 1
- LED模块 * 1
- 9克舵机 * 1

## 4.开发计划

### 1）第一部分 GPIO控制
- 数字输出
- 数字输入
- 模拟输出
- 模拟输入
- 舵机控制
- 扩展模块

### 2）第二部分 物联网应用
- 数据采集
- 远程控制
- 自动控制

### 3）第三部分 人工智能应用
- 语音控制
- 车库门禁
- 人脸跟踪


## 5.pinpong的更多文档

官方文档：https://pinpong.readthedocs.io/

github：https://github.com/DFRobot/pinpong-docs