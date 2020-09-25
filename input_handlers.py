import tcod


def handle_keys(key):
    # normal keypress
    key_press = {
        # movement
        # up
        tcod.KEY_UP: {'move': (0, -1)},
        tcod.KEY_KP8: {'move': (0, -1)},
        'k': {'move': (0, -1)},
        # down
        tcod.KEY_DOWN: {'move': (0, 1)},
        tcod.KEY_KP2: {'move': (0, 1)},
        'j': {'move': (0, 1)},
        # left
        tcod.KEY_LEFT: {'move': (-1, 0)},
        tcod.KEY_KP4: {'move': (-1, 0)},
        'h': {'move': (-1, 0)},
        # right
        tcod.KEY_RIGHT: {'move': (1, 0)},
        tcod.KEY_KP6: {'move': (1, 0)},
        'l': {'move': (1, 0)},
        # diagonals
        tcod.KEY_KP1: {'move': (-1, 1)},
        'b': {'move': (-1, 1)},
        tcod.KEY_KP7: {'move': (-1, -1)},
        'y': {'move': (-1, -1)},
        tcod.KEY_KP9: {'move': (1, -1)},
        'u': {'move': (1, -1)},
        tcod.KEY_KP3: {'move': (1, 1)},
        'n': {'move': (1, 1)},
        tcod.KEY_ESCAPE: {'exit': True}
    }

    alt_key_press = {
        tcod.KEY_ENTER: {'fullscreen': True},
        tcod.KEY_1: {'msg': 'alt and 1'}
    }

    ctrl_key_press = {
        tcod.KEY_1: {'msg': 'ctrl and 1'}
    }

    both_key_press = {
        tcod.KEY_1: {'msg': 'ctrl + alt and 1'}
    }

    if(key.vk == 65):
        keypress = chr(key.c)
    else:
        keypress = key.vk

    if key.lalt or key.ralt:
        if key.lctrl or key.rctrl:
            return both_key_press.get(keypress, {})
        return alt_key_press.get(keypress, {})

    if key.lctrl or key.rctrl:
        return ctrl_key_press.get(keypress, {})
    return key_press.get(keypress, {})
