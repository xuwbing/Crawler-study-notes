var ChinaEc=echarts.init(document.getElementById('c2'));
var winwidthc = document.documentElement.clientWidth
var ChinaOption={
    title:{
        text:"",
        subtext:"",
        x:"left",
    },
    tooltip:{
        trigger:"item",
        backgroundColor:"#f7430d",
        padding:winwidthc*0.015, //悬浮框大小
        textStyle:{fontFamily:"华文行楷",fontSize:winwidthc*0.015,color:"white"},    //悬浮框字体设置
    },
    visualMap:{     //图例设置
        show:true,
        x:"left",
        y:winwidthc*0.235,
        itemHeight:winwidthc*0.009,
        itemWidth:winwidthc*0.01,
        textStyle:{
            fontSize:winwidthc*0.01,
        },
        splitList:[
            {start: 1, end:9},
            {start: 10, end: 99},      
            {start: 100, end: 999},
            {start: 1000, end: 9999},  
            {start: 10000}
        ],
        color:["#8A3310","#C64918","#E55B25","#F2AD92","#F9DCD1"]
    },
    series:[{
        name:"累计确诊人数",
        type:"map",
        mapType:"china",
        roam:false,
        itemStyle:{
            normal:{
                bordeWidth:winwidthc*0.003,
                borderColor:"#009fe8",
                areaColor:"#ffefd5",
            },
            emphasis:{
                bordeWidth:winwidthc*0.003,
                borderColor:"#4b0082",
                areaColor:"#fff",
            }
        },
        label:{
            normal:{
                show:true,
                fontSize:winwidthc*0.0089
            },
            emphasis:{
                show:true,
                fontSize:winwidthc*0.017,
                textStyle:{color:"black"}
            }
        },
        data:[]
    }]
};
// window.addEventListener("resize", function() {  //看了一天官方文档没学会,copy一下别人的就实现了a_a,还发现实际效果不好
//     ChinaEc.resize();
// });
ChinaEc.setOption(ChinaOption);

function changec(){
    var winwidthc2 = document.documentElement.clientWidth
    if (winwidthc2!=winwidthc) {
        window.onresize = function () {
            ChinaEc.resize()
        };
        ChinaOption.tooltip.padding=winwidthc2*0.015;
        ChinaOption.tooltip.textStyle.fontSize=winwidthc2*0.015;
        ChinaOption.visualMap.y=winwidthc2*0.235;
        ChinaOption.visualMap.textStyle.fontSize=winwidthc2*0.01;
        ChinaOption.visualMap.itemHeight=winwidthc2*0.009;
        ChinaOption.visualMap.itemWidth=winwidthc2*0.01;
        ChinaOption.series[0].itemStyle.normal.bordeWidth=winwidthc2*0.003;
        ChinaOption.series[0].itemStyle.emphasis.bordeWidth=winwidthc2*0.003;
        ChinaOption.series[0].label.normal.fontSize=winwidthc2*0.0089;
        ChinaOption.series[0].label.emphasis.fontSize=winwidthc2*0.017;
        ChinaEc.setOption(ChinaOption);
        winwidthc=winwidthc2;
    }

}
setInterval(changec,1000);