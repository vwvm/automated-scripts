from time import sleep

from pynput import mouse, keyboard
from pynput.keyboard import Controller, Key

key_input = Controller()


def on_press():
    for i in range(21):
        key_input.press("s")
        sleep(0.3)
        key_input.release("s")
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
    # 向下收完之后
    key_input.press("s")
    sleep(0.3)
    key_input.release("s")
    sleep(0.1)
    for i in range(21):
        key_input.press("d")
        sleep(0.3)
        key_input.release("d")
        sleep(0.1)
    # 右到头
    for i in range(21):
        key_input.press("w")
        sleep(0.3)
        key_input.release("w")
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
    # 开始加油
    for i in range(30):
        key_input.press("d")
        sleep(0.3)
        key_input.release("d")
        sleep(0.1)
        key_input.press("w")
        sleep(0.1)
        key_input.release("w")
        sleep(0.1)
        key_input.press("1")
        sleep(0.1)
        key_input.release("1")
        sleep(0.1)
        key_input.press("1")
        sleep(0.1)
        key_input.release("1")
        sleep(0.1)
    # 加完油之后
    key_input.press("d")
    sleep(0.3)
    key_input.release("d")
    sleep(0.1)
    for i in range(3):
        key_input.press("w")
        sleep(0.3)
        key_input.release("w")
        sleep(0.1)
    # 开始收矿
    for i in range(30):
        key_input.press("a")
        sleep(0.3)
        key_input.release("a")
        sleep(0.1)
        key_input.press("s")
        sleep(0.1)
        key_input.release("s")
        sleep(0.1)
        key_input.press("1")
        sleep(0.1)
        key_input.release("1")
        sleep(0.1)


def on_release(key):
    print('{0} released'
          .format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


temp = 1
while temp:
    with keyboard.Events() as events:
        for event in events:
            if event.key == keyboard.KeyCode.from_char('-'):
                print("hh")
                on_press()
            if event.key == keyboard.KeyCode.from_char('='):
                print("结束")
                temp = 0
                on_press()
            else:
                print('Received event {}'.format(event))
