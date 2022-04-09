var Left1Ec = echarts.init(document.getElementById("l1"))
// var winheight=document.documentElement.clientHeight
var winwidthl1 = document.documentElement.clientWidth
var Left1Option = {
    title:{
        text:"全国累计趋势",
        left:"center",
        textStyle:{color:"whitesmoke",fontFamily:"楷体",fontSize:winwidthl1*0.017}
    },
    tooltip:{
        trigger:"axis",
        textStyle:{fontFamily:"粗体",fontSize:winwidthl1*0.0088},
        axisPointer:{
            type:"line",
            lineStyle:{
                color:"#ffefd5"
            }
        },
    },
    legend:{
        data:["累计确诊","累计无症状","累计治愈","累计死亡"],
        textStyle:{color:"white",fontSize:winwidthl1*0.008},
        // left:"center",
        icon: "circle",
        itemHeight:winwidthl1*0.005,
        itemGap:winwidthl1*0.0001,
        bottom:"0%"
    },
    grid:{
        left:"4%",
        right:"6%",
        bottom:"8%",
        top:"15%",
        containLabel:true
    },
    xAxis:[{
        type:"category",
        data:[],      //待导入数据
        axisLine:{
            show:true,
            lineStyle:{color:"white"}
        },
        axisLabel:{
            show:true,
            textStyle:{fontSize:winwidthl1*0.009},
        }
    }],
    yAxis:[{
        type:"value",
        axisLabel:{
            show:true,
            color:"white",
            textStyle:{fontSize:winwidthl1*0.009},
            formatter:function(value){
                if (value>=10000){
                    value = value /10000+"w";
                } else if(value>=1000){
                    value = value /1000 +"k";
                }
                return value;
            }
        },
        axisLine:{
            show:true,
            lineStyle:{color:"white"}
        },
        splitLine:{
            show:true,
            lineStyle:{
                color:"#330867",
                width:1,
                type:"solid",
            }
        }
    }],
    series:[{
        name:"累计确诊",
        fontColor:"white",
        type:"line",
        smooth:true,
        data:[]
    },{
        name:"累计无症状",
        type:"line",
        smooth:true,
        data:[]
    },{
        name:"累计治愈",
        type:"line",
        smooth:true,
        data:[]
    },{
        name:"累计死亡",
        type:"line",
        smooth:true,
        data:[]
    }]
};
Left1Ec.setOption(Left1Option);

function changel1(){
    var winwidthl12 = document.documentElement.clientWidth
    if (winwidthl12!=winwidthl1) {
        window.onresize = function () {
            Left1Ec.resize()
        };
        // window.addEventListener("resize", function() {
        //     Right2Ec.resize();
        // }
        // );
        Left1Option.title.textStyle.fontSize=winwidthl12*0.017;
        Left1Option.tooltip.textStyle.fontSize=winwidthl12*0.0088;
        Left1Option.legend.textStyle.fontSize=winwidthl12*0.008;
        Left1Option.legend.itemHeight=winwidthl12*0.005;
        Left1Option.legend.itemGap=winwidthl12*0.0001
        Left1Option.xAxis[0].axisLabel.textStyle.fontSize=winwidthl12*0.009;
        Left1Option.yAxis[0].axisLabel.textStyle.fontSize=winwidthl12*0.009;
        Left1Ec.setOption(Left1Option);
        winwidthl1=winwidthl12;
    }
}
setInterval(changel1,1000)