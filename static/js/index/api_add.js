$(document).ready(function () {
    var flag = 2;
    $("#head_data_add").click(function () {
        var tr = "<tr>" + '<td>' + flag + '</td>'
            + '<td><input type="text" placeholder="请输入请求键" style="border-radius: 5px"></td>'
            + '<td><input type="text" placeholder="请输入请求值" style="border-radius: 5px"></td>'
            + '<td><input type="text" placeholder="请输入注释" style="border-radius: 5px"></td>'
            + '</tr>';
        $("#head_data").append(tr);
        flag++;
    });

    var data_flag = 2;
    $("#add_new_data").click(function () {
        var tr = "<tr>" +
            '<td>' + data_flag + '</td>'
            + '<td><input type="text" placeholder="请输入请求键" style="border-radius: 5px"></td>'
            + '<td><input type="text" placeholder="请输入请求值" style="border-radius: 5px"></td>'
            + '<td><input type="text" placeholder="请输入注释" style="border-radius: 5px"></td>'
            + '</tr>';
        $("#resquest_data").append(tr);
        data_flag++;
    });
});