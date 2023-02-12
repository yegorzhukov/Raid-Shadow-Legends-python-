from __future__ import annotations

from classes.skills import *
from classes.characteristics import *

class Hero:
    """базовый класс всех героев"""

    def __init__(self, *args, **kwargs):

        """Базовые атрибуты"""
        self.__hp = kwargs["hp"]
        self.__attack = kwargs["attack"]
        self.__deffense = kwargs["deffense"]
        self.__crit_rate = kwargs["crit_rate"]
        self.__crit_damage = kwargs["crit_damage"]
        self.__resistance = kwargs["resistance"]
        self.__accuracy = kwargs["accuracy"]

        """Текущие показатели"""
        self.current_hp = kwargs["hp"]
        self.current_attack = kwargs["attack"]
        self.current_deffense = kwargs["deffense"]
        self.bonuces = []
        self.penalty = []
        self.aura_influence = None
        self.status = "Alive"

        """Способности"""
        self.skills: list[Skill] = []
        self.aura = None

    def use_skill(self, skill, target):
        target.accept_skill(skill)

    def accept_skill(self, skill: Skill):
        if self.current_hp <= 0:
            self.status = "Dead"
            print(f"{self.name} is {self.status}, он не {skill.influence_str}")
            return 
        skill.influence(self)
        self.info() # self не надо передавать внутри метода класса

    def info(self):
        print(f"{self.name} hp: {self.current_hp}/{self.__hp}")

class Tyrel(Hero):
    """Лучший герой в рейде (кроме упряжника (нет))"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skills = [give_a_fuck(self)]
        self.name = "Tyrel"

class Kael(Hero):
    """Лучший герой в рейде (кроме упряжника (нет))"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skills = [give_a_poison_fuck(self)]
        self.name = "Kael"


my_tyrel = Tyrel(**Tyrel_characteristics)

my_Kael = Kael(**kael_characteristics)




