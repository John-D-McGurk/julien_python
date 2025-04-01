import random
import pygame as pg
import os


class Screen:
    def __init__(self):
        self.x_size = 1000
        self.y_size = 1000

class UFO:
    def __init__(self, screen, player):
        self.random_coords(screen)
      
    def random_coords(self, screen):
        self.x = random.randint(0, screen.x_size)
        self.y = random.randint(0, screen.y_size)

class Player:
    def __init__(self, screen):
        self.x = screen.x_size / 2
        self.y = screen.y_size / 2
        self.angle = 0

class Asteroid:
    def __init__(self, screen):
        self.random_coords(screen)

    def random_coords(self, screen):
        self.x = random.randint(0, screen.x_size)
        self.y = random.randint(0, screen.y_size)

if __name__ == '__main__':
    screen_obj = Screen()
 
    pg.init()
    clock = pg.time.Clock()
    screen_dims = (screen_obj.x_size, screen_obj.y_size)
    screen = pg.display.set_mode(screen_dims)

    player = Player(screen_obj)

    player_sprite = pg.image.load(os.path.join())
    

    while True:

        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
        
        keys = pg.key.get_pressed()
        if keys.K_w:
            player.y = player.y - 300



        #pg.draw.circle(screen, 'red', (player.x, player.y), 40)
        pg.Rect(player.x, player.y, 30, 30)
        pg.Surface.blit()


        pg.display.update()
        clock.tick(1)