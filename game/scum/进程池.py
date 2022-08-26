# encoding: utf-8
import os
import time
import random
from multiprocessing import Process
from multiprocessing import Event


def now():
    return str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


def traffic_light(e):  # 红绿灯
    print(now() + ' \033[31m红灯亮\033[0m')  # Flag 默认是False
    while True:
        if e.is_set():  # 如果是绿灯
            time.sleep(2)  # 2秒后
            print(now() + ' \033[31m红灯亮\033[0m')  # 转为红灯
            e.clear()  # 设置为False

        else:  # 如果是红灯
            time.sleep(2)  # 2秒后
            print(now() + ' \033[32m绿灯亮\033[0m')  # 转为绿灯
            e.set()  # 设置为True


def people(e, i):
    if not e.is_set():
        print(now() + ' people %s 在等待' % i)
        e.wait()
    print(now() + ' people %s 通过了' % i)


def explain():
    print("你可以直接按'-'启动脚本")
    print("是否取消系统所有定时关机（y/n）")
    if input() == 'y':
        os.system("shutdown /a")
    if input("是否定时关机（y/n）\n") == 'y':
        print("请输入多少秒后定时关机（单位秒）")
        os.system("shutdown /s /t " + input())


if __name__ == '__main__':
    e = Event()  # 默认为 False，红灯亮
    p = Process(target=explain, args=(e,))  # 红绿灯进程
    p.daemon = True
    p.start()
    process_list = []
    for i in range(6):  # 6人过马路
        time.sleep(random.randrange(0, 4, 2))
        p = Process(target=people, args=(e, i))
        p.start()
        process_list.append(p)

    for p in process_list:
        p.join()
