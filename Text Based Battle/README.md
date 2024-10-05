# Text Based Battle

This project is a text-based battle simulation between a hero and an enemy, where players can see the health bars of both characters and watch the outcome of each attack in real-time. It demonstrates various programming concepts in Python, including object-oriented programming, custom classes, and the use of color for visual enhancements in the console.

## Concepts
- **Object-Oriented Programming**: Classes for characters, weapons, and health bars demonstrate inheritance and encapsulation.
- **Console Visual Effects**: Use of color codes to create a more engaging terminal interface.
-**Basic Game Mechanics**: Simulates simple combat logic with health management and weapon damage.

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
```
### 2. Health Bar
The HealthBar class is responsible for visualizing the character's health during the battle. It uses customizable symbols, colors, and barriers to create a health bar for each character and take parameters such as:
-`symbol_remaining` and `symbol_lost`: Symbols to show remaining and lost health.
- `barrier`: Character used to enclose the health bar.
- `colors`: A dictionary defining various colors for the health bar.

### 3. Charecter
The `Character` class represents each combatant in the game and provides methods for attacking.

####Subclasses:

-`Hero`: Can equip and drop weapons.
-`Enemy`: Has a predefined weapon and health bar.

####Attributes:

-`name`: Name of the character.
-`health` and `max_health`: Track current and maximum health values.
-`weapon`: The weapon a character wields.

### 4. Main loop
In the `main` script, the battle simulation begins by creating the hero and enemy. They then take turns attacking each other until one character's health reaches zero. After each attack, the health bars of both characters are updated and displayed.
![image](https://github.com/user-attachments/assets/092e7295-e59e-4bc4-a22c-dd2ff2ecca07)
#### Key Functionality:
Allows the player to press the action button (Enter) after each attack to progress the fight.
Uses os.system("cls") to clear the console after each action for a clean output (works on Windows; for other systems, consider replacing with os.system("clear")).

