import csv  # 系统自带

import zipfile  # 第三方

import people  # 项目内其他文件


class Readertxt(object):  # 创建一个Reader类，包含txt,csv和zip格式文件的读取，并返回所有人员的数据
    def __init__(self,path='cast.txt'):
        self.f = open(path,'r',encoding='UTF-8-sig')
        
    def __iter__(self):
        return self

    def __next__(self):
        line = 0
        if line != None :
            return self.read()
        else:
            StopIteration

    def read(self):  # 
            line = self.f.readline()
            return line

    def __del__(self):
        pass

class Readercsv(object):  # 创建一个Reader类，包含txt,csv和zip格式文件的读取，并返回所有人员的数据
    def __init__(self,path='cast.csv'):
        self.f = open(path,'r',encoding='UTF-8-sig')
        
    def __iter__(self):
        return self

    def __next__(self):
        line = 0
        if line != None :
            return self.read()
        else:
            StopIteration

    def read(self):  # 
            line = self.f.readline()
            return line

    def __del__(self):
        pass

class Readerzip(object):  # 创建一个Reader类，包含txt,csv和zip格式文件的读取，并返回所有人员的数据
    def __init__(self,path='cast.zip/cast_zip.txt'):
        self.f = open(path,'r',encoding='UTF-8-sig')
        
    def __iter__(self):
        return self

    def __next__(self):
        line = 0
        if line != None :
            return self.read()
        else:
            StopIteration

    def read(self):  # 
            line = self.f.readline()
            return line

    def __del__(self):
        pass


if __name__ == "__main__":
    a = Readertxt()
    b = iter(a)
    print(next(b))

    """
    func = test.read_txt
    func(path="cast.txt")
    func = test.read_csv
    func(path="cast.csv")
    print(func)"""
    # print(test.read_txt())
    # print(test.read_txt())
    # assert len(test.read_txt()) == 10

