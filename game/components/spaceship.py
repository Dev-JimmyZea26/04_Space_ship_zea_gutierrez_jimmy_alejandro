import pygame as pg
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SPACESHIP_SHIELD, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = SCREEN_HEIGHT - 100
    
    def __init__(self):
        self.image = SPACESHIP
        self.image = pg.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        
    # Events   
    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10
        else:
            self.rect.x = SCREEN_WIDTH - 40
    
    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
        else:
            self.rect.x = 0
    
    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= 10
    
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += 10

            
    def update(self, user_input):
        if user_input[pg.K_LEFT]:
            self.move_left()
        elif user_input[pg.K_RIGHT]:
            self.move_right()
        elif user_input[pg.K_UP]:
            self.move_up()
        elif user_input[pg.K_DOWN]:
            self.move_down()

    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))