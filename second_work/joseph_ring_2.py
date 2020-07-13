def generate_cast():
    class Cast:
        def __init__(self, name, sex, age):
            self.name = name
            self.sex = sex
            self.age = age

    file = open(
        "E:\\github_download\\workspace22\\melody33\\second_work\\cast.txt",
        "r",
        encoding="UTF-8",
    )  # 读取人员
    cast_lst = list(file)  # 名单由txt转为列表
    num_lst = list()  # 空列表 用于 存放对象

    for i in range(0, len(cast_lst), 3):  # 使用类 创建姓名，性别和年龄
        cast_lst[i] = Cast(cast_lst[i], cast_lst[i + 1], cast_lst[i + 2])
        """
        print("name : %s" % cast_lst[i].name)
        print("sex : %s" % cast_lst[i].sex)
        print("age : %s" % cast_lst[i].age)
        """
        num_lst.append(cast_lst[i])
    return num_lst


def joseph_ring(dead_num):  # 创建一个函数用于解决约瑟夫环问题(使用列表),dead_num 为报数的数字
    num_list = generate_cast()  # 生成一个人数列表
    index = 0
    while num_list:
        temp = num_list.pop(0)  # 把列表中首元素提取出来
        index += 1  # 进行报数
        if index == dead_num:
            index = 0
            continue  # 如果 == dead_num,就会执行到continue. continue跳出本次循环，break跳出整个循环
        num_list.append(temp)
        if len(num_list) == dead_num - 1:  # 幸存者人数为死亡数字-1
            for j in range(dead_num):  # 将所有幸存者信息输出
                print(
                    "幸存者：\n",
                    num_list[j].name,
                    "性别：",
                    num_list[j].sex,
                    "年龄：",
                    num_list[j].age,
                )
                break


if __name__ == "__main__":
    dead_num = int(input("请输入死亡数字："))
    joseph_ring(dead_num)
