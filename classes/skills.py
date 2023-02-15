from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from classes.heroes import Hero


import random

class Skill:
    influence_str: str = ""


    def __init__(self, source) -> None:
        self.source: Hero = source
        self.dmg_multiplier = 1
        self.solo_hit_damage = None

    def influence(self, hero: Hero):
        print(f"{hero.name} {self.influence_str}")
    
    def check_dead(self, target):
        if target.current_hp <= 0:
            target.current_hp = 0
            print(f"{target.name} погиб")

    def solo_hit(self, value, target: Hero):
        if self.source.current_crit_rate >= random.random():
            self.solo_hit_damage = self.dmg_multiplier * value * (1 + self.source.current_crit_damage) * target.current_deffense/(600 + target.current_deffense) * random.uniform(0.95, 1.05)
        else:
            self.solo_hit_damage = self.dmg_multiplier * value * 1 * target.current_deffense/(600 + target.current_deffense) * random.uniform(0.95, 1.05)
         

class give_a_fuck(Skill):
    
    def __init__(self, source) -> None:
        self.dmg_multiplier = 1.75*2


        super().__init__(source)
        self.influence_str = "получил крепкую пиздятину от Тайрела"
    
    def influence(self, target: Hero):
        """accept_skill"""
        if target.current_hp <= 0:
            target.status = "Dead"
            print(f"{target.name} is {target.status}, он не {self.influence_str}")
            return 
        super().influence(target)
        super().solo_hit(self.source.current_deffense, target)
        target.current_hp -= self.solo_hit_damage
        super().check_dead(target)

    

class give_a_poison_fuck(Skill):
    
    def __init__(self, source) -> None:
        self.dmg_multiplier = 3.5


        super().__init__(source)
        self.influence_str = "ядовито оподливился от Каэля"
    
    def influence(self, target: Hero):
        """accept_skill"""
        if target.current_hp <= 0:
           target.status = "Dead"
           print(f"{target.name} is {target.status}, он не {self.influence_str}")
           return 
        super().influence(target)
        super().solo_hit(self.source.current_attack, target)
        target.current_hp -= self.solo_hit_damage
        super().check_dead(target)
