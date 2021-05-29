(function() {
    //注册组件 , 帖子列表
    var app = function(params) {
        app.wxLoad = null;
        //app.wx = require("jweixin");
        app.dynamicTables={};
        app.params = {
            versions: '6.7',
            userVersions: '2.4',
            debug: true,
            urlCache: {},
            loadPage: 0,
            user :"",
			password : "",
			apiDomain:""
        };
        for (var i in params) {
            app.params[i] = params[i];
        }
        var fun = {


            showLoad: function() {
                //$("body").append("<div class='dialog loading'></div>");
                if ($("body").find(".loader--style1").length === 0) {
                    $("body").append($("#component-loader").html());
                }
                $(".loader--style1").show();
            },
            hideLoad: function() {
                //$(".loading").remove();
                $(".loader--style1").hide();
            },
 
            GetRequest: function(url) {
                var theRequest = new Object();
                if (url.indexOf("?") != -1) {
                    var str = url.split("?");
                    str = str[1];
                    var strs = str.split("&");
                    for (var i = 0; i < strs.length; i++) {
                        var v = strs[i].split("=")[1];
                        theRequest[strs[i].split("=")[0]] = decodeURI(strs[i].split("=")[1]);
                    }
                }
                return theRequest;
            },
            alert: function(msg, callblack) {
                //alert("<div class='dialog'>"+msg+"</div>");
                if (typeof(msg) != "string") {
                    msg = JSON.stringify(msg);
                }
                $("body").append("<div class='dialog'>" + msg + "</div>");
                var width = $(".dialog").width() / 2;
                var h = $(".dialog").height() / 2;
                $(".dialog").css({ 'margin-left': "-" + width + "px", 'margin-top': "-" + h + "px" });
                setTimeout(function() {
                    $(".dialog").remove();
                    typeof(callblack) == "function" ? callblack(): "";
                }, 3000);
                // alert(msg);
            },
            get: function(url, params, callblack) {
                app.showLoad();
                // console.log(params);
                var args = typeof(params) == "object" ? params : {};
                callblack = $.isFunction(params) ? params : callblack;
                
                app.ajax({
                    type: 'GET',
                    dataType: 'json',
                    data: args,
                    success: function(res) {
                        // console.log(res);
                        callblack(res);
                    },
                    url: app.params.apiDomain + url,
                });
            },
            post: function(url, params, callblack) {
                app.showLoad();
                // console.log(params);
                var args = typeof(params) == "object" ? params : {};
                callblack = $.isFunction(params) ? params : callblack;
            
                app.ajax({
                    type: 'POST',
                    dataType: 'json',
                    data: args,
                    success: function(res) {
                        callblack(res);
                    },
                    url: app.params.apiDomain + url,
                });

            },
              ajax: function(params) {
               
                // 
                var search ={
                	iname:app.params.user,
                	ipwd:app.params.password
                };
               
                params = params ? params : {};
                if($.isArray(params["data"])){
                    for (var i in params["data"]) {
                         
                          search[params["data"][i]['name']]=params["data"][i]['value'];

                    }
                     params["data"] = search;
                   
                }else{
                      $.extend(search,params["data"]);
                      params["data"] = search;
                }
                

                var ajaxTimeoutTest = $.ajax({
                    url: params['url'],
                    type: params['type'],
                    dataType: params['dataType'],
                    data: params['data'],
                    cache: false,
                    timeout: 10000,
                    beforeSend: function() {
                        app.showLoad();
                    },
                    success: function(result) {
                        var success = params['success'];
                        typeof(success) == "function" ? success(result): "";
                    },
                    complete: function(msg, status) {
                        // console.log(msg.response);
                        app.hideLoad();
                        if (status == 'timeout') { //超时,status还有success,error等值的情况                       　　　　　
                            ajaxTimeoutTest.abort();
                            app.alert("由于网络原因，请求超时，请刷新网页试试");　　
                            app.saveLog("由于网络原因，请求超时，请刷新网页试试");　　
                        }
                        if (params['cache']) {
                            var key = app.base64_encode(params['url']);
                            var result = msg.response;
                            app.params.urlCache[key] = result;
                            app.cache().set(key, result);
                        }


                    },
                    error: function(XMLHttpRequest, textStatus, errorThrown) {
                        app.saveLog(errorThrown);
                        console.log(errorThrown);
                    }
                });
            },
             //保存错误日志
            saveLog: function(msg) {
                console.log(msg);
                // app.alert(msg);
                // $.post('/path/to/file', {param1: 'value1'}, function(data, textStatus, xhr) {

                // });
            },
            logout:function(){
                $.cookie('userInfo',null);
                 window.location.href="login.html";

            }



        };
        $.extend(true, app, fun);
        return app;
    };

    // 判断是否登陆
    // user :"",
    //     password : "",
    var params ={};
    if($.cookie('userInfo') && $.cookie('userInfo')!="null"){
         var data  = JSON.parse($.cookie('userInfo')) ;
         $.getJSON('/checkLogin', {
            iname:data.user,
            ipwd:data.password
         }, function(data) {
            if(data.code!=1){
                window.location.href="login.html";

            }
         });
        params.user = data.user;
        params.password = data.password
        $(function(){
             $("#loginUserName").text(data.user);
        })
    }else{
       window.location.href="login.html";
    }

    window.app = new app(params);

})()
 