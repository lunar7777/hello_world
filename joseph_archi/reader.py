import os
from tkinter import filedialog
import csv  # 系统自带

import zipfile  # 第三方


class Reader(object):
    def __init__(self, path: str):
        self.f = open(path, "r", encoding="UTF-8-sig")

    def __iter__(self):
        return self

    def __next__(self):
        line = 0
        if line != None:
            return self.read()
        else:
            StopIteration

    def read(self):
        line = self.f.readline()
        return line

    def __del__(self):
        pass


def load_data():
    """使用窗口弹出功能时，GUI无法使用 """
    #file_path = filedialog.askopenfilename()  # 弹出窗口以选择文件
    #file_type = os.path.splitext(file_path)[1]  # 返回文件的格式 如 .txt

    file_path = 'E:\\github_download\\workspace22\\melody33\\joseph_archi\\cast.txt'
    file_type = '.txt'
    
    if file_type == ".zip":
        zip_file = zipfile.ZipFile(file_path, "r")
        path = zip_file.extract(
            "cast_zip.txt",
            "E:\\github_download\\workspace22\\melody33\\joseph_archi",
        )
        temp = Reader(path)
    else:
        file_type == ".txt" or file_type == ".csv"
        temp = Reader(file_path)

    myiter = iter(temp)
    people_data = []
    for index in range(8):  # 9为参加游戏的人数
        element = next(myiter).strip("\n")
        people_data.append(element.split(","))
    # return people_data
    return people_data
    del temp


if __name__ == "__main__":
    data1_list = load_data()
    print(data1_list)
# print(people_data)
