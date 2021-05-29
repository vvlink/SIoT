new Vue({
   el: '#appContainer',
   data: {
      loading: 0,
      topic: '',
      projectsList: [],
      lastMsg: {},
      editProjectData: {},
      params: {},
      webtitle: '智慧农场插件'
   },
   created: function () {
      // `this` 指向 vm 实例
      this.fetchData();
   },
   methods: {
      fetchData: function () {
         var params = app.GetRequest(window.location.search);
         this.getProjects();
         if (params.topic) {
            this.topic = params.topic;
         }

      },
      getlastMsg(projectId, devId) {
      
         var topic = projectId + "/" + devId;
         app.get("/lastmessage?topic=" + topic, {}, function (res) {
            console.log(res);
            if (res.code != 1) {
               app.alert(res.msg);
            }
            if (res.data.length > 0) {
               $("."+projectId + "_" + devId).html("<b>"+res.data[0].Content+"</b> ["+res.data[0].Created+"]") ;
            }

         })
      },

      getProjects: function () {
         var that = this;
         app.get("/projects", this.params, function (res) {
            console.log(res);
            if (res.code != 1) {
               app.alert(res.msg);
            } else {
               that.projectsList = res.data;

            }
         })
      },
      openurl: function (url) {
         window.location.href = 'devices.html?projectID=' + url;
      },

      sendMsg_af: function (af_topic, af_msg) {
         var that = this;
         if (this.loading == 1) {
            return;
         }
         this.loading = 1;
         app.get("/publish", {
            topic: af_topic,
            msg: af_msg,
         }, function (res) {
            that.loading = 0;
            if (res.code != 1) {
               app.alert(res.msg);
            } else {
               app.alert("指令发送成功");
            }
         })
      },

   }
})