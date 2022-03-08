"""email: 1850309703@qq.com / christinecunningham053@gmail.com"""
"""第一次使用class编写python。有错误或不完善的地方希望得到指点"""
from urllib.parse import unquote
import re, os, time, random, requests


class get_picture:
    def __init__(self, settings=None):
        if settings is None:
            settings = setting
        else:
            quit()
        self.U_A = settings['User_A']
        self.Proxy = settings['Proxy']
        self.proxy = settings['Proxy_yes_no']
        self.sleep = settings['time_sleep']
        self.start = settings['sleep_start']
        self.end = settings['sleep_end']
        self.address = settings['save_address']
        self.target, self.name_mkdir, self.more_mkdir, self.mkdir_all = [], [], [], []
        self.size_picture = ['1024x768', '1280x720', '1280x1024', '1440x900', '1920x1080', '1920x1200', '1920x1440']

    def get_json(self):
        file_json = open('json_1.txt', 'a+', encoding='utf-8-sig')
        if not self.U_A:
            print('请输入User-Agent')
            quit()
        for i in range(28):  # 共28页图片
            header = {'User-Agent': random.choice(self.U_A)}
            if self.sleep:
                if type(self.start) == type(self.end) == int and self.end > self.start >= 0:
                    time_random_json = round(random.uniform(self.start, self.end), 3)
                    print('随机等待时间为:', time_random_json, '秒')
                    time.sleep(time_random_json)
                else:
                    print('请输入正确的等待时间范围')
                    quit()
            url = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page=' + str(
                i) + '&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735'
            if type(self.proxy) == bool:
                if self.proxy:
                    if not self.Proxy:
                        print('请输入代理地址或不设置代理')
                        quit()
                    proxies_json = {'http': 'http://' + random.choice(self.Proxy)}
                    response = requests.get(url=url, headers=header, proxies=proxies_json)
                    file_json.write(response.text + '\n')
                elif not self.proxy:
                    response = requests.get(url=url, headers=header)
                    file_json.write(response.text + '\n')
            else:
                print('proxy的值请输入True或False')
                quit()
            print('已获取第' + str(i + 1) + '条json数据')
        file_json.close()

    def read_json(self):
        file_read = open('json_1.txt', 'r', encoding='utf-8-sig')
        connect = file_read.read()
        connect = unquote(connect, 'utf-8')
        self.target = re.findall('"sProdImgNo_\d":"(.*?)"|"sProdName":"(.*?)"', connect)
        self.target = list(map(list, self.target))
        file_read.close()
        for i in range(len(self.target)):
            if '' in self.target[i]:
                self.target[i].remove('')
        """正则筛选时筛选到了空字符串，暂时不知道正则语句怎么修改"""

    def make_mkdir(self):
        num_target = len(self.target)
        for i in range(num_target):
            for j in self.target[i]:
                if 'http' not in j:
                    if j in self.mkdir_all:
                        self.more_mkdir.append(j)
                    else:
                        self.mkdir_all.append(j)
        self.more_mkdir = list(set(self.more_mkdir))
        for i in range(len(self.more_mkdir)):
            self.more_mkdir[i] = [self.more_mkdir[i], 0]
        for i in range(num_target):
            """上下有重复的部分，可以考虑优化"""
            for j in self.target[i]:
                if 'http' in j:
                    self.target[i][0] = self.target[i][0].replace('jpg/200', 'jpg/0')
                else:
                    if j.replace('壁纸', '') in self.name_mkdir:
                        for k in range(len(self.more_mkdir)):
                            if j == self.more_mkdir[k][0]:
                                self.more_mkdir[k][1] += 1
                                j += str(self.more_mkdir[k][1])
                                self.target[i] = [j.replace('壁纸', '')]
                                self.name_mkdir.append(j.replace('壁纸', ''))
                    elif ':' in j:
                        j = j.replace(':', '比')
                        self.target[i] = [j]
                        self.name_mkdir.append(j)
                    else:
                        self.target[i] = [j.replace('壁纸', '')]
                        self.name_mkdir.append(j.replace('壁纸', ''))
        try:
            os.mkdir(self.address)
        except:
            pass
        for i in self.name_mkdir:
            try:
                os.mkdir(self.address + '/' + i)
            except:
                pass
        """创建下载目录文件夹"""

    def download(self):  # 可以调用idm下载，理论上速度会更快
        page = 0
        for i in self.target:
            name_url = i[0]
            if 'No_1' in name_url:
                continue
            proxies = {'http': 'http://' + random.choice(self.Proxy)}
            headers = {'User-Agent': random.choice(self.U_A)}
            time_random_picture = round(random.uniform(self.start, self.end), 3)
            print('随机等待时间为:', time_random_picture, '秒')
            time.sleep(time_random_picture)
            if 'http' in name_url:
                response_picture = requests.get(url=name_url, headers=headers, proxies=proxies)
                connect_picture = response_picture.content
                size = int(re.findall(r'No_(\d).', name_url)[0]) - 2
                """文件命名时声明分辨率大小"""
                with open(self.address + '/' + self.name_mkdir[page] + '/' +
                          self.name_mkdir[page] + self.size_picture[size] + '.jpg', 'wb+') as f:
                    f.write(connect_picture)
                print(self.name_mkdir[page] + self.size_picture[size] + '已下载完毕')
            else:
                page += 1

    def run(self):
        self.get_json()
        self.read_json()
        self.make_mkdir()
        self.download()


if __name__ == '__main__':
    setting = {  # 相关设置
        'User_A': [
            "Mozilla/5.0 (X11; U; Linux; hu-HU) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3)  Arora/0.4 ("
            "Change: 388 835b3b6) "],  # 填入请求头
        'Proxy': [],  # 填入代理地址
        'Proxy_yes_no': False,  # 是否使用代理地址
        'time_sleep': True,  # 是否随机暂停
        'sleep_start': 1,  # 暂停时间范围，左区间
        'sleep_end': 3,  # 暂停时间范围，右区间    暂停时间为从左区间到右区间随机一个数
        'save_address': r"C:\Users\admin\Desktop\王者荣耀壁纸"  # 保存的路径
    }
    get_picture().run()
