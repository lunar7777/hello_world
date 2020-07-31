from joseph_rule import Joseph
from create_gamelist import create_gamelist


def start_game(start_num: int, step: int) -> object:
    gamelist = create_gamelist()
    test = Joseph(start_num, step, gamelist)

    myit = iter(test)
    for result in myit:
        pass
    return result

if __name__ == "__main__": 
    start_num = int(input("please input strat number:"))
    step = int(input("please input step:"))  
    print(start_game(start_num,step))
    # start_game(2,3)