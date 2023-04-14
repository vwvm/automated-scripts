#!/usr/bin/python
# -*- coding: UTF-8 -*-
import ctypes
import sys

from pytz import unicode
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from shutil import copyfile, copytree
import tkinter as tk
from tkinter import filedialog
from threading import Thread
from time import sleep, ctime
import time
import os
import configparser

global dirs
global dirStart
global start_configs
global stop_configs
config_num: int


def get_local_file():
    """
     可视化选择文件夹
    @return:
    """
    root = tk.Tk()
    root.withdraw()

    # file_path = filedialog.askopenfilename()
    file_path = filedialog.askdirectory()

    print('文件路径：', file_path)
    return file_path


def read_config(num: int = 1):
    global start_configs
    global stop_configs
    """
    读取配置文件
    @return: 配置文件列表
    """
    #  实例化configParser对象
    config = configparser.ConfigParser()
    # -read读取ini文件

    config.read('config.ini', encoding='UTF-8')
    num = int(config.get("config", "size"))
    start_dirs = ["start" + str(i) for i in range(num)]
    stop_dirs = ["stop" + str(i) for i in range(num)]

    start_configs = [str(config.get('config', i)) for i in start_dirs]
    stop_configs = [str(config.get('config', i)) for i in stop_dirs]

    return


class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        return

    def on_created(self, event):
        dirs1 = str(dirs)
        time.sleep(2)
        path = event.src_path
        if os.path.isdir(path):
            print("dd")
            str4 = str(path).split("\\")
            str5 = dirs1 + str4[-1]
            copytree(event.src_path, str5)
            print("文件夹被创建了 %s" % str5)
        elif os.path.isfile(path):
            str4 = str(path).split("\\")
            str5 = dirs1 + str4[-1]
            copyfile(event.src_path, str5)
            print("文件被创建了 %s" % str5)

        else:
            print("it's a special file(socket,FIFO,device file)")


def start_(xx: int = 1):
    """
        启动器
    @param xx:
    """
    global dirStart
    global dirs
    print(start_configs)
    print(stop_configs)

    for i in range(xx):

        dirStart = start_configs[i]
        dirs = stop_configs[i]
        is_dirs = True
        while is_dirs:
            try:
                # input("按回车选择起点")
                # dirStart = get_local_file()

                if dirStart[-1] != "\\":
                    dirStart += "\\"
                if not os.path.exists(dirStart):
                    os.makedirs(dirStart)
                    print("起点路径设置成功：" + dirStart)
                    is_dirs = False
                if os.path.exists(dirStart):
                    print("起点路径设置成功：" + dirStart)
                    is_dirs = False
            except FileNotFoundError:
                print("输入的路径不合法")

        is_dirs = True
        while is_dirs:
            try:
                # input("按回车选择终点")
                # dirs = get_local_file()
                if dirs[-1] != "\\":
                    dirs += "\\"
                if not os.path.exists(dirs):
                    os.makedirs(dirs)
                    print("终点路径设置成功：" + dirs)
                    is_dirs = False
                if os.path.exists(dirs):
                    print("终点路径设置成功：" + dirs)
                    is_dirs = False
            except FileNotFoundError:
                print("输入的路径不合法")
        event_handler = MyHandler()
        observer = Observer()
        observer.schedule(event_handler, dirStart, recursive=True)
        observer.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        exit()


def start_num1(number: int, string: str):
    for i in range(number):
        print(string + ":" + str(i))
        time.sleep(2)


def is_admin():
    """
        判断是否为管理员权限
    @return:
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if __name__ == "__main__":
    #  实例化configParser对象
    config = configparser.ConfigParser()
    # 如果文件不存在配置config.ini
    if not os.path.exists('config.ini'):
        config_num = int(input("请输入启动配置中的数量\n"))
        file = open("config.ini", 'w', encoding='UTF-8')
        config.read('config.ini', encoding='UTF-8')
        config.add_section("config")
        config.set("config", "size", str(config_num))
        for i in range(config_num):
            print("请选择第%d个起始文件夹" % i)
            temp_dir = get_local_file()
            config.set("config", "start" + str(i), temp_dir)
            print("请选择第%d个结束文件夹" % i)
            temp_dir = get_local_file()
            config.set("config", "stop" + str(i), temp_dir)
        config.write(file)
        file.close()

    name = os.path.basename(__file__)
    print(name)

    if not os.path.exists("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\" + name):
        if input("是否加入启动目录 (y) \n") == 'y':
            if is_admin():
                # 将要运行的代码加到这里
                copyfile("cache8.0.exe",
                         "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\" + name)
                copyfile("config.ini", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\config.ini")
            else:
                if sys.version_info[0] == 3:
                    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
                else:  # in python2.x
                    ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__),
                                                        None, 1)
                exit()

    read_config()

    start_()
