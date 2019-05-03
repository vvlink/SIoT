new Vue({
   el: '#appContainer',
   data: {
      loading: 0,
      topic:'',
   },
   created: function () {
      // `this` 指向 vm 实例
      this.fetchData();
   },
   methods: {
      fetchData: function () {
          var params = app.GetRequest(window.location.search);
          if(params.topic){
            this.topic = params.topic;
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
            }
         })
      }


   }
})