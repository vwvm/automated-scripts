from os import walk
import os


def save(line, buff_size=1000, clear_buff=False):
    f = open("aa.txt", mode="a+", encoding="utf-8")
    f.write("嘿嘿嘿嘿")
    f.flush()
    f.close()

if __name__ == "__main__":

    path = "F:\\project\\python\\automated-scripts\\文件浏览"
    for curDir, dirs, files in walk(path):
        # for curDir, dirs, files in walk(path,topdown=False):
        print("现在的目录：", curDir)
        print("该目录下包含的子目录：", str(dirs))
        print("该目录下包含的文件：", str(files))
        print("*" * 20)

    save(2, )
