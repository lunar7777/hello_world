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
    #file_path =  filedialog.askopenfilename()
    file_path = 'E:\\github_download\\workspace22\\melody33\\joseph_archi_copy\\cast.txt'
    file_type = '.txt'
    
    if file_type == ".zip":
        zip_file = zipfile.ZipFile(file_path, "r")
        path = zip_file.extract(
            "cast_zip.txt",
            "E:\\github_download\\workspace22\\melody33\\joseph_archi_copy",
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