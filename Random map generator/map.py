from tile import Tile, plains, forest, pines, mountain, water
from random import randint


class Map:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        # the list of lists that will represent our map
        self.map_data: list[list[Tile]]
        # calling the generate map method to generate the initial map upon calling the init
        self.generate_map()
        # having a random patch at a random place each postition
        self.generate_patch(forest, 2, 5, 7)
        self.generate_patch(pines, 2, 2, 5)
        self.generate_patch(mountain, 3, 5, 7)
        self.generate_patch(water, 1, 10, 12)

    def generate_map(self) -> None:
        """
        this function defines the initial frame for the map
        """
        self.map_data = [[plains for _ in range(self.width)] for _ in range(self.height)]

    def generate_patch(self, tile: Tile, num_patches: int, min_size: int, max_size: int) -> None:
        """
        this function generate a patch for selected element e.g making a patch for the forest in the map
        """
        # width and heights of the specific patch
        for _ in range(num_patches):
            width = randint(min_size, max_size)
            height = randint(min_size, max_size)
            # defining the coordinates for the patch on the map
            start_x = randint(1, self.width - width - 1)
            start_y = randint(1, self.height - height - 1)
            # swapping the predefined . values (plains) with the tile value
            for i in range(height):
                for j in range(width):
                    self.map_data[start_y + i][start_x + j] = tile

    def display_map(self) -> None:
        frame = 'X'+'='*self.width + 'X'
        print(frame)
        for row in self.map_data:
            # creating local list of symbols for each row
            row_tiles = [tile.symbol for tile in row]
            print('|'+''.join(row_tiles)+'|')
        print(frame)




