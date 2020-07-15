from josf_generate_cast import generate_cast

def joseph_ring(dead_num, start_pos=0):  # 创建一个函数用于解决约瑟夫环问题(使用列表),dead_num 为报数的数字
    num_list = generate_cast()  # 生成一个人数列表
    index = 0
    while len(num_list) >= 1:
        temp = num_list.pop(start_pos % len(num_list))  # 把列表中首元素提取出来
        index += 1  # 进行报数
        if index == dead_num:                
            index = 0
            continue  # 如果 == dead_num,就会执行到continue. continue跳出本次循环，break跳出整个循环
        num_list.append(temp)
        if len(num_list) == 1:
            return num_list[0].get_info()
