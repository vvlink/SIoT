Processing
=========================


Processing是一款专为设计师和艺术家使用的编程语言，由美国麻省理工学院媒体实验室（MIT）美学与运算小组创立的。Processing的出现，被视为艺术设计创作的一场革命。利用Processing，艺术家可以将抽象的数据呈现为生动的视觉形象。它不仅可以生成唯美的图形，还能编写出功能强大的互动艺术作品。

- Processing下载地址：https://processing.org/


Processing的MQTT库简介
-----------------------------------
Processing是一个开源的编程语言，有很多人为其开发了各种开源的库。借助MQTT库，Processing即可与MQTT服务器进行交互。

在库文件中查找“MQTT”即可找到。

.. image:: ../image/demo/09_processing_02.png

Processing的MQTT库全名：MQTT library for Processing based on the Eclipse Paho project

库的开源地址：https://github.com/256dpi/processing-mqtt

.. image:: ../image/demo/09_processing_03.png

参考代码
-----------------------

::

    import mqtt.*;
    MQTTClient client;

    class Adapter implements MQTTListener {
      void clientConnected() {
        println("client connected");
        client.subscribe("xzr/001");//要订阅的消息名称
      }
      void messageReceived(String topic, byte[] payload) {
        println("new message: " + topic + " - " + new String(payload));
      }
      void connectionLost() {
        println("connection lost");
      }
    }
    Adapter adapter;
    void setup() {
      adapter = new Adapter();
      client = new MQTTClient(this, adapter);
      client.connect("mqtt://siot:dfrobot@127.0.0.1", "processing");//用户名为siotd；密码为frobot
    }
    void draw() {}
    void keyPressed() {
      client.publish("xzr/001", "world");//给名称为"xzr/001"的topic发送消息"world"
    }
