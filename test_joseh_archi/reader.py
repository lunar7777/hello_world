import os
import csv  # 系统自带
import unittest # 写测试
from tkinter import filedialog # 写GUI
import zipfile  # 压缩文件 （第三方库）


class Reader(object):
    def __init__(self, path):
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
    #file_path = filedialog.askopenfilename()  # 弹出窗口以选择文件
    #file_type = os.path.splitext(file_path)[1]  # 返回文件的格式 如 .txt

    file_path = 'E:\\github_download\\workspace22\\melody33\\joseph_archi\\cast.txt'
    file_type = '.txt'
    
    if file_type == ".zip":
        zip_file = zipfile.ZipFile(file_path, "r")
        path = zip_file.extract(
            "cast_zip.txt",
            "E:\\github_download\\workspace22\\melody33\\joseph_archi.py",
        )
        obj_temp = Reader(path)
    else:
        file_type == ".txt" or file_type == ".csv"
        obj_temp = Reader(file_path)
    
    myiter = iter(obj_temp)
    people_data = []
    for index in range(8):  # 8为参加游戏的人数
        element = next(myiter).strip("\n")
        people_data.append(element.split(","))
    # return people_data
    #return people_data # 该return用于测试后续调用本函数的其他模块
    return people_data, file_type  #该return 用于测试本模块
    del obj_temp

class TestReader(unittest.TestCase):

    def test_load_txtdata(self):
        people_data, file_type = load_data()
        self.assertEqual(file_type,'.txt')

    def test_len_load_data(self):
        people_data, file_type = load_data()
        self.assertEqual(len(people_data),8)

if __name__ == "__main__":
    #data1_list = load_data()
    #print(data1_list)
    #load_data()
    unittest.main()
