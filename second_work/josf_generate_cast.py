def generate_cast(): #该模块用于生成约瑟夫环的对象
    with open(
        "E:\\github_download\\workspace22\\melody33\\second_work\\cast.txt",
        "r",
        encoding="UTF-8-sig",
    ) as f:  # 读取人员
        cast_lst = list(f)  # 名单由txt转为列表

    num_lst = list()  # 空列表 用于 存放对象
    class Cast:
        def __init__(self, name, sex, age):
            self.__name = name
            self.__sex = sex
            self.__age = age

        def get_info(self):
            print( self.__name,self.__sex,self.__age)

    for i in range(0, len(cast_lst), 3):  # 使用类 创建姓名，性别和年龄
        cast_lst[i] = Cast(cast_lst[i], cast_lst[i + 1], cast_lst[i + 2])
        num_lst.append(cast_lst[i])
    return num_lst
    