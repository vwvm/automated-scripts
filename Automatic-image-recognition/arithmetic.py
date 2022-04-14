import datetime
import re
import time
import numpy as np
from PIL import Image
import easyocr.model.vgg_model
import operation_xlsx

import config

dates = [str, str, str, str, str, str, str]

reader = easyocr.Reader(['ch_sim'], model_storage_directory="./", download_enabled=False, gpu=False,
                        base_directory="./")


class Arithmetic(object):

    def __init__(self):
        """
        主要算法
        """
        print("启动成功")

    def get_day_of_the_week(self, date=config.date):
        """
        计算一个星期中的每一天，写入字符串
        :param date: 一个星期的一天
        """
        time_tuple = time.strptime(date, "%Y-%m-%d")
        # 获取输入星期几
        tm_wday = time_tuple.tm_wday
        today = datetime.date.fromtimestamp(time.mktime(time_tuple))
        today = today - datetime.timedelta(days=tm_wday + 1)
        for i in range(7):
            today = today + datetime.timedelta(days=1)
            dates[i] = today.strftime("%Y-%m-%d")
        config.dates = dates
        return dates

    def identify_the_image(self, ws, file):
        """
        计算表格中图片的文字
        :param file: 文件的绝对路径和名字
        :param ws: 闯入一个表格
        """
        for image in ws._images:
            # 获取图片位置
            site = image.anchor._from
            # 获取图片坐标行
            row = site.row + 1

            # 如果已经匹配则跳过
            if ws.cell(row=row, column=10).value == "匹配成功":
                print(ws.cell(row=row, column=3).value + " " + "已经匹配成功")
                continue
            # 转换可以识别的格式
            img = Image.open(image.ref).convert("RGB")
            img = np.array(img)




            sign = False

            print(ws.cell(row=row, column=3).value)
            # 读取图像
            result = reader.readtext(img)
            # 结果
            sign = self.match_the_date(result=result, row=row, ws=ws, file=file)

            # 序列
            if sign is False:
                ws.cell(row=row, column=10, value="匹配失败：图片时间不对").fill = config.fills

            print()
            print()
            print()

        for i in range(1, ws.max_row):
            if ws.cell(row=i, column=6).value == "是":
                if ws.cell(row=i, column=10).value is None:
                    ws.cell(row=i, column=10, value="匹配失败：,没有图片").fill = config.fills

        operation_xlsx.save(file)

    def match_the_date(self, result, row, ws, file):
        """
        匹配日期
        :param file: 文件的绝对路径和名字
        :return: 匹配成功
        :param row: 图片所在行
        :param ws: 当前表格
        :param result: 识别的字符串数据
        """

        name_matching = False
        date_matching = False
        negative_matching = False
        date = ""
        name = ""
        accuracy_rate = 1.0
        negative = ""
        for i in result:

            # 匹配名字
            username = ws.cell(row=row, column=config.name_column).value
            str_mat = r"[" + username + "]"
            mat = re.search(str_mat, i[1])
            if mat is not None:
                name = mat.group()
                name_matching = True

            # 匹配阴性
            mat = re.search(r"[阴性]", i[1])
            if mat is not None:
                negative = mat.group()
                negative_matching = True

            # 匹配日期
            mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", i[1])
            if mat is not None:
                if mat.group() in config.dates:
                    date = mat.group()
                    accuracy_rate = i[2]
                    date_matching = True

        if name_matching and negative_matching and date_matching:
            print(name + " " + date + " " + negative + " 匹配成功")
            ws.cell(row=row, column=10).value = "匹配成功"
            ws.cell(row=row, column=11).value = date
            print("准确率" + str(accuracy_rate))
            ws.cell(row=row, column=12).value = "准确率" + str(accuracy_rate)
            operation_xlsx.save(file)
            return True
        return False




if __name__ == '__main__':
    a = Arithmetic()
    a.get_day_of_the_week()
    print(config.dates)
