new Vue({
   el: '#appContainer',
   data: {
      items: [],
      editData: {},
      params: {},
      webtitle: '全部设备'

   },
   created: function () {
      // `this` 指向 vm 实例
      this.fetchData();
   },
   methods: {
      fetchData: function () {
         var params = app.GetRequest(window.location.search);
         this.params.pid = params.projectID
         if (this.params.pid) {
            this.webtitle = this.params.pid + "的设备";
         }
         this.getDevices();
      },
      search: function () {
         var params = {};
         if ($("#pid").val() != "") {
            params.pid = $("#pid").val();
         }
         if ($("#deviceName").val() != "") {
            params.deviceName = $("#deviceName").val();
         }
         params.psize = $("#limit").val();
         this.params = params;
         this.getDevices();
      },

      getDevices: function () {
         var that = this;
         app.get("/devices", this.params, function (res) {

            if (res.code != 1) {
               app.alert(res.msg);
            } else {
               that.items = res.data;
            }
         })
      },

      clearMessage: function (k) {
         var r = confirm("确认删除该设备的消息吗");
         if (!r) {
            return;
         }
         var data = this.items[k];
         var topic = data.ProjectID + "/" + data.DeviceName;
         var that = this;
         app.get("/clearmsg", {
            topic: topic
         }, function (res) {
            app.alert(res.msg);
         })
      },

      edit: function (k) {
         this.editData = this.items[k];
         $("#editBox").modal("show");
      },
      update: function () {
         var that = this;
         app.get("/updatedev", {
            desc: $("#Description").val(),
            pid: this.editData.ProjectID,
            dname: this.editData.DeviceName,
            id: this.editData.ID
         }, function (res) {

            if (res.code != 1) {
               app.alert(res.msg);
            } else {
               that.getDevices();
               $("#editBox").modal("hide");
            }
         })
      },
      deleteDevice: function (id) {
         var r = confirm("此操作将会删除设备及设备下的消息,确认删除吗");
         if (!r) {
            return;
         }
         var that = this;
         app.get("/deldev", {
            topic: id
         }, function (res) {

            if (res.code != 1) {
               app.alert(res.msg);
            } else {
               that.getDevices();
            }
         })
      },

   }
})