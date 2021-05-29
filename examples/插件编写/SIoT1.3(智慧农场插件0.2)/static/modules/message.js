new Vue({
    el: '#appContainer',
    data: {
        items: [],
        line_options: {},
        editData: {},
        params: {},
        topic: '',
        items2: [],
        isShow: false,
        MessagesInterval:0
    },
    mounted: function () {
        $("#end_time").datetimepicker({
            "language": 'zh-CN',
            "autoclose": 1,
            "minView": 1
        });
        $("#start_time").datetimepicker({
            "language": 'zh-CN',
            "autoclose": 1,
            "minView": 1
        });
    },
    created: function () {
        // `this` 指向 vm 实例
        this.fetchData();
        var that = this;
        
    },


    methods: {
        fetchData: function () {
            var params = app.GetRequest(window.location.search);
            this.topic = this.params.topic = params.topic
            this.getMessages();

        },
        setIntervalStatus:function(){
            if ($("[name='IntervalStatus']").prop("checked")){
                this.startInterval();
            }else{
                this.stopInterval();
            }
        },
        startInterval:function(){
            var that = this;
            if ( this.MessagesInterval>0){
                return;
            }
           this.MessagesInterval =  window.setInterval(function(){
                    that.getMessages();
            },1000)
        },
        stopInterval:function(){
            console.log("MessagesInterval",this.MessagesInterval);
            window.clearInterval(this.MessagesInterval)
            this.MessagesInterval = 0;
        },
        setShow:function(){
            this.isShow = !this.isShow
            var that = this;
            if(this.isShow){
                Vue.nextTick(function(){
                    that.changeToHighcharts()
                })
                
            }
        },
        sendMsg: function () {
            var that = this;
            if (this.loading == 1) {
                return;
            }
            this.loading = 1;
            app.get("/publish", {
                topic: $("#topic").val(),
                msg: $("#msg").val(),
            }, function (res) {
                that.loading = 0;
                if (res.code != 1) {
                    app.alert(res.msg);
                } else {
                    app.alert("发送成功");
                    that.getMessages();

                }
            })
        },

        getMessages: function () {
            var that = this;
            var params = this.params;
            params.order = "desc"
            app.get("/messages", params, function (res) {
                if (res.code != 1) {
                    app.alert(res.msg);
                } else {
                    that.items2 = res.data;
                    //that.items2 = [].concat(that.items)
                    that.items = []
                    for (var index = 0; index < that.items2.length; index++) {
                        const element = that.items2[index];
                        if (!isNaN(element.Content * 1)) {
                            that.items.push(element);
                        }
                    }
                    that.items.reverse();
                }
                if(that.isShow){ 
                    that.changeToHighcharts();
                  }
                // that.changeToHighcharts();
            })

            // params.order = "desc"
            // app.get("/messages", params, function (res) {
            //     if (res.code != 1) {
            //         app.alert(res.msg);
            //     } else {
            //         that.items2 = res.data;
            //     }

            // })
        },


        search: function () {
            var params = {
                topic: this.params.topic
            };
            if ($("#start_time").val() != "") {
                params.begin = $("#start_time").val()+":00";
            }
            if ($("#end_time").val() != "") {
                params.end = $("#end_time").val()+":00";
            }
            params.psize = $("#limit").val();
            this.params = params;
            this.getMessages();
        },

        changeToHighcharts: function () {
            var HighchartsData = this.items;

            /************折线形图*************/

            var data = [];
            var categories = [];
            for (var i = 0 in HighchartsData) {
                categories.push(HighchartsData[i].Created);
                data.push(Number(HighchartsData[i].Content));
            }

            option = {
                tooltip: {
                    trigger: 'axis',
                    position: function (pt) {
                        return [pt[0], '10%'];
                    }
                },
                title: {
                    left: 'center',
                    text: "[" + this.params.topic + ']消息监控',
                },
                toolbox: {
                    feature: {
                        dataZoom: {
                            yAxisIndex: 'none'
                        },
                        restore: {},
                        saveAsImage: {}
                    }
                },
                xAxis: {
                    type: 'category',
                    data: categories
                },
                yAxis: {
                    type: 'value'
                },
                series: [{
                    data: data,
                    type: 'line'
                }]
            };

            var myChart = echarts.init(document.getElementById('highcharts'));
            myChart.setOption(option);
            // 实例化统计
            // this.showhighcharts();
        },
        tableToExcel: function () {
            console.log(this.items2);
            var jsonData = this.items2;

            let str = "ID,主题,消息,时间\n";
            //增加\t为了不让表格显示科学计数法或者其他格式
            for (let i = 0; i < jsonData.length; i++) {
                arr = [];
                for (var k in jsonData[i]) {
                    arr.push(jsonData[i][k]);
                }
                str += arr.join(",") + '\n';
            }

            //encodeURIComponent解决中文乱码
            var exportContent = "\uFEFF";
            var blob = new Blob([exportContent + str], { type: "text/plain;charset=utf-8" });
            saveAs(blob, "消息数据.xls");

        }




    }
})
