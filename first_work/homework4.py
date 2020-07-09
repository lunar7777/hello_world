a, b = 0, 1  # 斐波那契数列

for i in range(7):  # 改变range()里的数，就能得到相应项的结果
    a, b = b, a + b  # a = b ; b = a+b

print(a)

