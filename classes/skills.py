from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from classes.heroes import Hero

class Skill:
    influence_str: str = ""

    def __init__(self, source) -> None:
        self.source: Hero = source

    def influence(self, hero: Hero):
        print(f"{hero.name} {self.influence_str}")
    
    def check_dead(self, target):
        if target.current_hp <= 0:
            target.current_hp = 0
            print(f"{target.name} погиб")

class give_a_fuck(Skill):
    
    def __init__(self, source) -> None:
        self.dmg_multiplier = 1.75*2


        super().__init__(source)
        self.influence_str = "получил крепкую пиздятину от Тайрела"
    
    def influence(self, target: Hero):
        """accept_skill"""
        super().influence(target)
        target.current_hp -= self.dmg_multiplier * self.source.current_deffense
        super().check_dead(target)

    

class give_a_poison_fuck(Skill):
    
    def __init__(self, source) -> None:
        self.dmg_multiplier = 3.5


        super().__init__(source)
        self.influence_str = "ядовито оподливился от Каэля"
    
    def influence(self, target: Hero):
        """accept_skill"""
        super().influence(target)
        target.current_hp -= self.dmg_multiplier * self.source.current_attack
        super().check_dead(target)
