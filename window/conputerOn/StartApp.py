import configparser


class StartApp:
    import os
    command = ""

    def __init__(self, command):
        self.command = command
        pass


if __name__ == "__main__":
    #  实例化configParser对象
    config = configparser.ConfigParser()
    # -read读取ini文件
    config.read('config.ini', encoding='UTF-8')
