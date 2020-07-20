import csv  # 系统自带

import zipfile  # 第三方

import people  # 项目内其他文件


class Reader(object):
    def __init__(self, path="cast.txt"):
        self.f = open(path, "r", encoding="UTF-8-sig")

    def __iter__(self):
        return self

    def __next__(self):
        line = 0
        if line != None:
            return self.read()
        else:
            StopIteration

    def read(self):  #
        line = self.f.readline()
        return line

    def __del__(self):
        pass


class Readertxt(Reader):  # 创建一个Reader类，包含txt,csv和zip格式文件的读取，并返回所有人员的数据
    def __init__(self, path="cast.csv"):
        self.f = open(path, "r", encoding="UTF-8-sig")


class Readercsv(Reader):  # 创建一个Reader类，包含txt,csv和zip格式文件的读取，并返回所有人员的数据
    def __init__(self, path="cast.csv"):
        self.f = open(path, "r", encoding="utf-8-sig")


    
class Readerzip(Reader):  # 创建一个Reader类，包含txt,csv和zip格式文件的读取，并返回所有人员的数据
    zip_file = zipfile.ZipFile('cast.zip','r')
    path_txt = zip_file.extract('cast_zip.txt')
    def __init__(self,path=path_txt):
        self.f = open(path,'r',encoding='utf-8-sig')

if __name__ == "__main__":

    a = Readercsv()
    b = iter(a)
    cast_list = []
    for index in range(9):
        element = next(b).strip("\n")
        cast_list.append(element.split(","))
    print(cast_list)
    del a

# print(cast_list)
