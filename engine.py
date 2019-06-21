import tcod
from entity import Entity
from input_handlers import handle_keys

def main():
    screen_width = 80
    screen_height = 50

    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', tcod.white)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', tcod.yellow)

    entities = [npc, player]

    tcod.console_set_custom_font('.\\assets\\fonts\\arial10x10.png', 
                                  tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    
    tcod.console_init_root(screen_width,
                           screen_height,
                           'libtcod tutorial revised',
                           fullscreen=False)
    
    con = tcod.console_new(screen_width, screen_height)

    key = tcod.Key()
    mouse = tcod.Mouse()

    while not tcod.console_is_window_closed():
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)

        tcod.console_set_default_foreground(con, tcod.white)
        tcod.console_put_char(con, player.x, player.y, '@', tcod.BKGND_NONE)
        tcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
        tcod.console_flush()

        tcod.console_put_char(con, player.x, player.y, ' ', tcod.BKGND_NONE)

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')
        msg = action.get('msg')

        if move:
            dx, dy = move
            player.move(dx,dy)

        if exit:
            return True

        if fullscreen:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

        if msg:
            tcod.console_print(con, 1, 1, '                  ')
            tcod.console_print(con, 1, 1, msg)
    
if __name__ == '__main__':
    main()
