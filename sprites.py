import pygame as pg
import random
from settings import *
import math

segment_list = []
fireball_list = []
homing_fireball_list = []

class Player:
    def __init__(self):
        self.image = pg.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        
        self.rect.center = (
            100,
            100
        )
        
        self.score = 0
        
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
            
    def add_score(self):
        self.score += 10
                
    def update(self):
        self.move()
        self.check_collision()
        

class Head:
    def __init__(self):
        self.image = pg.Surface((HEAD_WIDTH, HEAD_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
        self.rect.center = (
            WIDTH//2 - PLAYER_WIDTH//2,
            HEIGHT//2 - PLAYER_HEIGHT//2
        )
        
        self.pos = pg.math.Vector2(self.rect.center)
        self.vel = pg.math.Vector2(0, 0)
        self.acc = pg.math.Vector2(0, 0)
        
        #self.acc_value = 0.5
        self.speed = 3
        
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
        
        self.target_acc = self.direction
        
        smoothing_factor = 0.04
        self.acc = self.acc.lerp(self.target_acc, smoothing_factor)
        
        self.vel += self.acc
        self.vel = self.vel.normalize()
    
        self.pos += self.vel * self.speed
        self.rect.center = self.pos
        
        if self.distance.length() <= 100:
            self.get_point()
            #self.add_segment()
            
    def add_segment(self):
        new_segment = Segment(self.rect.centerx, self.rect.centery)
        
        if segment_list:
            last_segment = segment_list[-1]
            
            new_segment.pos = last_segment.pos - self.direction * (2 * PLAYER_WIDTH)  # Adjust the multiplier as needed
            #new_segment.pos = pg.math.Vector2(last_segment.pos)
            new_segment.vel = pg.math.Vector2(last_segment.vel)
            
        segment_list.append(new_segment)

class Segment:
    
    segment_nr = 0
    
    def __init__(self, x, y):
        self.image = pg.Surface((SEGMENT_WIDTH, SEGMENT_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
        self.rect.center = (x, y)
        
        Segment.segment_nr += 1
        self.segment_nr = Segment.segment_nr
        
        self.pos = pg.math.Vector2(self.rect.center)
        self.vel = pg.math.Vector2(0, 0)
    
        self.speed = 3
        
    def move(self):
        if self.segment_nr > 0:  # Skip the head segment
            # Calculate the direction to follow the previous segment
            previous_segment = segment_list[self.segment_nr - 1]
            direction = pg.math.Vector2(previous_segment.pos - self.pos)
            distance = direction.length()
            direction.normalize_ip()

            # Apply acceleration towards the previous segment
            acceleration = direction * 0.1  # Adjust acceleration as needed

            # Update velocity and position based on acceleration
            self.vel += acceleration
            self.vel = self.vel.normalize()
            
            self.pos += self.vel * self.speed
            self.rect.center = self.pos
        
        
        
        
class FireBall:
    def __init__(self, x, y):
        self.image = pg.Surface((FIREBALL_WIDTH, FIREBALL_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
    
        self.rect.center = (x, y)
        
        self.pos = pg.math.Vector2(self.rect.center)
        
        self.vel_direction = pg.math.Vector2(random.uniform(-1,1), random.uniform(-1,1))
        
        self.speed = 3
    
        
    def move(self):
        while self.vel_direction.length() == 0:
            self.vel_direction = pg.math.Vector2(random.uniform(-1,1), random.uniform(-1,1))
        
        self.pos += self.vel_direction * self.speed
            
        self.rect.center = self.pos
        
    def check_collision(self):
        if self.pos.x <= FIREBALL_WIDTH//2:
            self.vel_direction.x *= -1
        
        if self.pos.x >= WIDTH - FIREBALL_WIDTH//2:
            self.vel_direction.x *= -1
    
    
        if self.pos.y <= FIREBALL_HEIGHT//2:
            self.vel_direction.y *= -1
        
        if self.pos.y >= HEIGHT - FIREBALL_HEIGHT//2:
            self.vel_direction.y *= -1
            
    def update(self):
        self.move()
        self.check_collision()




class HomingFireBall:
    def __init__(self, x, y, player_instance):
        self.image = pg.Surface((FIREBALL_WIDTH, FIREBALL_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
    
        self.rect.center = (x, y)
        
        self.pos = pg.math.Vector2(self.rect.center)
        self.vel = pg.math.Vector2(0, 0)
        self.speed = 2
        self.homing_strength = 0.1
        
        self.player_instance = player_instance
    
        
    def move(self):
        self.vel_direction = pg.math.Vector2(self.player_instance.rect.center[0] - self.pos.x, self.player_instance.rect.center[1] - self.pos.y)
        
        self.vel = self.vel_direction * self.homing_strength
        self.vel = self.vel.normalize()    
    
        self.pos += self.vel * self.speed
        self.rect.center = self.pos
            
    def update(self):
        self.move()
        
      
class Powerup:
    def __init__(self):
        self.image = pg.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
    
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.pos = pg.math.Vector2(self.rect.center)
        self.x = 0
        
    def move(self):
        self.x += 0.01
        self.rect.centery = (self.pos.y + int(25 * math.sin(self.x)))
        
        
        
        
        