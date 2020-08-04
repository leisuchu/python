class SuperMan:
    """
    类继承测试
    """

    def __init__(self, name):
        self.name = name
        self.gender = 1
        self.age = 20

    def fight_start(self):
        return "wu mai mo shi de ru!"

    def fight_end(self):
        return "na ni !"


superMan = SuperMan('leisuchu')
superMan.gender = 2
superMan.age = 18
print(superMan.fight_start())
print(superMan.fight_end())

