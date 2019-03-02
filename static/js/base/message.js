"use strict";

// 消息提示框
function Message() {
  // 判断是否加载
  this.isAppended = false;
  // 提示框的宽度
  this.wrapperWidth = 400;
  // 提示框的高度
  this.wrapperHeight = 48;
  // 提示框初始化样式
  this.initStyle();
  // 提示框初始化元素
  this.initElement();
  // 提示框监听关闭按钮
  this.listenCloseEvent();
}

// 初始化样式
Message.prototype.initStyle = function () {
  // 错误消息文字和背景样式
  this.errorStyle = {
    "wrapper": {
      "background": "#f8d7da",
      "color": "#dc3545"
    },
    "close": {
      "color": "#993d3d"
    }
  };
  // 成功消息文字和背景样式
  this.successStyle = {
    "wrapper": {
      "background": "#d4edda",
      "color": "#28a745"
    },
    "close": {
      "color": "#468847"
    }
  };
  // 描述信息文字和背景样式
  this.infoStyle = {
    "wrapper": {
      "background": "#d1ecf1",
      "color": "#17a2b8"
    },
    "close": {
      "color": "#5bc0de"
    }
  };
};

// 初始化元素
Message.prototype.initElement = function () {
  // 设置提示框元素
  this.wrapper = $("<div></div>");
  // 设置提示框整体样式
  this.wrapper.css({
    'padding': '10px',
    'font-size': '14px',
    'width': this.wrapperWidth,
    'position': 'fixed',
    'z-index': 99999,
    'left': 'calc(50% - ' + this.wrapperWidth / 2 + 'px)',
    'top': -this.wrapperHeight,
    'height': this.wrapperHeight,
    'box-sizing': 'border-box',
    'border': '1px solid #ddd',
    'border-radius': '5px',
    'line-height': 'calc(' + this.wrapperHeight / 2 + 'px)',
    'font-weight': 600
  });
  // 生成关闭按钮
  this.closeBtn = $("<span>×</span>");
  // 关闭按钮的样式
  this.closeBtn.css({
    'float': 'right',
    'cursor': 'pointer',
    'font-size': '24px',
    'font-weight': 500
  });
  // 提示文字的元素生成
  this.messageSpan = $("<span class='py-message'></span>");
  // 将提示文字的元素和关闭按钮添加到提示框中
  this.wrapper.append(this.messageSpan);
  this.wrapper.append(this.closeBtn);
};

// 关闭按钮的事件
Message.prototype.listenCloseEvent = function () {
  var _this = this;

  // 点击关闭
  this.closeBtn.click(function () {
    _this.wrapper.animate({ "top": -_this.wrapperHeight });
  });
};

// 显示异常
Message.prototype.showError = function (message) {
  this.show(message, "error");
};

Message.prototype.showSuccess = function (message) {
  this.show(message, "success");
};

Message.prototype.showInfo = function (message) {
  this.show(message, "info");
};

// 提示框的显示
Message.prototype.show = function (message, type) {
  var _this2 = this;

  // 如果没有添加  则添加
  if (!this.isAppended) {
    $(document.body).append(this.wrapper);
    this.isAppended = true;
  }

  // 将各种提示的文字添加对应不同的样式
  this.messageSpan.text(message);
  if (type === "error") {
    this.wrapper.css(this.errorStyle['wrapper']);
    this.closeBtn.css(this.errorStyle['close']);
  } else if (type === "info") {
    this.wrapper.css(this.infoStyle['wrapper']);
    this.closeBtn.css(this.infoStyle['close']);
  } else if (type === "success") {
    this.wrapper.css(this.successStyle['wrapper']);
    this.closeBtn.css(this.successStyle['close']);
  }
  // 设置两秒后自动关闭
  this.wrapper.animate({ "top": 0 }, function () {
    setTimeout(function () {
      _this2.wrapper.animate({ "top": -_this2.wrapperHeight });
    }, 2500);
  });
};
// 将对象绑定到 window 上
window.message = new Message();
