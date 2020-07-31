from joseph_rule import Joseph
from create_gamelist import create_gamelist
import unittest

# start_num = int(input("please input strat number:"))
# step = int(input("please input step:"))
def start_game(start_num, step):
    gamelist = create_gamelist()
    test = Joseph(start_num, step, gamelist)
    myit = iter(test)
    for result in myit:
        pass
    return result

class Test_final_result(unittest.TestCase):
    """用于测试导入实际人员信息后，按约瑟夫环规则进行的最终结果"""
    def test_result(self):
        result = start_game(2, 3)
        self.assertEqual(result.__str__(), 'name:a, sex:male, age:1') 
        
if __name__ == "__main__":   
    #print(start_game(2,3))
    # start_game(2,3)
    unittest.main()