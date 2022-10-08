import configparser
import os
import random
from time import sleep

from pynput import mouse
from pynput.mouse import Button


def script_entrance_start_and_stop():
    mouse_controll = mouse.Controller()
    #  实例化configParser对象
    config = configparser.ConfigParser()
    # -read读取ini文件
    config.read('config.ini', encoding='UTF-8')
    config_dict = config.get('path_config', "SCUMPath")
    config_time_min = int(config.get('path_config', "timeMin"))
    config_time_max = int(config.get('path_config', "timeMax"))
    config_x = int(config.get('path_config', "x"))
    config_y = int(config.get('path_config', "y"))
    config_path = '"' + config_dict + '"'
    config_start_time = int(config.get('path_config', "appStartTime"))
    # 启动
    while True:
        os.system(config_path)
        sleep(config_start_time)
        mouse_controll.position = (config_x, config_y)
        mouse_controll.click(Button.left, 2)
        sleep(random.randint(config_time_min, config_time_max))
        # 关闭
        os.system("taskkill /F /IM SCUM.exe")
        sleep(1)
