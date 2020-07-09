import math


def is_prime(num):  # 创建一个函数用于判断是否为素数
    kai_gen = math.sqrt(num)
    if num <= 1:
        return False
    for i in range(2, int(kai_gen + 1)):  # 向上取整
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    test_num = int(input("请输入一个整数："))
    primes = [i for i in range(2, test_num + 1) if is_prime(i)]  # 从 2 开始，因为 1 显然不是质数
    print("%d 以内的素数有：" % (test_num))
    print(primes)
