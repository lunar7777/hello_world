def jose_ring(total_num, key):  # 创建一个函数用于解决约瑟夫环问题(使用列表),total_num 为总人数,key 为报数的数字
    num_list = list(range(1, total_num + 1))  # 生成一个人数列表
    index = 0
    while list:
        temp = num_list.pop(0)  # 把列表中首元素提取出来
        index += 1  # 进行报数
        if index == key:
            index = 0
            continue  # 如果 == key,就会执行到continue. continue跳出本次循环，break跳出整个循环
        num_list.append(temp)
        if len(num_list) == key - 1:
            print("幸存号码为：", num_list[:])
            break


if __name__ == "__main__":
    total_num = int(input("请输入总人数："))
    key = int(input("请输入报数的数字："))
    jose_ring(total_num, key)

