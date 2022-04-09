import pymysql
import datetime
from jieba.analyse import extract_tags


class visit:
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            user='*******',
            password='*******',
            db='covid',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()
        self.res=[]

    def China(self):
        sql = 'select * from chinatotal'
        self.cursor.execute(sql)
        target=self.cursor.fetchall()[-1]
        for i in (4,0,8,2,12,14):
            self.res.append(target[i])

    def Close(self):
        self.cursor.close()
        self.connect.close()

    def run(self):
        self.China()
        self.Close()
        return self.res


class C2:
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            user='*******',
            password='*******',
            db='covid',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()
        self.res=[]

    def Close(self):
        self.cursor.close()
        self.connect.close()

    def Province(self):
        sql="select * from provincetotal"
        self.cursor.execute(sql)
        for i in self.cursor.fetchall():
            self.res.append([i[0],i[3]])
        self.res.append(["南海诸岛","0"])

    def Run(self):
        self.Province()
        self.Close()
        return self.res


class Left:

    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            user='*******',
            password='*******',
            db='covid',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()
        self.res=[]

    def Close(self):
        self.cursor.close()
        self.connect.close()

    def Up(self):
        sql = "select * from chinatotal"
        self.cursor.execute(sql)
        t = []
        for i in self.cursor.fetchall():
            t.append(i)
        flag = 0
        target = 0
        for i in range(len(t) - 1, -1, -1):
            ans = []
            if flag == 7:           # 获得几个数据
                break
            if t[i][-1][8:10] == target:
                continue
            else:
                target = t[i][-1][8:10]
                for j in (0, 2, 8, 12):
                    ans.append(t[i][j])
                ans.append(t[i][-1][5:10])
                self.res.append(ans)
                flag += 1

    def RunUp(self):
        self.Up()
        self.Close()
        return self.res

    def Down(self):
        sql = "select * from chinatotal"
        self.cursor.execute(sql)
        t = []
        for i in self.cursor.fetchall():
            t.append(i)
        flag = 0
        target = 0
        for i in range(len(t) - 1, -1, -1):
            ans = []
            if flag == 7:  # 获得几个数据
                break
            if t[i][-1][8:10] == target:
                continue
            else:
                target = t[i][-1][8:10]
                for j in (1,3,9,-2):
                    ans.append(t[i][j])
                ans.append(t[i][-1][5:10])
                self.res.append(ans)
                flag += 1

    def RunDown(self):
        self.Down()
        self.Close()
        return self.res


class R1:
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            user='*******',
            password='*******',
            db='covid',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()
        self.res=[]

    def Close(self):
        self.cursor.close()
        self.connect.close()

    def Up(self):
        sql = "select * from provincedetail"
        self.cursor.execute(sql)
        t = []
        for i in self.cursor.fetchall():
            t.append(list(i))
        t.sort(key=lambda x: int(x[3]), reverse=True)
        for i in range(len(t)):
            if len(self.res)==7:
                break
            if t[i][1]=="境外输入":
                continue
            self.res.append([t[i][1],t[i][3]])

    def Run(self):
        self.Up()
        self.Close()
        return self.res


class R2:

    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            user='*******',
            password='*******',
            db='news',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()
        self.res=[]

    def Close(self):
        self.cursor.close()
        self.connect.close()

    def Down(self):
        target = []
        for j in ('baidu_news', 'weibo_news', 'tencent_news', 'toutiao_news'):
            sql = f"select * from {j}"
            self.cursor.execute(sql)
            t = []
            for i in self.cursor.fetchall():
                t.append(i)
            flag = [str(datetime.datetime.now() - datetime.timedelta(days=i))[8:10] for i in range(7)]
            for i in range(len(t) - 1, -1, -1):
                if t[i][-1][8:10] not in flag:
                    continue
                ans = [t[i][0], t[i][1], t[i][-1]]
                target.append(ans)
        demo = {}
        for i in target:
            for j in extract_tags(i[0]):
                if j in ("男子", "女子"):
                    continue
                if j not in demo:
                    demo[j] = 1
                else:
                    demo[j] += 1
        self.res = sorted(demo.items(), key=lambda x: x[1])[len(demo.keys()) - 70:]
        for i in range(len(self.res)):
            self.res[i] = list(self.res[i])
            self.res[i][1] += (i + 1) * (i + 1)

    def Run(self):
        self.Down()
        self.Close()
        return self.res

if __name__ == "__main__":
    # print(visit().run())
    # print(C2().Run())
    # print(Left().RunUp())
    # print(Left().RunDown())
    # print(R2().Run())
    R2().Run()