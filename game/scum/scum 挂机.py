import configparser
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, thread
from time import sleep
import os
import threading

from pynput import keyboard
from pynput import mouse

key_input = keyboard.Controller()
mouse_input = mouse.Controller()
mouse_button = mouse.Button


def script_start(running):
    """
    前后移动挂机
    """
    for j in range(15):
        key_input.press("w")
        sleep(10)
        if not running.is_set():
            return
        key_input.release("w")
        sleep(0.1)
        key_input.press("s")
        sleep(10)
        if not running.is_set():
            return
        key_input.release("s")
        sleep(0.1)
        key_input.press("c")
        sleep(0.3)
        key_input.release("c")
        sleep(10)
        if not running.is_set():
            return
        key_input.press("c")
        sleep(0.3)
        key_input.release("c")
        sleep(0.1)
    feed(running)


def mouse_press(running):
    if not running.is_set():
        return
    sleep(1)
    key_input.press(keyboard.Key.tab)
    sleep(0.1)
    key_input.release(keyboard.Key.tab)
    sleep(0.5)
    key_input.press('1')
    sleep(0.1)
    key_input.release('1')
    sleep(0.5)
    for i in range(20):
        mouse_input.move(-100, -100)
        sleep(0.1)
    mouse_input.move(450, 250)
    sleep(0.1)
    mouse_input.press(mouse_button.right)
    sleep(0.1)
    mouse_input.release(mouse_button.right)
    sleep(0.5)
    mouse_input.move(20, 20)
    sleep(0.5)
    mouse_input.press(mouse_button.left)
    sleep(0.1)
    mouse_input.release(mouse_button.left)
    sleep(0.5)
    key_input.press(keyboard.Key.tab)
    sleep(0.1)
    key_input.release(keyboard.Key.tab)
    sleep(0.1)


def feed(running):
    """
    吃东西
    """
    key_input.press("4")
    sleep(0.1)
    key_input.release("4")
    sleep(9)
    if not running.is_set():
        return
    key_input.press("3")
    sleep(0.1)
    key_input.release("3")
    sleep(9)
    if not running.is_set():
        return
    mouse_press(running)


class Main(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True

    def run(self):
        while self.__running.isSet():
            self.__flag.wait()  # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            script_start(self.__running)

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False


def explain():
    print("是否取消系统所有定时关机（y/n）")
    if input() == 'y':
        os.system("shutdown /a")
    if input("是否定时关机（y/n）\n") == 'y':
        print("请输入多少秒后定时关机（单位秒）")
        os.system("shutdown /s /t " + input())


def key_event():
    with keyboard.Events() as events:
        print("按'-'启动脚本")
        p = Main()
        is_right = 0
        down_right = 0
        for event in events:
            if event.key == keyboard.KeyCode.from_char('='):
                os.system("shutdown /a")
            if event.key == keyboard.KeyCode.from_char('-'):
                is_right = 1
                continue
            if event.key == keyboard.KeyCode.from_char('0'):
                is_right = 0
                down_right = 1
                continue
            if is_right:
                print("启动脚本")
                is_right = 0
                p.start()
                print("按'0'停止脚本")
            if down_right:
                print("脚本即将停止")
                down_right = 0
                p.stop()
                break


def read_config():
    #  实例化configParser对象
    config = configparser.ConfigParser()
    # -read读取ini文件
    config.read('config.ini', encoding='UTF-8')

    # -get(section,option)得到section中option的值，返回为string类型
    userName = config.get('move_config', 'userName')
    password = config.get('move_config', 'password')
    operator = config.get('move_config', 'operator')


if __name__ == '__main__':
    # threading.Thread(target=explain).start()
    # threading.Thread(target=key_event).start()
    explain()
    key_event()
    t = 1
    while t:
        p = input("脚本已经停止，是否重新运行（y/n）")
        if p == 'n':
            break
        if p == 'y':
            key_event()
