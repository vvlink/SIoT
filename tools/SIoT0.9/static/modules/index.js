new Vue({
	el: '#appContainer',
	data: {
		projectsList: [],
		editProjectData: {},
		params: {}
	},
	created: function () {
		// `this` 指向 vm 实例
		this.fetchData();
	},
	methods: {
		fetchData: function () {
			this.getProjects();
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
		editProject: function (k) {
			this.editProjectData = this.projectsList[k];
			$("#editProjectBox").modal("show");
		},
		updateprj: function () {
			var that = this;
			app.get("/updateprj", {
				desc: $("#Description").val(),
				pid: this.editProjectData.ID
			}, function (res) {

				if (res.code != 1) {
					app.alert(res.msg);
				} else {
					that.getProjects();
					$("#editProjectBox").modal("hide");
				}
			})
		},
		deleteprj: function (pid) {
			var r = confirm("此操作将会删除账户及些账户下的设备,确认删除吗");
			if (!r) {
				return;
			}
			var that = this;
			app.get("/deleteprj", {
				pid: pid
			}, function (res) {

				if (res.code != 1) {
					app.alert(res.msg);
				} else {
					that.getProjects();
				}
			})
		},
		search: function () {
			var params = {};
			if ($("#projectId").val() != "") {
				params.id = $("#projectId").val();
			}
			params.psize = $("#limit").val();
			this.params = params;
			this.getProjects();
		}

	}
})