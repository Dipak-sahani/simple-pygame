import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image=pygame.image.load('robo.png')
        #self.image.fill(('red'))
        self.rect=self.image.get_rect(topleft=pos)
        self.direction=pygame.math.Vector2(0,0)
        self.speed=8
        self.gravity=0.8
        self.jump_speed=-16
    def import_character_assets(self):
        pass
    def apply_gravity(self):
        self.direction.y+=self.gravity
        self.rect.y+=self.direction.y


    def get_input(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x=1
        elif keys[pygame.K_LEFT]:
            self.direction.x=-1
        else:
            self.direction.x=0

        if keys[pygame.K_SPACE]:
            self.jump()
    def jump(self):
        self.direction.y=self.jump_speed
    def update(self):
        self.get_input()
