from joseph.domain.joseph_rule import Joseph
from joseph.use_case.create_gamelist import Individual
from joseph.use_case.create_gamelist import create_gamelist


def start_game(start_num: int, step: int) -> object:
    gamelist = create_gamelist()
    test = Joseph(start_num, step, gamelist)

    myit = iter(test)
    for result in myit:
        pass
    return result