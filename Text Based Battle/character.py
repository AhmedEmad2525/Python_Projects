from weapon import fists
from health_bar import HealthBar


class Character:
    race = "human"

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        # the initial weapon of the character will be the fists
        self.weapon = fists

    def attack(self, target) -> None:
        """
        this method allows the character to attack a chosen target
        """
        target.health -= self.weapon.damage
        # to avoid the target health to go below 0 hp
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f'{self.name} has dealt {self.weapon.damage} to {target.name} with {self.weapon.name}')


class Hero(Character):
    def __init__(self,
                 name: str,
                 health: int
                 ) -> None:
        super().__init__(name=name, health=health)
        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color='green')

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")

    def drop(self) -> None:
        print(f'{self.name} dropped the {self.weapon}! ')
        self.weapon = self.default_weapon


class Enemy(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 weapon
                 ) -> None:
        super().__init__(name=name, health=health)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color='red')



        
        

