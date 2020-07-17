class Reader(object):    #创建一个Reader类，包含txt,csv和zip格式文件的读取，并返回所有人员的数据
    def read_txt(self, path_t="cast.txt"):  #读取txt文件的数据，并返回一个列表
        self.path_txt = path_t
        with open(self.path_txt, "r", encoding="UTF-8-sig") as f_txt:  # 读取人员
            cast_lst_txt = list(f_txt)  # 名单由txt转为列表
        cast_list_txt = []  # 创建一个新列表，用于整理数据
        for i in range(len(cast_lst_txt)):
            cast_lst_txt[i] = cast_lst_txt[i].strip("\n")
            cast_list_txt.append(cast_lst_txt[i].split(" "))
        return cast_list_txt

    def read_csv(self, path_c="cast.csv"):  #读取csv文件的数据，返回一个列表
        self.path_csv = path_c
        import csv

        cast_lst_csv = []   
        csv_temp = open(self.path_csv, "r", encoding="UTF-8-sig")
        f_csv = csv.reader(csv_temp)  #csv自带reader函数 用于读取数据
        for i in f_csv:
            cast_lst_csv.append(i)   #将csv文件内的数据重新存入一个列表
        csv_temp.close()
        return cast_lst_csv

    def read_zip(self, path_z="cast.zip"): #该zip文件包含一个txt文件
        self.path_zip = path_z
        import zipfile

        zf = zipfile.ZipFile(self.path_zip, "r")
        get_path_zip_txt = zf.extract("cast_zip.txt")  # 解压zip文件，获取zip文件里txt文件的地址
        # zf.extractall()    #提取压缩包中所有文件
        with open(get_path_zip_txt, "r", encoding="UTF-8-sig") as f_txt:  # 读取人员
            cast_lst_txt = list(f_txt)  # 名单由txt转为列表
        cast_list_txt = []  # 创建一个新列表
        for i in range(len(cast_lst_txt)):
            cast_lst_txt[i] = cast_lst_txt[i].strip("\n")
            cast_list_txt.append(cast_lst_txt[i].split(" "))
        return cast_list_txt
if __name__ == "__main__":
    test = Reader()
    #print(test.read_txt())
    assert(len(test.read_txt()) == 10)