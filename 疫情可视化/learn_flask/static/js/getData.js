function get_c1(){     //每次刷新从获取当前最新数据
    $.ajax({
        url:"/c1",
        success:function(data){
            $(".num1 h1").text(data.newconfirm);
            $(".num2 h1").text(data.confirm);
            $(".num3 h1").text(data.No);
            $(".num4 h1").text(data.heal);
            $(".num5 h1").text(data.dead);
            $(".data h5").text(data.newtime);
        },
    })
}
function get_c2(){
    $.ajax({
        url:"/c2",
        success:function(data){
            ChinaOption.series[0].data=data.data;
            ChinaEc.setOption(ChinaOption);
        }
    })
}
function get_l1(){
    $.ajax({
        url:"/l1",
        success:function(data){
            Left1Option.xAxis[0].data=data.day;
            Left1Option.series[0].data=data.confirm;
            Left1Option.series[1].data=data.suspect;
            Left1Option.series[2].data=data.heal;
            Left1Option.series[3].data=data.dead;
            Left1Ec.setOption(Left1Option);
        }
    })
}
function get_l2(){
    $.ajax({
        url:"/l2",
        success:function(data){
            Left2Option.xAxis[0].data=data.day;
            Left2Option.series[0].data=data.confirm;
            Left2Option.series[1].data=data.suspect;
            Left2Option.series[2].data=data.heal;
            Left2Option.series[3].data=data.dead;
            Left2Ec.setOption(Left2Option);
        }
    })
}
function get_r1(){
    $.ajax({
        url:"r1",
        success:function(data){
            Right1Option.xAxis.data=data.city;
            Right1Option.series[0].data=data.number;
            Right1Ec.setOption(Right1Option);
        }
    })
}
function get_r2(){
    $.ajax({
        url:"r2",
        success:function(data){
            Right2Option.series[0].data=data.data;
            Right2Ec.setOption(Right2Option);
        }
    })
}
get_c1();
get_c2();
get_l1();
get_l2();
get_r1();
get_r2();