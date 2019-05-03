new Vue({
   el: '#appContainer',
   data: {
      projectsList: [],
      editProjectData: {},
      params: {}
   },
   created: function () {
      // `this` 指向 vm 实例

   },
   methods: {
      fetchData: function () {

      },

      login: function () {

         $.getJSON('/checkLogin', {
            iname: $("#exampleInputEmail1").val(),
            ipwd: $("#exampleInputPassword1").val()
         }, function (data) {
            if (data.code != 1) {
               alert(data.msg);
               return;
            }
            // 保存信息
            $.cookie('userInfo', JSON.stringify({ user: $("#exampleInputEmail1").val(), password: $("#exampleInputPassword1").val() }));
            window.location.href = "index.html";
         });
      }

   }
})