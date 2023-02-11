import configparser
import time

import requests


def script_entrance_lottery():
    #  实例化configParser对象
    config = configparser.ConfigParser()
    # -read读取ini文件
    config.read('config.ini', encoding='UTF-8')
    cookie = config.get('lottery_config', "cookie")
    token = config.get('lottery_config', "token")
    lottery_number = config.get('lottery_config', "lottery_number")
    lottery_time = config.get('lottery_config', "lottery_time")

    url = "http://003.cnscum.com:5997/api/rotate/dorotate"
    headers = {"Accept": 'application/json, text/plain, */*',
               "Accept-Encoding": 'gzip, deflate',
               "Accept-Language": 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
               "Connection": 'keep-alive',
               # "Cookie": cookie,
               "DNT": '1',
               "Host": '003.cnscum.com:5997',
               "Referer": "http://003.cnscum.com:5997/rotate",
               "token": token,
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36}"}

    for i in range(int(lottery_number)):
        print(requests.get(url, headers))
        time.sleep(int(lottery_time) / 1000)
    if (input("是否继续抽奖 y?") == "y"):
        script_entrance_lottery()