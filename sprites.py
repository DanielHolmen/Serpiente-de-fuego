import pygame as pg
from settings import *

class Player:
    def __init__(self):
        self.image = pg.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (
            WIDTH//2 - PLAYER_WIDTH//2,
            HEIGHT//2 - PLAYER_HEIGHT//2
        )

    
    def update(self):
        pass