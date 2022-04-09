var winwidthr2 = document.documentElement.clientWidth
var Right2Ec = echarts.init(document.getElementById("r2"));
var testdata = [
    {"name": "python3.6","value": "479"},
    {"name": "Tensorflow2.0","value": "443"},
    {"name": "Django2.2","value": "386"},
    {"name": "Spring Boot","value": "345"},
    {"name": "Pytorch1.0","value": "256"},
    {"name": "Nginx","value": "178"},
    {"name": "清风抽纸","value": "75"},
    {"name": "python","value": "46"},]
var Right2Option = {
    title:{
        text:"近期热搜",
        textStyle:{
            color:"#18BDB9",
            fontFamily:"黑体",
            fontSize:winwidthr2*0.017
        },
        left:"center"
    },
    tooltip:{
        show:false
    },
    series:[{
        type:"wordCloud",
        gridSize:winwidthr2/1536,
        shape:"square",
        sizeRange:[winwidthr2*0.006,winwidthr2*0.042],
        rotationRange:[-45,45,0,90],
        textStyle:{
            normal : {
                fontFamily:'微软雅黑',},
            color: function() {
                return 'rgb(' + [
                    Math.round(Math.random() * 220),
                    Math.round(Math.random() * 220),
                    Math.round(Math.random() * 220)
                ].join(',') + ')';
            }
        },
        right:null,
        bottom:null,
        data:[]
    }]
};
Right2Ec.setOption(Right2Option);
function changer2(){
    var winwidthr22 = document.documentElement.clientWidth
    if (winwidthr22!=winwidthr2) {
        window.onresize = function () {
            Right2Ec.resize()
        };
        // window.addEventListener("resize", function() {
        //     Right2Ec.resize();
        // }
        // );
        Right2Option.title.textStyle.fontSize=winwidthr22*0.017;
        Right2Option.series[0].sizeRange=[winwidthr22*0.006,winwidthr22*0.042];
        Right2Ec.setOption(Right2Option);
        winwidthr2=winwidthr22;
    }
}
setInterval(changer2,1000)