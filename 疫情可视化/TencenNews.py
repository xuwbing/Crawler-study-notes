import requests,re
import pymysql
import datetime


def Crawler():
    now = str(datetime.datetime.now())[:19]
    url = "https://tophub.today/n/qndg48xeLl"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
    }
    response = requests.get(url=url, headers=headers)
    content = response.text
    num=int(re.findall('<td align="center">(\d+).</td>',content)[-1])
    target = re.findall('itemid.*?>(.*?)<', content)[:num]
    target2 = re.findall('<td>(.*?万)<', content)[:num]
    res = []
    for i in zip(target, target2):
        ans = list(i)
        if not ans[0]:
            continue
        ans.append(now)
        res.append(tuple(ans))
    return res

Data=Crawler()


connect=pymysql.connect(
    host='localhost',
    user='*******',
    password='*******',
    charset='utf8',
    db='news'
)
cursor=connect.cursor()


def insertNews():
    # print('开始更新')                     # 数据量不是很大，不需要加入提示
    step,new=0,0
    SqlSelect = """select 热搜新闻,热搜指数 from tencent_news"""
    cursor.execute(SqlSelect)
    target = []
    for i in cursor.fetchall():
        target.append([i[0], i[1]])
    InsertNews='insert into tencent_news(热搜新闻,热搜指数,最后更新时间) values ("%s","%s","%s")'
    for i in range(len(Data)):
        flag=True
        for j in target:
            if Data[i][0] == j[0]:
                flag=False
                if Data[i][1]!=j[1]:
                    step+=1
                    SqlUpdate='update tencent_news set 热搜指数 = "%s",最后更新时间 = "%s" where 热搜新闻 = "%s"'
                    data=Data[i][1:3]+Data[i][:1]
                    cursor.execute(SqlUpdate % data)
                    connect.commit()
        if not flag:
            continue
        cursor.execute(InsertNews % Data[i])
        new+=1
    connect.commit()
    print(f'腾讯新闻：共更新{step}条数据,新增{new}条数据')


def Run():
    try:
        insertNews()
    finally:
        connect.close()