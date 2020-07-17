class People(object):  # 创建一个People类，用来定义约瑟夫环内每个人的信息
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


if __name__ == "__main__":
    test = People("xiaoa", "neutral", 10)
    assert test.__name == "xiaoa"  # 测试私有变量
    assert test.get_name() == "xiaoa"

