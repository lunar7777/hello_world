class Joseph(object):  # 创建一个约瑟夫类，包含迭代功能、约瑟夫出站规则
    def __init__(self, start_num, step, people_list):
        self._person = people_list
        self.start_num = start_num
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._person) > 0:
            self._key = (self.start_num + self.step - 1) % len(
                self._person
            )  # self._key 约瑟夫出队列规则， 私有变量，仅在内部使用
            self.start_num = self._key

            return self._person.pop(self._key)  # 排出本轮被淘汰的人
        else:
            raise StopIteration

    def add_people(self, Joseph):
        self._person.append(Joseph)


if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6, 7, 8]
    test = Joseph(3, 4, test_list)
    myit = iter(test)
    for x in myit:
        print(x)
    assert x == 1  # 测试最终出局号码

