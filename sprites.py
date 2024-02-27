import pygame as pg
import random
from settings import *

acc_list = [pg.math.Vector2(0.0001,0.0001), pg.math.Vector2(0.0001,0.0001)]

class Player:
    def __init__(self):
        self.image = pg.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        
        self.rect.center = (
            WIDTH//2 - PLAYER_WIDTH//2,
            HEIGHT//2 - PLAYER_HEIGHT//2
        )
        
    def move(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
            
        if keys[pg.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
            
        if keys[pg.K_UP]:
            self.rect.y -= PLAYER_SPEED
            
        if keys[pg.K_DOWN]:
            self.rect.y += PLAYER_SPEED
            
    def check_collision(self):
        if self.rect.x <= 0:
            self.rect.x = 0
            
        if self.rect.x >= WIDTH - PLAYER_WIDTH:
            self.rect.x = WIDTH - PLAYER_WIDTH
                
        if self.rect.y <= 0:
            self.rect.y = 0
            
        if self.rect.y >= HEIGHT - PLAYER_HEIGHT:
            self.rect.y = HEIGHT - PLAYER_HEIGHT
                
    def update(self):
        self.move()
        self.check_collision()
        

class Head:
    def __init__(self):
        self.image = pg.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
        self.rect.center = (
            WIDTH//2 - PLAYER_WIDTH//2,
            HEIGHT//2 - PLAYER_HEIGHT//2
        )
        
        self.pos = pg.math.Vector2(self.rect.center)
        self.vel = pg.math.Vector2(0, 0)
        
        self.acc_value = 0.1
        self.speed = 2
        
        self.get_point()
        
    def get_point(self):
        self.point = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.distance = pg.math.Vector2(self.point[0] - self.pos.x, self.point[1] - self.pos.y).length()
        self.direction = pg.math.Vector2(self.point[0] - self.pos.x, self.point[1] - self.pos.y)
        
        if self.distance > 200:
            self.get_point()
            
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()
        
    def move(self):
        self.distance = pg.math.Vector2(self.point[0] - self.pos.x, self.point[1] - self.pos.y)
        
        self.acc = self.direction * self.acc_value
        acc_list.insert(0, self.acc)
        print(acc_list)
        
        self.vel += self.acc
        self.vel = self.vel.normalize()
            
    
        self.pos += self.vel * self.speed
        self.rect.center = self.pos
        
        #print(self.distance.length())
        
        if self.distance.length() <= 100:
            #acc_list.insert(0, self.acc)
            self.get_point()

class Segment:
    
    segment_nr = 0
    
    def __init__(self):
        self.image = pg.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
        self.rect.center = (
            WIDTH//2 - PLAYER_WIDTH//2,
            HEIGHT//2 - PLAYER_HEIGHT//2
        )
        
        Segment.segment_nr += 1
        self.segment_nr = Segment.segment_nr
        
        self.pos = pg.math.Vector2(self.rect.center)
        self.vel = pg.math.Vector2(0, 0)
        
        #self.acc_value = acc_list[self.segment_nr]
        self.speed = 2

        
    def move(self):
        
        self.acc = acc_list[self.segment_nr]
        
        self.vel += self.acc
        self.vel = self.vel.normalize()
            
    
        self.pos += self.vel * self.speed
        self.rect.center = self.pos