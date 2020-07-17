# Reader用于产生人员信息(二维数组)， 在People类引用Reader的信息生成对象 ，People生成的对象引入到Joseph的person[]
from joseph import Joseph
from people import People
from reader import Reader

if __name__ == "__main__":
    temp = Reader()
    cast_list_ret = temp.read_zip()  # 从txt读取信息

    people_list = []

    for i in range(len(cast_list_ret)):
        people_list.append(
            People(cast_list_ret[i][0], cast_list_ret[i][1], cast_list_ret[i][2])
        )  # 把第一个人作为people类的一个对象

    test_jos = Joseph(3, 4, people_list)
    myiter = iter(test_jos)
    for i in myiter:
        print(i)

