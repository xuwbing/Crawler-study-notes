import requests
import json
import datetime
import pymysql


def Crawler():
    url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    with open('tencent.json', 'w+') as f:
        f.write(response.text)
        f.close()


def Read():
    file = open('tencent.json', 'r')
    res = file.read()
    data = json.loads(res)
    return data['data']


Crawler()
Data = Read()
LastUpdateTime = Data['diseaseh5Shelf']['lastUpdateTime']
print(LastUpdateTime)
Today = str(datetime.datetime.now())[:19]
ChinaTotal={}
ProvinceDetail = []


def DataChina():
    global ChinaTotal
    ChinaTotal = {
        'HistoryConfirm': Data['diseaseh5Shelf']['chinaTotal']['confirm'],  # 累计确诊
        'Confirm': Data['diseaseh5Shelf']['chinaAdd']['confirm'],  # 新增累计确诊

        'NowHeal': Data['diseaseh5Shelf']['chinaTotal']['heal'],  # 累计治愈
        'NewHeal': Data['diseaseh5Shelf']['chinaAdd']['heal'],  # 新增累计治愈

        'NowLocalConfirm': Data['diseaseh5Shelf']['chinaTotal']['localConfirm'],  # 现有确诊(不含港澳台)
        'NewLocalConfirm': Data['diseaseh5Shelf']['chinaAdd']['localConfirmH5'],  # 新增现有确诊(不含港澳台)

        'NowConfirm': Data['diseaseh5Shelf']['chinaTotal']['nowConfirm'],  # 现有确诊(含港澳台)
        'NewConfirm': Data['diseaseh5Shelf']['chinaAdd']['nowConfirm'],  # 新增现有确诊(含港澳台)

        'NoSymptoms': Data['diseaseh5Shelf']['chinaTotal']['noInfect'],  # 无症状感染者
        'NewNoSymptoms': Data['diseaseh5Shelf']['chinaAdd']['noInfect'],  # 新增无症状感染者

        'Offshore': Data['diseaseh5Shelf']['chinaTotal']['importedCase'],  # 境外输入病例
        'NewOffshore': Data['diseaseh5Shelf']['chinaAdd']['importedCase'],  # 新增境外输入病例

        'NowDead': Data['diseaseh5Shelf']['chinaTotal']['dead'],  # 累计死亡
        'NewDead': Data['diseaseh5Shelf']['chinaAdd']['dead'],  # 新增累计死亡
    }


def DataPro():
    global ProvinceDetail
    for i in range(34):
        res = [[Data['diseaseh5Shelf']['areaTree'][0]['children'][i]['name'],  # 省的名字
                Data['diseaseh5Shelf']['areaTree'][0]['children'][i]['today']['confirm'],  # 新增确诊
                Data['diseaseh5Shelf']['areaTree'][0]['children'][i]['total']['nowConfirm'],  # 现有确诊
                Data['diseaseh5Shelf']['areaTree'][0]['children'][i]['total']['confirm'],  # 累计确诊
                Data['diseaseh5Shelf']['areaTree'][0]['children'][i]['today']['wzz_add'],  # 新增无症状
                Data['diseaseh5Shelf']['areaTree'][0]['children'][i]['total']['wzz'],  # 累计无症状
                Data['diseaseh5Shelf']['areaTree'][0]['children'][i]['total']['dead'],  # 累计死亡
                Data['diseaseh5Shelf']['areaTree'][0]['children'][i]['total']['heal']]]  # 累计治愈
        Children = len(Data['diseaseh5Shelf']['areaTree'][0]['children'][i]['children'])
        for j in range(Children):
            name = Data['diseaseh5Shelf']['areaTree'][0]['children'][i]['children'][j]['name']
            if name == '地区待确认' or name == '待确认':
                continue
            else:
                ans = [name,  # 市名
                       Data['diseaseh5Shelf']['areaTree'][0]['children'][i]['children'][j]['today']['confirm'],
                       # 新增确诊
                       Data['diseaseh5Shelf']['areaTree'][0]['children'][i]['children'][j]['total']['nowConfirm'],
                       # 现有确诊
                       Data['diseaseh5Shelf']['areaTree'][0]['children'][i]['children'][j]['total']['confirm'],
                       # 累计确诊
                       Data['diseaseh5Shelf']['areaTree'][0]['children'][i]['children'][j]['total']['heal'],  # 累计治愈
                       Data['diseaseh5Shelf']['areaTree'][0]['children'][i]['children'][j]['total']['dead'],  # 累计死亡
                       ]
            res.append(ans)
        ProvinceDetail.append(res)

connect = pymysql.connect(
    host='localhost',
    user='*******',
    password='*******',
    charset='utf8',
    db='covid'
)
cursor = connect.cursor()


def insertChina():
    SqlSelect = """select 最后更新时间 from chinatotal"""
    cursor.execute(SqlSelect)
    FinallyTime = cursor.fetchall()[-1][0]
    if FinallyTime == LastUpdateTime:
        print("当前已是最新数据")
    else:
        print("开始更新数据")
        InsertChina = """insert into chinatotal(累计确诊,新增累计确诊,累计治愈,新增累计治愈,现有确诊_不含港澳台,
                      新增现有确诊_不含港澳台,现有确诊,新增现有确诊,无症状感染者,新增无症状感染者,境外输入,新增境外输入,
                      累计死亡,新增累计死亡,最后更新时间) values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")"""
        ChinaValues = []
        for i in ChinaTotal.values():
            ChinaValues.append(str(i))
        ChinaValues.append(LastUpdateTime)
        ChinaValues = tuple(ChinaValues)
        cursor.execute(InsertChina % ChinaValues)
        connect.commit()
        print("更新完毕")


def insertProTotal():
    SqlSelect = """select 最后更新时间 from provincetotal"""
    cursor.execute(SqlSelect)
    FinallyTime = cursor.fetchall()[0][0]
    if FinallyTime == LastUpdateTime:
        print("当前已是最新数据")
    else:
        print("开始更新数据")
        SqlClear = 'truncate provincetotal'
        cursor.execute(SqlClear)
        InsertPro = """insert into provincetotal(省名,新增确诊,现有确诊,累计确诊,新增无症状感染者,
                        累计无症状感染者,累计死亡,累计治愈,最后更新时间)
                        values ("%s","%s","%s","%s","%s","%s","%s","%s","%s")"""
        for i in ProvinceDetail:
            i[0].append(LastUpdateTime)
            arr = tuple(map(str, i[0]))
            cursor.execute(InsertPro % arr)
        connect.commit()
        print("更新完毕")


def insertProDetail():
    SqlSelect = 'select 最后更新时间 from provincedetail'
    cursor.execute(SqlSelect)
    FinallyTime = cursor.fetchall()[0][0]
    if FinallyTime==LastUpdateTime:
        print("当前已是最新数据")
    else:
        print("开始更新数据")
        SqlClear = 'truncate provincedetail'
        cursor.execute(SqlClear)
        InsertPro = 'insert into provincedetail(省名,市名,新增确诊,现有确诊,累计确诊,累计治愈,累计死亡,最后更新时间) values ("%s","%s","%s","%s","%s","%s","%s","%s")'
        for i in ProvinceDetail:
            if i[0][0] in ('香港','澳门','北京','天津','上海','重庆'):
                arr=[i[0][0]]
                for j in (0,1,2,3,7,6):
                    arr.append(i[0][j])
                arr.append(LastUpdateTime)
                arr=tuple(arr)
                cursor.execute(InsertPro % arr)
                connect.commit()
                continue
            for j in range(1,len(i)):
                arr=i[j]
                arr.insert(0,i[0][0])
                arr.append(LastUpdateTime)
                arr=tuple(map(str,arr))
                cursor.execute(InsertPro % arr)
            connect.commit()
        print("更新完毕")


def Run():
    try:
        DataChina()
        DataPro()
        insertChina()
        insertProTotal()
        insertProDetail()
    finally:
        connect.close()
