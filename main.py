import pygame as pg
import sys
import constants as c
from enemy import Enemy
from world import World
import json

def main():
    pg.init()

    clock = pg.time.Clock()

    screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    pg.display.set_caption('Tower Defence')

    map_image = pg.image.load('levels/level.png').convert_alpha()
    enemy_image = pg.image.load('assets/images/enemies/enemy_1.png').convert_alpha()\
    
    # load json data for level
    with open('levels/level.tmj') as file:
        world_data = json.load(file)

    world = World(world_data, map_image)
    world.process_data()

    enemy_group = pg.sprite.Group()

    enemy = Enemy(world.waypoints, enemy_image)
    enemy_group.add(enemy)

    running = True
    while running:
        clock.tick(c.FPS)

        screen.fill('black')

        world.draw(screen)

        enemy_group.update()

        enemy_group.draw(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        pg.display.flip()

    print('QUIT')
    pg.quit()
    sys.exit()

if __name__ == '__main__':
    main()