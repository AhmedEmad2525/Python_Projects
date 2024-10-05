import os
from character import Hero, Enemy
from weapon import wooden_bow, iron_sword

hero = Hero(name='Hero', health=100)
hero.equip(iron_sword)
enemy = Enemy(name='Enemy', health=100, weapon=wooden_bow)

print('press the action button(Enter) to show each fight ')
# initiating the play loop
while hero.health != 0 and enemy.health != 0:
    # clear screen before each run
    os.system("cls")

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()


