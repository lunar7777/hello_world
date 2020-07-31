from reader import load_data
import unittest
data_list = load_data()


class Individual(object):  # 一个人作为一个对象，包含多项信息
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age

    def get_name(self):
        return self.__name

    def get_sex(self):
        return self.__sex

    def get_age(self):
        return self.__age

    def __str__(self):  # 返回一个对象的描述信息
        return "name:%s, sex:%s, age:%s" % (self.__name, self.__sex, self.__age)


def create_gamelist():
    gamelist = []
    people_info = []
    for i in range(len(data_list)):  # 参与游戏的总人数，此处为文本内所有人员
        people_info.append(data_list[i][0].split(" "))

        obj_person = Individual(people_info[i][0], people_info[i][1], people_info[i][2])
        gamelist.append(obj_person)
    return gamelist

class TestPeopleInfo(unittest.TestCase):
    """用于测试每个人员的信息是否正确"""
    def setUp(self):
        """创建一个游戏人员列表，后续姓名性别年龄的测试都会用到"""
        self.gamelist = create_gamelist()

    def test_people_name(self):
        test_name = self.gamelist[0].get_name()
        self.assertEqual(test_name,'a')   #第一个人的名字叫 a

    def test_people_sex(self):
        test_sex = self.gamelist[0].get_sex()
        self.assertEqual(test_sex, 'male') #第一个人的性别为male

    def test_people_age(self):
        test_age = self.gamelist[0].get_age()
        self.assertEqual(test_age, '1') #第一个人的年龄为1

    def test_gamelist_length(self):
        test_len = len(self.gamelist)
        self.assertEqual(test_len,8)

if __name__ == "__main__":
    unittest.main()
