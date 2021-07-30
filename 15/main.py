"""
    练习15
"""


class Pokemon:
    def __init__(self, name):
        self.name = name


class Water_Pokemon(Pokemon):
    def __init__(self, name):
        super().__init__(name)

    def skill_water(self):
        print('水枪 ', end="")


class Grass_Pokemon(Pokemon):
    def __init__(self, name):
        super().__init__(name)

    def skill_grass(self):
        print('飞叶快刀 ', end="")


class Fire_Pokemon(Pokemon):
    def __init__(self, name):
        super().__init__(name)

    def skill_fire(self):
        print('喷火 ', end="")


class Special_Pokemon(Water_Pokemon, Grass_Pokemon, Fire_Pokemon):
    def __init__(self, name):
        super().__init__(name)


Guinness_turtle = Water_Pokemon('杰尼龟')
Bulbasaur = Grass_Pokemon('妙蛙种子')
Charmander = Fire_Pokemon('小火龙')
mutation = Special_Pokemon('百变怪')

print(Guinness_turtle.name, '技能：', end="")
Guinness_turtle.skill_water()
print('\n' + Bulbasaur.name, '技能：', end="")
Bulbasaur.skill_grass()
print('\n' + Charmander.name, '技能：', end="")
Charmander.skill_fire()
print('\n' + mutation.name, '技能：', end="")
mutation.skill_water()
mutation.skill_grass()
mutation.skill_fire()
