from time import sleep

from pynput import mouse


def mouse_move_test():
    mouse_controll = mouse.Controller()
    for i in range(5):
        mouse_controll.move(10, 0)
        sleep(0.1)
    for i in range(5):
        mouse_controll.move(0, 10)
        sleep(0.1)
    for i in range(5):
        mouse_controll.move(-10, 0)
        sleep(0.1)
    for i in range(5):
        mouse_controll.move(0, -10)
        sleep(0.1)