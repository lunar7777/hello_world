origin_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("原始列表为：", origin_lst[:])

x = origin_lst.pop(0)
origin_lst.append(x)

print("变换后列表为：", origin_lst[:])
