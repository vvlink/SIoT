// 连接MQTT服务器的Processing代码，在EasyIoT、SIoT上测试成功，实现消息发送和订阅。
// 基于MQTT库
// 代码编写：谢作如，2019.5.7

import mqtt.*;
MQTTClient client;

class Adapter implements MQTTListener {
  void clientConnected() {
    println("连接成功");
    client.subscribe("xzr/001");//要订阅的消息名称
  }
  void messageReceived(String topic, byte[] payload) {
    println("收到新消息: " + topic + " - " + new String(payload));
  }
  void connectionLost() {
    println("连接断开");
  }
}
Adapter adapter;
void setup() {
  adapter = new Adapter();
  client = new MQTTClient(this, adapter);
  client.connect("mqtt://siot:dfrobot@192.168.1.100", "processing");//用户名为siotd；密码为frobot
}
void draw() {}
void keyPressed() {
  client.publish("xzr/001", "hello");//给名称为"xzr/001"的topic发送消息"hello"
}
