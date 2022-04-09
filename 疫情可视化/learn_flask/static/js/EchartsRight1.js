var Right1Ec = echarts.init(document.getElementById("r1"));
var winwidthr1 = document.documentElement.clientWidth;
var Right1Option = {
    grid: {
        // x: "12%",//x 偏移量
        // y: "20%", // y 偏移量
        // width: "87%", // 宽度
        height: 60+(winwidthr1-600)/112+"%"// 高度
      },
    title:{
        text:"国内现有确诊城市TOP7",
        textStyle:{color:"whitesmoke",fontFamily:"楷体",fontSize:winwidthr1*0.017},
        left:"center"
    },
    color:["#3398DB"],
    tooltip:{   //悬浮框设置
        trigger:"axis",
        axisPointer:{
            type:"shadow"
        },
        textStyle:{fontFamily:"粗体",fontSize:winwidthr1*0.012}
    },
    xAxis:{
        type:"category",
        minInterval:1,
        data:[],
        axisLine:{
            show:true,
            lineStyle:{color:"white"}
        },
        axisLabel:{
            textStyle:{show:true,fontSize:winwidthr1*0.009},
        }
    },
    yAxis:{
        type:"value",
        splitLine :{
            lineStyle:{
                type:'dashed'//虚线
            },
            show: true //隐藏
        },
        axisLine:{
            length:100
        },
        axisLabel:{
            show:true,
            color:"white",
            textStyle:{show:true,fontSize:winwidthr1*0.009},
            formatter:function(value){
                if (value>=10000){
                    value = value /10000+"w";
                } else if(value>=1000){
                    value = value /1000 +"k";
                }
                return value;
            }
        }
    },
    series:[{
        data:[],
        type:"bar",
        barMaxWidth:"50%"
    }]
};
Right1Ec.setOption(Right1Option)

function changer1(){
    var winwidthr12 = document.documentElement.clientWidth
    if (winwidthr12!=winwidthr1) {
        window.onresize = function () {
            Right1Ec.resize()
        };
        // window.addEventListener("resize", function() {
        //     Right2Ec.resize();
        // }
        // );
        Right1Option.title.textStyle.fontSize=winwidthr12*0.017;
        Right1Option.grid.height=60+(winwidthr12-600)/112+"%"
        Right1Option.tooltip.textStyle.fontSize=winwidthr12*0.012;
        Right1Option.xAxis.axisLabel.textStyle.fontSize=winwidthr12*0.009;
        Right1Option.yAxis.axisLabel.textStyle.fontSize=winwidthr12*0.009
        Right1Ec.setOption(Right1Option);
        winwidthr1=winwidthr12;
    }
}
setInterval(changer1,1000)