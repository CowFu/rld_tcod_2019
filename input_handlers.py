import tcod

def handle_keys(key):
    #normal keypress
    key_press = {
        tcod.KEY_UP: {'move': (0, -1)},
        tcod.KEY_DOWN: {'move': (0, 1)},
        tcod.KEY_LEFT: {'move': (-1, 0)},
        tcod.KEY_RIGHT: {'move': (1, 0)},
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

    if key.lalt or key.ralt:
        if key.lctrl or key.rctrl:
            return both_key_press.get(key.vk, {})
        return alt_key_press.get(key.vk, {})
        
    if key.lctrl or key.rctrl:
        return ctrl_key_press.get(key.vk, {})
    return key_press.get(key.vk, {})
