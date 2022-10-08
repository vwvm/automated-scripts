from time import sleep

from pynput import keyboard
from pynput.keyboard import Controller

key_input = Controller()


def lift_right(key):
    # 上下移动收获
    for i in range(22):
        key_input.press(key)
        sleep(0.3)
        key_input.release(key)
        sleep(0.1)
        key_input.press("a")
        sleep(0.1)
        key_input.release("a")
        sleep(0.1)
        key_input.press("1")
        sleep(0.1)
        key_input.release("1")
        sleep(0.1)
        key_input.press("d")
        sleep(0.1)
        key_input.release("d")
        sleep(0.1)
        key_input.press("1")
        sleep(0.1)
        key_input.release("1")
        sleep(0.1)


def up_down(key):
    # 左右移动收获
    for i in range(20):
        key_input.press(key)
        sleep(0.3)
        key_input.release(key)
        sleep(0.1)
        key_input.press("w")
        sleep(0.1)
        key_input.release("w")
        sleep(0.1)
        key_input.press("1")
        sleep(0.1)
        key_input.release("1")
        sleep(0.1)
        key_input.press("s")
        sleep(0.1)
        key_input.release("s")
        sleep(0.1)
        key_input.press("1")
        sleep(0.1)
        key_input.release("1")
        sleep(0.1)


def on_press():
    lift_right("s")
    # 向下收完之后
    key_input.press("s")
    sleep(0.3)
    key_input.release("s")
    sleep(0.1)
    # 向右
    up_down("d")
    for i in range(6):
        key_input.press("s")
        sleep(0.3)
        key_input.release("s")
        sleep(0.1)
    # 向左
    up_down("a")
    for i in range(6):
        key_input.press("s")
        sleep(0.3)
        key_input.release("s")
        sleep(0.1)
    # 向右
    up_down("d")
    for i in range(12):
        key_input.press("w")
        sleep(0.3)
        key_input.release("w")
        sleep(0.1)
    # 向上收
    lift_right("w")
    # 向上收完之后
    key_input.press("w")
    sleep(0.3)
    key_input.release("w")
    sleep(0.1)
    key_input.press("d")
    sleep(0.3)
    key_input.release("d")
    sleep(0.1)
    key_input.press("w")
    sleep(0.3)
    key_input.release("w")
    sleep(0.1)
    key_input.press("w")
    sleep(0.3)
    key_input.release("w")
    sleep(0.1)
    key_input.press("a")
    sleep(0.3)
    key_input.release("a")
    sleep(0.1)


def on_release(key):
    print('{0} released'
          .format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def add_one():
    for i in range(500):
        key_input.press("w")
        sleep(0.05)
        key_input.release("w")
        sleep(0.05)
        key_input.press("1")
        sleep(0.05)
        key_input.release("1")
        sleep(0.05)
        key_input.press("1")
        sleep(0.05)
        key_input.release("1")
        sleep(0.05)


temp = 1
while temp:
    with keyboard.Events() as events:
        for event in events:
            if event.key == keyboard.KeyCode.from_char('-'):
                print("hh")
                on_press()
                break
            if event.key == keyboard.KeyCode.from_char('+'):
                print("hh")
                add_one()
                break
            if event.key == keyboard.KeyCode.from_char('='):
                print("结束")
                temp = 0
                on_press()
                break
            else:
                print('Received event {}'.format(event))
