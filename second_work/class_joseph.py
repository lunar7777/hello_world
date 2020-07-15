class Joseph(object):
    def __init__(self,name):
        self._name = name
        self._person = []

    def __repr__(self):
        return 'person:{}'.format(self._name)

    def add_child(self,Joseph):
        self._person.append(Joseph)

    def __iter__(self):
        return iter(self._person)


if __name__ == '__main__':
    root = Joseph(0)
    child1 = Joseph(1)
    child2 = Joseph(2)
    root.add_child(child1)
    root.add_child(child2)
    for i in root:
        print(i)