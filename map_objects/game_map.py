# default packages
from random import randint
import tcod

from components.ai import BasicMonster
from components.fighter import Fighter

# imports from /map_objects
from map_objects.tile import Tile
from map_objects.rectangle import Rect
from entity import Entity

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

        return tiles

    def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height,
                 player, entities, max_monsters_per_room):
        # Create two rooms for deomnstration
        rooms = []
        num_rooms = 0

        for r in range(max_rooms):
            # random width and height
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)

            # random position without going out of the boundries of the map
            x = randint(0, map_width - w - 1)
            y = randint(0, map_height - h - 1)

            # 'Rect' class makes rectangels easier to work with
            new_room = Rect(x, y, w, h)
            center_x, center_y = 0,0
            prev_x, prev_y = 0,0
            # run through existing rooms and see if they intersect with the new one
            for other_room in rooms:
                if new_room.intersect(other_room):
                    break
            else:
                # no intersections, valid room

                # paint it to the map's tiles
                self.create_room(new_room)

                # center coordinates of new room
                (center_x, center_y) = new_room.center()

                if num_rooms == 0:
                    # first room
                    player.x = center_x
                    player.y = center_y
                else:
                    # not the fist room
                    # have to connect it to previous room with a tunnel

                    (prev_x, prev_y) = rooms[num_rooms - 1].center()

                    # flip a coin
                    if randint(0, 1) == 1:
                        # first move horizontally, then vertically
                        self.create_h_tunnel(prev_x, center_x, prev_y)
                        self.create_v_tunnel(prev_y, center_y, center_x)
                    else:
                        # first move vertically, then horizontal
                        self.create_v_tunnel(prev_y, center_y, center_x)
                        self.create_h_tunnel(prev_x, center_x, prev_y)
                
                self.place_entities(new_room, entities, max_monsters_per_room)

                # finally, append the new room to the list
                rooms.append(new_room)
                num_rooms += 1


    def create_room(self, room):
        # go through the list of tiles in the rectangle and make them passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) +1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def place_entities(self, room, entities, max_monsters_per_room):
        # Get a random number of monsters
        number_of_monsters = randint(0, max_monsters_per_room)

        for i in range(number_of_monsters):
            # Choose a random location in the room
            x = randint(room.x1 + 1, room.x2 - 1)
            y = randint(room.y1 + 1, room.y2 - 1)

            if not any([entity for entity in entities if entity.x == x and entity.y == y]):
                if randint(0, 100) < 80:
                    fighter_component = Fighter(hp=10, defense=0, power=3)
                    ai_component = BasicMonster()

                    monster = Entity(x, y, 'o', tcod.desaturated_green, 'Orc', blocks=True, 
                                     fighter=fighter_component, ai=ai_component, entityID=len(entities))
                else:
                    fighter_component = Fighter(hp=16, defense=1, power=4)
                    ai_component = BasicMonster()

                    monster = Entity(x, y, 'T', tcod.darker_green, 'Troll', blocks=True,
                                     fighter=fighter_component, ai=ai_component, entityID=len(entities))

                entities.append(monster)

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True
        return False
