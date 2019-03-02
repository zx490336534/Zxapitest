'use strict';

const QINIU = {
  'upload': function (args) {
    let domain = args['domain'];
    let up_token_url = args['uptoken_url'];
    let browser_btn = args['browse_btn'];

    let params = {
      browse_button: browser_btn, //上传文件的按钮
      runtimes: 'html5,flash,html4', //上传模式，依次退化
      max_file_size: '100mb', //文件最大允许的尺寸
      chunk_size: '4mb', //分块上传时，每片的大小
      uptoken_url: up_token_url, //ajax请求token的url
      domain: domain, //图片下载时候的域名
      get_new_uptoken: false, //是否每次上传文件都要从业务服务器获取token
      auto_start: true, //如果设置了true,只要选择了图片,就会自动上传
      unique_names: true, // 唯一名字
      multi_selection: false, // 多个选择上传内容
      filters: {
        // 过滤  选择文件的类型
        mime_types: [
          {title: 'Image files', extensions: 'jpg,gif,png,bmp,jepg,tiff'},
        ]
      },
      init: {
        'FileUploaded': function (up, file, info) {
          // 每个文件上传成功后，处理相关的事情
          // 其中 info 是文件上传成功后，服务端返回的json，形式如
          // {
          //    "hash": "Fh8xVqod2MQ1mocfI4S4KpRL6D98",
          //    "key": "gogopher.jpg"
          //  }
          // 参考http://developer.qiniu.com/docs/v6/api/overview/up/response/simple-response.html
          if (args['success']) {
            let success = args['success'];
            success(up, file, info);
          }
        },
        'Error': function (up, err, errTip) {
          // 上传出错时，处理相关的事情
          if (args['error']) {
            let error = args['error'];
            error(up, err, errTip);
          }
        },
        'UploadProgress': function (up, file) {
          // 每个文件上传时，处理相关的事情
          if (args['progress']) {
            args['progress'](up, file);
          }
        },
        'UploadComplete': function () {
          // 队列文件处理完毕后，处理相关的事情
          if (args['complete']) {
            args['complete']();
          }
        }
      }
    };

    // 把args中的参数放到params中去
    for (let key in args) {
      params[key] = args[key];
    }
    return Qiniu.uploader(params);
  }
};
