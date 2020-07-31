import unittest


class Joseph(object):  # 创建一个约瑟夫类，包含迭代功能、约瑟夫出站规则
    def __init__(self, start_num, step, gamelist):
        self._person = gamelist
        self.start_num = start_num
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._person)>0 and self.step!=0:
            self._key = (self.start_num + self.step - 1) % len(
                self._person
            )  # self._key 约瑟夫出队列规则， 私有变量，仅在内部使用
            self.start_num = self._key

            return self._person.pop(self._key)  # 排出本轮被淘汰的人
        else:
            raise StopIteration


class TestJoseph(unittest.TestCase):
    def test_final_num(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8]
        test = Joseph(2, 3, test_list)
        myit = iter(test)
        for x in myit:
            pass
        self.assertEqual(x, 1)

    def test_start_num(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8]
        start_num = -1   # 在此处修改start_num的值以测试
        test = Joseph(start_num, 3, test_list)
        myit = iter(test)
        for x in myit:
            pass
        self.assertTrue(x)

    def test_step(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8]
        step = 0     # 在此处修改step的值以测试
        test = Joseph(2, step, test_list)
        myit = iter(test)
        for x in myit:
            pass
        self.assertTrue(x)

if __name__ == "__main__":
    unittest.main()
    
