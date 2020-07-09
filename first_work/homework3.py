def clear_space(str1):  # 创建一个函数用于去除多余的空格
    str1 = "I love  code."  # 在 code 前面有两个空格，应该删除一个
    print(str1)  # 为了能够清楚看到每步的结果，把过程中的量打印出来

    str1_lst = str1.split(" ")  # 以空格为分割，得到词汇的列表
    print(str1_lst)

    words = [i for i in str1_lst if i != ""]  # 去除列表中的空格
    print(words)

    new_string = " ".join(words)  # 以空格为连接符，将单词链接起来
    print(new_string)


print("输入字符串：")
str_in = input()
clear_space(str_in)
