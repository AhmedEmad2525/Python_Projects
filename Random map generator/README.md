# Random Map Generator

- This project is a simple text-based random map generator that creates a visually appealing representation of various terrain types. The map is displayed in the terminal using ANSI color codes to enhance the visual experience.
**Concepts**
-`Object-Oriented Programming`: Usage of classes to encapsulate tile and map functionality.
-`Randomization`: Creating random patches of tiles within the map for variability.
-`Console Visual Effects`: Utilizing ANSI escape codes for colorizing the terminal output.

## Features

- **Tile Class**: Represents different types of terrain with customizable symbols and colors.
- **Map Class**: Generates a map filled with terrain tiles and displays it in a frame.
- **Random Patch Generation**: Creates random patches of different terrain types within the map.
- **Interactive Map Display**: Continuously generates and displays new maps based on specified dimensions until the user decides to stop.

## Project Structure

### 1. Tile Class
The `Tile` class defines individual tiles for the map with properties such as:
- `symbol`: The character that represents the tile.
- `color`: The ANSI color code for the tile.
- `is_colored`: A boolean that determines whether the tile will use color.

**Example Tiles**:
```python
plains = Tile(".", ANSI_YELLOW)
forest = Tile("8", ANSI_GREEN)
pines = Tile("Y", ANSI_GREEN)
mountain = Tile("A", ANSI_WHITE)
water = Tile("~", ANSI_CYAN)
```

### 2. Map Class
The Map class represents the entire game map and is responsible for:

- Initializing the map with a default tile type (plains).
- Generating patches of different terrain types at random locations and sizes.

**Main Methods**:

-`generate_map()`: Initializes the map with plains tiles.
-`generate_patch(tile: Tile, num_patches: int, min_size: int, max_size: int)`: Creates a specified number of patches for a given tile type.
-`display_map()`: Displays the generated map within a frame.

### 3. Main Loop
The main script continuously generates and displays new maps based on specified dimensions until the user interrupts the process.

**Key Functionality**:

- Initializes the map with a specified width and height.
- Clears the console before displaying the next map.
- Allows the user to press the action button (Enter) to generate a new map.

  ### Output
  ![Screenshot 2024-10-05 203040](https://github.com/user-attachments/assets/9b848e53-2919-4bc1-bb87-53e439aa919c)
  
  ![Screenshot 2024-10-05 203031](https://github.com/user-attachments/assets/89319efd-7e9d-4c96-9d22-0ab4316c3611)
