import random


def create_score(stu_num, max_score=100):  # 定义一个函数用于创建成绩表
    score_list = [
        random.randint(0, max_score) for i in range(stu_num)
    ]  # 0 到 100 之间，随机得到 40 个整数，组成列表
    return score_list


def filter_under_average(score_list):  # 创建一个函数用于 筛选出低于平均分的人数和分数
    num = len(score_list)  # 分数的个数，即人数
    sum_score = sum(score_list)  # 对列表中的整数求和
    average_num = sum_score / num  # 计算平均数
    under_average = len(
        [i for i in score_list if i < average_num]
    )  # 将小于平均数的找出来，组成新的列表，并度量该列表的长度
    print("the average score_list is:%.1f" % average_num)
    print("There are %d students less than average." % under_average)


score_list = create_score(40)
filter_under_average(score_list)
sorted_score = sorted(score_list, reverse=True)  # 对原列表排序
print(sorted_score)

