from map import Map
import os

map_w, map_h = 30, 15
while True:
    os.system("cls")
    game_map = Map(map_w, map_h)
    game_map.display_map()
    input()
    




