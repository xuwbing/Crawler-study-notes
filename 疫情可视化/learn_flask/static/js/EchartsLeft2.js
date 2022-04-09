var Left2Ec = echarts.init(document.getElementById("l2"))
var winwidthl2 = document.documentElement.clientWidth
var Left2Option = {
    title:{
        text:"全国新增趋势",
        left:"center",
        textStyle:{color:"whitesmoke",fontFamily:"楷体",fontSize:winwidthl2*0.017}
    },
    tooltip:{
        trigger:"axis",
        textStyle:{fontFamily:"粗体",fontSize:winwidthl2*0.0088},
        axisPointer:{
            type:"line",
            lineStyle:{
                color:"#ffefd5"
            }
        },
    },
    legend:{
        data:["新增确诊","新增无症状","新增治愈","新增死亡"],
        textStyle:{color:"white",fontSize:winwidthl2*0.008},
        itemHeight:winwidthl2*0.005,
        itemGap:winwidthl2*0.001,
        icon: "circle",
        left:"center",
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
            textStyle:{fontSize:winwidthl2*0.009},
        }
    }],
    yAxis:[{
        type:"value",
        axisLabel:{
            show:true,
            color:"white",
            textStyle:{fontSize:winwidthl2*0.009},
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
        name:"新增确诊",
        fontColor:"white",
        type:"line",
        smooth:true,
        data:[]
    },{
        name:"新增无症状",
        type:"line",
        smooth:true,
        data:[]
    },{
        name:"新增治愈",
        type:"line",
        smooth:true,
        data:[]
    },{
        name:"新增死亡",
        type:"line",
        smooth:true,
        data:[]
    }]
};
Left2Ec.setOption(Left2Option);

function changel2(){
    var winwidthl22 = document.documentElement.clientWidth
    if (winwidthl22!=winwidthl2) {
        window.onresize = function () {
            Left2Ec.resize()
        };
        Left2Option.title.textStyle.fontSize=winwidthl22*0.017;
        Left2Option.tooltip.textStyle.fontSize=winwidthl22*0.0088;
        Left2Option.legend.textStyle.fontSize=winwidthl22*0.008;
        Left2Option.legend.itemHeight=winwidthl22*0.005;
        Left2Option.legend.itemGap=winwidthl22*0.001;
        Left2Option.xAxis[0].axisLabel.textStyle.fontSize=winwidthl22*0.009;
        Left2Option.yAxis[0].axisLabel.textStyle.fontSize=winwidthl22*0.009;
        Left2Ec.setOption(Left2Option);
        winwidthl2=winwidthl22;
    }
}
setInterval(changel2,1000)