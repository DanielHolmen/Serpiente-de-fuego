import pygame as pg
import random
from settings import *

acc_list = []
segment_list = []
fireball_list = []

class Player:
    def __init__(self):
        self.image = pg.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        
        """
        self.rect.center = (
            WIDTH//2 - PLAYER_WIDTH//2,
            HEIGHT//2 - PLAYER_HEIGHT//2
        )
        """
        
        self.rect.center = (
            100,
            100
        )
        
        self.score = 0
        self.last_time_score_added = pg.time.get_ticks()
        
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
        self.image = pg.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
        self.rect.center = (
            WIDTH//2 - PLAYER_WIDTH//2,
            HEIGHT//2 - PLAYER_HEIGHT//2
        )
        
        self.pos = pg.math.Vector2(self.rect.center)
        self.vel = pg.math.Vector2(0, 0)
        
        self.acc_value = 0.1
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
        
        self.acc = self.direction * self.acc_value
        acc_list.insert(0, self.acc)
        
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
        self.image = pg.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
        """
        self.rect.center = (
            WIDTH//2 - PLAYER_WIDTH//2,
            HEIGHT//2 - PLAYER_HEIGHT//2
        )
        """
        
        self.rect.center = (x, y)
        
        Segment.segment_nr += 1
        self.segment_nr = Segment.segment_nr
        
        self.pos = pg.math.Vector2(self.rect.center)
        self.vel = pg.math.Vector2(0, 0)
    
        self.speed = 3
        
    def move(self):
        """
        self.acc = acc_list[self.segment_nr]
            
        self.vel += self.acc
        self.vel = self.vel.normalize()
                
        
        self.pos += self.vel * self.speed
        self.rect.center = self.pos
        """
        
        
        """
        if self.segment_nr > 0:  # Skip the head segment
            # Calculate the direction to follow the previous segment
            previous_segment = segment_list[self.segment_nr - 1]
            
            direction = pg.math.Vector2(previous_segment.pos - self.pos)
            distance = pg.math.Vector2(previous_segment.pos - self.pos).length()
            direction.normalize_ip()
            
            if distance <= 40:
                self.vel = pg.math.Vector2(0, 0)
                #self.direction *= 0.5
                
            else:
                # Move towards the previous segment
                self.pos += direction * self.speed
                self.rect.center = self.pos
        """

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
        self.image = pg.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
    
        self.rect.center = (x, y)
        
        self.pos = pg.math.Vector2(self.rect.center)
        
        self.vel_direction = pg.math.Vector2(random.randint(-1,1), random.randint(-1,1))
        
        self.speed = 3
    
        
    def move(self):
        
        while self.vel_direction.length() == 0:
            self.vel_direction = pg.math.Vector2(random.randint(-1,1), random.randint(-1,1))
        
        self.pos += self.vel_direction * self.speed
            
        self.rect.center = self.pos
        
    def check_collision(self):
        if self.pos.x <= 0 + 25//2:
            self.vel_direction.x *= -1
        
        if self.pos.x >= WIDTH - 25//2:
            self.vel_direction.x *= -1
    
    
        if self.pos.y <= 0 + 25//2:
            self.vel_direction.y *= -1
        
        if self.pos.y >= HEIGHT - 25//2:
            self.vel_direction.y *= -1
            
        
        
        
        