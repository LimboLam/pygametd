import pygame as pg
import sys
import constants as c
from enemy import Enemy
from world import World
import json
from turret import Turret

def main():
    pg.init()

    clock = pg.time.Clock()

    screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    pg.display.set_caption('Tower Defence')

    map_image = pg.image.load('levels/level.png').convert_alpha()
    cursor_turret = pg.image.load('assets/images/turrets/cursor_turret.png')
    enemy_image = pg.image.load('assets/images/enemies/enemy_1.png').convert_alpha()\
    
    # load json data for level
    with open('levels/level.tmj') as file:
        world_data = json.load(file)

    def create_turret(mouse_pos):
        mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
        mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
        # calc sequential num of tile
        mouse_tile_num = (mouse_tile_y * c.COLS) + mouse_tile_x
        # check if tile is grass
        if world.tile_map[mouse_tile_num] == 7:
            turret = Turret(cursor_turret, mouse_tile_x, mouse_tile_y)
            turret_group.add(turret)

    world = World(world_data, map_image)
    world.process_data()

    enemy_group = pg.sprite.Group()
    turret_group = pg.sprite.Group()

    enemy = Enemy(world.waypoints, enemy_image)
    enemy_group.add(enemy)

    running = True
    while running:
        clock.tick(c.FPS)

        screen.fill('black')

        world.draw(screen)

        enemy_group.update()
        turret_group.draw(screen)

        enemy_group.draw(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pg.mouse.get_pos()
                # check if mouse in on game area
                if mouse_pos[0] < c.SCREEN_WIDTH and mouse_pos[1] < c.SCREEN_HEIGHT:
                    create_turret(mouse_pos)

        pg.display.flip()

    print('QUIT')
    pg.quit()
    sys.exit()

if __name__ == '__main__':
    main()