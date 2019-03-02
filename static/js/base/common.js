/*===  navMenuStart ===*/
$(()=>{
    let $navLi = $('#header .nav .menu li')
    $navLi.click(function(){
        $(this).addClass('active').siblings('li').removeClass('active')
    });
});
/*===  navMenuEnd ===*/
