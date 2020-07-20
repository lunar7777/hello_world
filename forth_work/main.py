# Reader用于产生人员信息(二维数组)， 在People类引用Reader的信息生成对象 ，People生成的对象引入到Joseph的person[]
from reader_cor import *
from joseph import Joseph
from people import People


if __name__ == "__main__":
    total_num= 9
    temp = Readercsv()
    myiter = iter(temp)
    cast_list = []
    for index in range(total_num):
        element = next(myiter).strip('\n')
        cast_list.append(element.split(','))
    print(cast_list)

    #cast_list_ret = temp.read()  # 从txt/csv/zip读取信息

    people_list = []

    for i in range(len(cast_list)):
        people_list.append(
            People(cast_list[i][0], cast_list[i][1], cast_list[i][2])
        )  # 把第一个人作为people类的一个对象

    START_NUM = 3
    STEP = 4
    test_jos = Joseph(START_NUM, STEP, people_list)
    myiter = iter(test_jos)
    for i in myiter:
        print(i)

