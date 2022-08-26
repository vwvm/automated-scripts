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


def script_start(running, this_dict):
    """
    前后移动挂机
    """
    for j in range(this_dict.get("count")):
        key_input.press("w")
        sleep(this_dict.get("move_up"))
        if not running.is_set():
            return
        key_input.release("w")
        sleep(0.1)
        key_input.press("s")
        sleep(this_dict.get("move_down"))
        if not running.is_set():
            return
        key_input.release("s")
        sleep(0.1)
        key_input.press("c")
        sleep(0.3)
        key_input.release("c")
        sleep(this_dict.get("休息几秒"))
        if not running.is_set():
            return
        key_input.press("c")
        sleep(0.3)
        key_input.release("c")
        sleep(0.1)
    feed(running, this_dict)


def mouse_press(running, this_dict):
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
    mouse_input.move(this_dict.get("x"), this_dict.get("y"))
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


def feed(running, this_dict):
    """
    吃东西
    """
    key_input.press(str(this_dict.get("eat")))
    sleep(0.1)
    key_input.release(str(this_dict.get("eat")))
    sleep(9)
    if not running.is_set():
        return
    key_input.press(str(this_dict.get("water")))
    sleep(0.1)
    key_input.release(str(this_dict.get("water")))
    sleep(9)
    if not running.is_set():
        return
    mouse_press(running, this_dict)


class Main(threading.Thread):
    this_dict = {}

    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True

    def run(self):
        while self.__running.isSet():
            self.__flag.wait()  # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            script_start(self.__running, this_dict)

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False


def explain(is_down=1, shutdown=0):
    if is_down:
        os.system("shutdown /a")
    if shutdown:
        os.system("shutdown /s /t " + str(shutdown))


def key_event(this_dict):
    with keyboard.Events() as events:
        print("按'-'启动脚本")
        p = Main()
        p.this_dict = this_dict
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
    config_str = ['count', "move_up", "move_down", "休息几秒", "eat", "water", "x", "y", "sum", "shutdown", "is"]

    config_dict = {i: int(config.get('move_config', i)) for i in config_str}
    return config_dict


if __name__ == '__main__':
    this_dict = read_config()
    print(this_dict)
    explain(this_dict.get("is"), this_dict.get("shutdown"))
    key_event(this_dict)
    t = 1
    while t:
        p = input("脚本已经停止，是否重新运行（y/n）")
        if p == 'n':
            break
        if p == 'y':
            key_event(this_dict)
