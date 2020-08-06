from joseph.adapter.reader import load_data

data_list = load_data()


class Individual(object):  # 一个人作为一个对象，包含多项信息
    def __init__(self, name: str, sex: str, age: str):
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