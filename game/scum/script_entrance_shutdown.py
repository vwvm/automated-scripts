import os
import configparser
import time


def script_entrance_shutdown(is_down=1, shutdown_later=0):
    print("1秒后启动关机任务")
    time.sleep(1)
    gmtime = time.gmtime()
    #  实例化configParser对象
    config = configparser.ConfigParser()
    # -read读取ini文件
    config.read('config.ini', encoding='UTF-8')
    shutdown_later = int(config.get('shutdown_config', "shutdown_later"))
    is_down = int(config.get('shutdown_config', "is_down"))
    shutdown_at = config.get('shutdown_config', "shutdown_at")
    # 1 表示多少秒后关机，2表示指定时间关机
    shutdown_type = config.get('shutdown_config', "shutdown_type")
    print(shutdown_type)
    tm_hour = gmtime.tm_hour + 8
    tm_min = gmtime.tm_min
    if is_down:
        os.system("shutdown /a")
    if shutdown_type == '1':
        if shutdown_later:
            os.system("shutdown /s /t " + str(shutdown_later))
    if shutdown_type == '2':
        at_list = shutdown_at.split("-")
        if int(at_list[0]) >= tm_hour and int(at_list[1]) >= tm_min:
            ti = (int(at_list[0]) - tm_hour) * 3600 + (int(at_list[1]) - tm_min) * 60
            os.system("shutdown /s /t " + str(ti))
        else:
            ti = (int(at_list[0]) + 24 - tm_hour) * 3600 + (int(at_list[1]) - tm_min) * 60
            os.system("shutdown /s /t " + str(ti))