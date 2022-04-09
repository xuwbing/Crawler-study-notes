import BaiduNews
import TencenNews
import TouTiaoNews
import WeiboNews
import pymysql
import datetime
import TencentCovid


def Run():
    BaiduNews.Run()
    TencenNews.Run()
    TouTiaoNews.Run()
    WeiboNews.Run()


def delete():
    global flag
    connect = pymysql.connect(
        host='localhost',
        user='*******',
        password='*******',
        charset='utf8',
        db='news'
    )
    cursor = connect.cursor()
    for news in ('weibo_news', 'tencent_news', 'baidu_news', 'toutiao_news'):
        sql = f'select * from {news}'
        arr, ans= [], []
        cursor.execute(sql)
        for data in cursor.fetchall():
            arr.append(data)
        for cut in range(len(arr)):
            if arr[cut][-1][8:10] != TargetTime:
                ans.append(arr[cut])
        if len(ans)!=len(arr):
            flag+=1
        SqlDel = f'truncate table {news}'
        InsertNews = f'insert into {news}(热搜新闻,热搜指数,最后更新时间) values ("%s","%s","%s")'
        cursor.execute(SqlDel)
        for end in ans:
            cursor.execute(InsertNews % end)
        connect.commit()

now=str(datetime.datetime.now())[:16]
TargetTime=str(datetime.datetime.now()+datetime.timedelta(days=-7))[8:10]
flag=0
if now[11:]=="12:30":
    delete()
    flag+=1
else:pass
f=open('flask.log','a')
try:
    if int(now[14:])==30:
        Run()
        TencentCovid.Run()
        f.write(f"{now} time work two \n")
        if flag==1:
            f.write("try del\n")
        elif flag==2:
            f.write("del yes\n")
    else:
        Run()
        f.write(f"{now} time work one \n")
except:
    f.write(f"{now} error {now} \n")
f.close()