# default packages
from random import randint

# imports from /map_objects
from map_objects.tile import Tile
from map_objects.rectangle import Rect


class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

        return tiles

    def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player):
        # Create two rooms for deomnstration
        rooms = []
        num_rooms = 0

        print("make_map called")

        for r in range(max_rooms):
            # random width and height
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)

            # random position without going out of the boundries of the map
            x = randint(0, map_width - w - 1)
            y = randint(0, map_height - h - 1)

            print ('calling new_room %d %d %d %d' % (x,y,w,h))
            # 'Rect' class makes rectangels easier to work with
            new_room = Rect(x, y, w, h)

            print(new_room)

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

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True
        return False
