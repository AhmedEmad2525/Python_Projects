

class Weapon:

    def __init__(self, name: str, weapon_type: str, damage: int, value: int) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value


# defining a set of weapons
iron_sword = Weapon(name='Iron sword', weapon_type='melee', damage=5, value=10)
wooden_bow = Weapon(name='Wooden bow', weapon_type='ranged', damage=3, value=8)
fists = Weapon(name='Fists', weapon_type='melee', damage=2, value=0)

