import math


def quadratic_equation(a, b, c):  # a为二次项系数 b为一次性系数 c为常数
    delta = b * b - 4 * a * c
    if delta < 0:
        print("False")
    elif delta == 0:
        print("唯一根为：%.2f" % -(b / (2 * a)))
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2 * a)
        x2 = (-b - sqrt_delta) / (2 * a)
        print("根1：%.2f  根2：%.2f" % (x1, x2))


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
quadratic_equation(a, b, c)  # 调用函数

