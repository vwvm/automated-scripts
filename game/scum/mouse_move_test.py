from time import sleep

from pynput import mouse


def mouse_move_test():
    print("鼠标将会移动一个正方形")
    mouse_controll = mouse.Controller()
    mouse_controll.position = (0, 0)
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
    if input("是否继续测试 y?") == "y":
        mouse_controll.position = (0, 0)
        mouse_move_test()
