安装运行
=========================

SIoT是一个绿色软件，将下载的压缩包解开后，将看到多个文件，如：

| SIoT_win.exe（Win10版本执行文件）
| SIoT_mac（Mac版本可执行文件）
| SIoT_linux（Linux版本执行文件）

注：更多操作系统支持的文件在不断增加中。

根据自己的操作系统，运行相应的软件即可。

### Window版本：
-----------

双击运行SIoT_win.exe，将看到一个黑色的CMD窗口，不要关闭。


### Mac版本：
------------

打开终端运行，转到相应目录然后执行命令，如“./SIoT_mac”。

注意：直接双击运行会出现错误！程序没有读取配置文件的权限问题，将默认开启的是8082端口。

如果担心程序被删除，可以使用nohup命令。

参考命令：nohup node /Users/xiezuoru/Desktop/iot_test/SIOT_Mac &
其中“/Users/xiezuoru/Desktop/iot_test/SIOT_Mac”为程序的路径。

### linux版本：
-----------

nohup ./SIoT_linux &
其中“SIoT_linux”为程序的路径。



