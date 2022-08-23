# coding:utf-8

from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import configparser

# driverUrl = 'msedgedriver.exe'
options = EdgeOptions()
# 使用谷歌内核
options.use_chromium = True
# 设置无界面模式
options.add_argument('headless')


def DetermineTheLogin():
    driver = webdriver.Edge(options=options)
    driver.get('http://59.77.64.130')
    try:
        userMessage = driver.find_element(By.ID, "userMessage")
    except:
        return True
    else:
        print(userMessage.text)


def login(userName, password, operator):
    driver = webdriver.Edge(options=options)

    driver.get('http://59.77.64.130')

    connectNetworkPageId = driver.find_element(By.ID, "connectNetworkPageId")

    # 查找用户名输入位置
    getUserText = connectNetworkPageId.find_element(By.NAME, "username")
    getUserText.send_keys(userName)
    getUserText.send_keys(Keys.TAB, password)

    connectNetworkPageId.find_element(By.ID, "xiala").click()
    # 0123分别表示教职工，移动，电信，联通

    if operator == "中国电信":
        operator = "bch_service_2"
    elif operator == "中国移动":
        operator = "bch_service_1"
    elif operator == "中国联通":
        operator = "bch_service_3"
    elif operator == "教职工":
        operator = "bch_service_0"

    driver.find_element(By.ID, operator).click()

    connectNetworkPageId.find_element(By.ID, "login_btn_1").click()

    driver.quit()


def remote_address(address=""):
    os.system("mstsc /f /v %s /" % address)


if __name__ == '__main__':

    #  实例化configParser对象
    config = configparser.ConfigParser()
    # -read读取ini文件
    config.read('config.ini', encoding='UTF-8')

    # -get(section,option)得到section中option的值，返回为string类型
    userName = config.get('login', 'userName')
    password = config.get('login', 'password')
    operator = config.get('login', 'operator')
    address = config.get('login', 'remoteAddress')
    if DetermineTheLogin():
        login(userName, password, operator)
        DetermineTheLogin()

    remote_address(address)
    print("20s后结束")
    sleep(20)
