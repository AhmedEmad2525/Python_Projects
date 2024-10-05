# Text Based Battle

This project is a text-based battle simulation between a hero and an enemy, where players can see the health bars of both characters and watch the outcome of each attack in real-time. It demonstrates various programming concepts in Python, including object-oriented programming, custom classes, and the use of color for visual enhancements in the console.

## Features

- **Weapons Class**: Define weapons with specific properties like type, damage, and value.
- **Health Bar Class**: A customizable health bar for visualizing character health during battles.
- **Character Classes**: Define a `Character` base class and specialized classes for `Hero` and `Enemy`, each capable of attacking and managing weapons.
- **Interactive Main Battle**: Run a simple battle simulation between a hero and an enemy, where each takes turns attacking.

## Project Structure

### 1. Weapon
The `Weapon` class allows you to create weapons with different properties such as:
- `name` (e.g., Iron Sword)
- `weapon_type` (e.g., melee, ranged)
- `damage` (amount of damage dealt)
- `value` (the value of the weapon)

**Example weapons**:
```python
iron_sword = Weapon(name='Iron sword', weapon_type='melee', damage=5, value=10)
wooden_bow = Weapon(name='Wooden bow', weapon_type='ranged', damage=3, value=8)
fists = Weapon(name='Fists', weapon_type='melee', damage=2, value=0)
