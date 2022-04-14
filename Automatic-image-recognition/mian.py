import configparser

import config
import operation_xlsx

from arithmetic import Arithmetic

if __name__ == "__main__":
    print("版本：" + config.version)
    path = operation_xlsx.path_name()
    print("当前路径:")
    print(path)
    files = operation_xlsx.file_name(path)
    print("程序将对如下文件进行匹配:")
    print(files)

    #  实例化configParser对象
    config = configparser.ConfigParser()
    # -read读取ini文件
    config.read('config.ini', encoding='UTF-8')

    # -get(section,option)得到section中option的值，返回为string类型
    date = config.get('login', 'date')
    config.date = date
    ari = Arithmetic()
    dates = ari.get_day_of_the_week(config.date)

    print("将匹配以下日期:")
    print(dates)

    for file in files:
        print("现在将对：" + file + "进行匹配")
        ws = operation_xlsx.read(path + "/" + file)
        ari.identify_the_image(ws, path + "/" + file)
