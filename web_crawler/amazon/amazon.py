# coding:utf-8
import base64
import time

import cv2
from time import sleep

import numpy as np
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import configparser

# driverUrl = 'msedgedriver.exe'
options = EdgeOptions()
# 使用谷歌内核
options.use_chromium = True


# 设置无界面模式
# options.add_argument('headless')
def show(name):
    '''展示圈出来的位置'''
    cv2.imshow('Show', name)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def _tran_canny(image):
    """消除噪声"""
    image = cv2.GaussianBlur(image, (3, 3), 0)
    return cv2.Canny(image, 50, 150)

def detect_displacement(img_slider_path, image_background_path):
    """detect displacement"""
    # # 参数0是灰度模式
    image = cv2.imread(img_slider_path, 0)
    template = cv2.imread(image_background_path, 0)

    # 寻找最佳匹配
    res = cv2.matchTemplate(_tran_canny(image), _tran_canny(template), cv2.TM_CCOEFF_NORMED)
    # 最小值，最大值，并得到最小值, 最大值的索引
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = max_loc[0]  # 横坐标
    # 展示圈出来的区域
    x, y = max_loc  # 获取x,y位置坐标

    w, h = image.shape[::-1]  # 宽高
    cv2.rectangle(template, (x, y), (x + w, y + h), (7, 249, 151), 2)
    show(template)
    return top_left



def findPic(bg_img, sg_img):
    """
    找出图像中最佳匹配位置
    :param img_bg_path: 滑块背景图本地路径
    :param img_slider_path: 滑块图片本地路径
    :return: 返回最差匹配、最佳匹配对应的x坐标
    """


    bg_img = base64.b64decode(bg_img.split(",")[-1])
    with open('./images/base64.jpg', 'wb') as file:
        file.write(bg_img)
    sg_img = base64.b64decode(sg_img.split(",")[-1])
    with open('./images/sp.jpg', 'wb') as file:
        file.write(sg_img)



    bg_img = np.frombuffer(bg_img, np.uint8)

    # img_raw = cv2.imdecode(img_array, cv2.IMREAD_COLOR)  # 转换Opencv格式BGR
    # img_gray = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)  # 转换灰度图

    bg_img = cv2.imdecode(bg_img, cv2.IMREAD_GRAYSCALE)

    # bg_img = cv2.imread(bg_img, 0)
    print(bg_img)
    sg_img = np.frombuffer(sg_img, np.uint8)
    sg_img = cv2.imdecode(sg_img, cv2.IMREAD_GRAYSCALE)
    # sg_img = cv2.imread(sg_img, 0)

    image = cv2.imread('./images/base64.jpg', 0)
    template = cv2.imread('./images/sp.jpg', 0)

    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc[0]
    top_left = int(top_left * 278 / 365)

    # top_left = detect_displacement("./images/base64.jpg", "background.png")
    print(top_left)

    return top_left


def DetermineTheLogin():
    driver = webdriver.Edge(options=options)
    driver.get('https://www.jd.com/')
    try:
        userMessage = driver.find_element(By.ID, "userMessage")
    except:
        return True
    else:
        print(userMessage.text)


def login(userName, password, operator):
    driver = webdriver.Edge(options=options)

    driver.get('https://www.amazon.com/')

    sleep(5000)
    if (True):
        return

    connectNetworkPageId = driver.find_element(By.ID, "ttbar-login")

    connectNetworkPageId.click()
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, "div.login-tab.login-tab-r").click()
    # 查找用户名输入位置

    loginIn = driver.find_element(By.ID, "loginname")
    loginIn.send_keys(userName)
    loginIn.send_keys(Keys.TAB, password)

    driver.find_element(By.CSS_SELECTOR, "div.login-btn").click()

    imgBackground = driver.find_element(By.CSS_SELECTOR, "div.JDJRV-bigimg")
    print(imgBackground.tag_name)
    while (True):
        big_img = imgBackground.find_element(By.XPATH, "//div[@class='JDJRV-bigimg']/img").get_attribute('src')
        small_img = imgBackground.find_element(By.XPATH, "//div[@class='JDJRV-smallimg']/img").get_attribute('src')
        # content = requests.get(big_img).content
        top_left = findPic(big_img, small_img) + 2
        print(top_left)
        # content = requests.get(big_img).content  # 下载背景
        # f = open('bj.jpg', mode='wb')
        # f.write(content)
        # f.close()
        # print('下载完成背景图片')
        # time.sleep(1)
        # content1 = requests.get(small_img).content  # 下载滑块
        # f = open('hk.jpg', mode='wb')
        # f.write(content1)
        # f.close()
        # print('下载完成滑块图片')

        hk = driver.find_element(By.CSS_SELECTOR, "div.JDJRV-slide-inner.JDJRV-slide-btn")
        ActionChains(driver).move_to_element(hk).perform()
        ActionChains(driver).click_and_hold(hk).perform()

        while top_left > 5:
            ActionChains(driver).move_by_offset(5, 0).perform()
            time.sleep(10 / 1000)
            top_left -= 5
        ActionChains(driver).release().perform()

    sleep(50000)
    driver.quit()


if __name__ == '__main__':
    #  实例化configParser对象
    config = configparser.ConfigParser()
    # -read读取ini文件
    config.read('config.ini', encoding='UTF-8')

    # -get(section,option)得到section中option的值，返回为string类型
    userName = config.get('login', 'userName')
    password = config.get('login', 'password')
    operator = config.get('login', 'operator')

    login(userName, password, operator)

    print("20s后结束")
    sleep(20)
