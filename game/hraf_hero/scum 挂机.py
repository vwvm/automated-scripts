import threading
from time import sleep
import os
import time

from pynput import keyboard
from pynput import mouse

key_input = keyboard.Controller()
mouse_input = mouse.Controller()
mouse_button = mouse.Button


def mouse_press():
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


def feed():
    key_input.press("4")
    sleep(0.1)
    key_input.release("4")
    sleep(9)
    key_input.press("3")
    sleep(0.1)
    key_input.release("3")
    sleep(9)
    mouse_press()


def on_press():
    for i in range(6):
        for j in range(100):
            key_input.press("w")
            sleep(10)
            key_input.release("w")
            sleep(0.1)
            key_input.press("s")
            sleep(10)
            key_input.release("s")
            sleep(0.1)
            key_input.press("c")
            sleep(0.3)
            key_input.release("c")
            sleep(10)
            key_input.press("c")
            sleep(0.3)
            key_input.release("c")
            sleep(0.1)
        feed()


def start():
    with keyboard.Events() as events:
        for event in events:
            if event.key == keyboard.KeyCode.from_char('-'):
                print("脚本启动")
                on_press()
                break


def timed_shutdown():
    print("你可以直接按'-'启动脚本")
    print("是否取消系统所有定时关机（y/n）")
    if input() == 'y':
        os.system("shutdown /a")
    if input("是否定时关机（y/n）\n") == 'y':
        print("请输入多少秒后定时关机（单位秒）")
        os.system("shutdown /s /t " + input())
    with keyboard.Events() as events:
        for event in events:
            if event.key == keyboard.KeyCode.from_char('='):
                os.system("shutdown /a")
                break


if __name__ == '__main__':
    # 创建多线程
    thread_1 = threading.Thread(target=timed_shutdown)
    thread_2 = threading.Thread(target=start)
    thread_1.start()
    thread_2.start()
