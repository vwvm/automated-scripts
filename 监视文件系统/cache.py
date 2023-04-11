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


# 可视化选择文件
def get_local_file():
    root = tk.Tk()
    root.withdraw()

    # file_path = filedialog.askopenfilename()
    file_path = filedialog.askdirectory()

    print('文件路径：', file_path)
    return file_path


def read_config(num: int):
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
    start_dirs = ["startDirs" + str(i) for i in range(num)]
    stop_dirs = ["stopDirs" + str(i) for i in range(num)]

    start_configs = [str(config.get('dirs', i)) for i in start_dirs]
    stop_configs = [str(config.get('dirs', i)) for i in stop_dirs]

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


def start_(xx: int):
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


if __name__ == "__main__":
    config_num = int(input("请输入启动配置中的数量\n"))
    read_config(config_num)
    # s1 = Thread(target=start_num1, args=(10, '第' + str(1) + '个线程'))
    # s2 = Thread(target=start_num1, args=(10, '第' + str(2) + '个线程'))
    # s3 = Thread(target=start_num1, args=(10, '第' + str(3) + '个线程'))
    # s1.start()
    # s2.start()
    # s3.start()
    start_(config_num)
