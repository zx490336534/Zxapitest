$(function () {

    // 添加
    let $tagAdd = $("#btn-add-tag");  // 1. 获取添加按钮
    $tagAdd.click(function () {   // 2. 点击事件
        fAlert.alertOneInput({
            title: "请输入接口集名称",
            text: "长度限制在20字以内",
            placeholder: "请输入接口集名称",
            confirmCallback: function confirmCallback(inputVal) {
                console.log(inputVal);

                if (inputVal === "") {
                    swal.showInputError('接口集名称不能为空');
                    return false;
                }

                let sDataParams = {
                    "name": inputVal
                };

                $.ajax({
                    // 请求地址
                    url: "/callections/",  // url尾部需要添加/
                    // 请求方式
                    type: "POST",
                    data: JSON.stringify(sDataParams),
                    // 请求内容的数据类型（前端发给后端的格式）
                    contentType: "application/json; charset=utf-8",
                    // 响应数据的格式（后端返回给前端的格式）
                    dataType: "json",
                })
                    .done(function (res) {
                        if (res.errno === "0") {
                            fAlert.alertSuccessToast(inputVal + " 接口集名称添加成功");
                            setTimeout(function () {
                                window.location.reload();
                            }, 1000)
                        } else {
                            swal.showInputError(res.errmsg);
                        }
                    })
                    .fail(function () {
                        message.showError('服务器超时，请重试！');
                    });

            }
        });
    });


    // 编辑
    let $tagEdit = $(".btn-edit");  // 1. 获取编辑按钮
    $tagEdit.click(function () {    // 2. 点击触发事件
        let _this = this;
        let sTagId = $(this).parents('tr').data('id');
        let sTagName = $(this).parents('tr').data('name');
        fAlert.alertOneInput({
            title: "编辑接口集名称",
            text: "你正在编辑 " + sTagName + " 标签",
            placeholder: "请输入接口集名称",
            value: sTagName,
            confirmCallback: function confirmCallback(inputVal) {
                console.log(inputVal);
                if (inputVal === sTagName) {
                    swal.showInputError('接口集名称未变化');
                    return false;
                }
                let sDataParams = {
                    "name": inputVal
                };

                $.ajax({
                    // 请求地址
                    url: "/callections/" + sTagId + "/",  // url尾部需要添加/
                    // 请求方式
                    type: "PUT",
                    data: JSON.stringify(sDataParams),
                    // 请求内容的数据类型（前端发给后端的格式）
                    contentType: "application/json; charset=utf-8",
                    // 响应数据的格式（后端返回给前端的格式）
                    dataType: "json",
                })
                    .done(function (res) {
                        if (res.errno === "0") {
                            // 更新标签成功
                            $(_this).parents('tr').find('td:nth-child(1)').text(inputVal);
                            swal.close();
                            message.showSuccess("接口集名称修改成功");
                        } else {
                            swal.showInputError(res.errmsg);
                        }
                    })
                    .fail(function () {
                        message.showError('服务器超时，请重试！');
                    });

            }
        });
    });


    // 删除
    let $tagDel = $(".btn-del");  // 1. 获取删除按钮
    $tagDel.click(function () {   // 2. 点击触发事件
        let _this = this;
        let sTagId = $(this).parents('tr').data('id');
        let sTagName = $(this).parents('tr').data('name');
        fAlert.alertConfirm({
            title: "确定删除 " + sTagName + " 接口集吗？",
            type: "error",
            confirmText: "确认删除",
            cancelText: "取消删除",
            confirmCallback: function confirmCallback() {

                $.ajax({
                    // 请求地址
                    url: "/callections/" + sTagId + "/",  // url尾部需要添加/
                    // 请求方式
                    type: "DELETE",
                    dataType: "json",
                })
                    .done(function (res) {
                        if (res.errno === "0") {
                            // 更新标签成功
                            message.showSuccess("接口集删除成功");
                            $(_this).parents('tr').remove();
                        } else {
                            swal.showInputError(res.errmsg);
                        }
                    })
                    .fail(function () {
                        message.showError('服务器超时，请重试！');
                    });
            }
        });
    });


    // get cookie using jQuery
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    // Setting the token on the AJAX request
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

});