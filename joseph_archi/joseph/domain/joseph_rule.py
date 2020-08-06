class Joseph(object):  # 创建一个约瑟夫类，包含迭代功能、约瑟夫出站规则
    def __init__(self, start_num: int, step: int, gamelist: list):
        self._person = gamelist
        self.start_num = start_num
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._person) > 0 and self.step!=0:
            self._key = (self.start_num + self.step - 1) % len(
                self._person
            )  # self._key 约瑟夫出队列规则， 私有变量，仅在内部使用
            self.start_num = self._key

            return self._person.pop(self._key)  # 排出本轮被淘汰的人
        else:
            raise StopIteration

