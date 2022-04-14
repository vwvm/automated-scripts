# -*- coding: utf-8 -*-
import glob
import openpyxl
from openpyxl import Workbook
import config
import os

wb = Workbook
ws = wb.active


def path_name(file_dir=config.file_dir):
    path = file_dir
    if file_dir == "./" or None:
        path = os.getcwd()
    return path


def file_name(file_dir=config.file_dir):
    path = file_dir
    if file_dir == "./" or None:
        path = os.getcwd()

    # files = glob.glob(os.path.join(path, '*.xlsx'))
    # print(files[0])
    my_files = []
    files = os.listdir(path)
    for file in files:
        if file.split('.')[-1] in ['xlsx']:
            my_files.append(file)
    return my_files


# def file_name(file_dir=config.file_dir):
#     for root, dirs, files in os.walk(file_dir):
#         for file in files:
#             if os.path.splitext(file)[1] == '.xlsx':
#                 print(file)

def read(name):
    """
    读取传入的表格名字
    :param name: 传入的表格名字
    :return: 第一个表
    """
    global wb, ws
    wb = openpyxl.load_workbook(name)
    ws = wb[wb.sheetnames[0]]
    return ws


def save(name):
    """
    报错表格
    :param name:传入表格名字
    """
    wb.save(name)


if __name__ == "__main__":
    file_name()
