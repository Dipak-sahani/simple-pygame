import pygame, sys
from setting import*
from tiles import*
from levels import*
pygame.init()
screen=pygame.display.set_mode((screen_width,screen_hight))
clock=pygame.time.Clock()
level=Level(level_map,screen)
tile=pygame.sprite.Group(Tile((100,100),100))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')
    level.run()
    pygame.display.update()
    clock.tick(30)