import pygame as pg
import sys, random
import time
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # Initiere pygame
        pg.init()
        pg.mixer.init()

        # Lager hovedvinduet
        self.screen = pg.display.set_mode(SIZE)

        # Lager en klokke
        self.clock = pg.time.Clock()
        
        self.font = pg.font.SysFont("Arial", 26)
        self.title_font = pg.font.SysFont("Arial", 60)
        self.instructions_font = pg.font.SysFont("Arial", 30)
        
        # Attributt som styrer om spillet skal kjøres
        self.running = True
        
        self.last_segment_time = pg.time.get_ticks()
        self.last_time_coin_collected = pg.time.get_ticks()
        
        self.last_time_shot = pg.time.get_ticks()
        self.last_time_homing_shot = pg.time.get_ticks()
        self.last_time_fast_shot = pg.time.get_ticks()
        
    # Metode for å starte et nytt spill
    def new(self):
        # Lager spiller-objekt
        self.player = Player(self.screen)
        self.head = Head()
        segment_list.insert(0, self.head)
        #self.coin = Powerup()
        
        self.run()


    # Metode som kjører spillet
    def run(self):
        # Game loop
        self.playing = True
        
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        
        
    # Metode som håndterer hendelser
    def events(self):
        # Går gjennom hendelser (events)
        for event in pg.event.get():        
            # Sjekker om vi ønsker å lukke vinduet
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False # Spillet skal avsluttes
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    pass
                    #self.shockwave = Shockwave(self.screen, self.fast_fireball)
                    #shockwave_list.append(self.shockwave)
                    #self.shockwave.activate()
    
    # Metode som oppdaterer
    def update(self):
        self.player.update()
        
        current_time = pg.time.get_ticks()
        
        if current_time - self.last_segment_time >= 3000:
            self.head.add_segment()
            segment_sound.play()
            self.player.add_score()
            self.last_segment_time = current_time
            
        if current_time - self.last_time_shot >= fireball_spawn_interval:
            self.fireball = FireBall(self.head.pos.x, self.head.pos.y)
            fireball_list.append(self.fireball)
            fireball_sound.play()
            
            self.last_time_shot = pg.time.get_ticks()
            
        if current_time - self.last_time_homing_shot >= homing_fireball_spawn_interval:
            self.homing_fireball = HomingFireBall(self.head.pos.x, self.head.pos.y, self.player)
            homing_fireball_list.append(self.homing_fireball)
            homing_fireball_sound.play()
            
            self.last_time_homing_shot = pg.time.get_ticks()
            
        if current_time - self.last_time_fast_shot >= fast_fireball_spawn_interval:
            self.fast_fireball = FastFireball(self.head.pos.x, self.head.pos.y, self.player)
            fast_fireball_list.append(self.fast_fireball)
            fast_fireball_sound.play()
            
            self.last_time_fast_shot = pg.time.get_ticks()
            
        # Lager mynt-powerup objekt
        if current_time - self.last_time_coin_collected >= coin_spawn_interval:
            self.coin = Powerup()
            powerup_list.append(self.coin)
            
            self.last_time_coin_collected = pg.time.get_ticks()
        
        for segment in segment_list:
            segment.move()
            
            if segment.rect.colliderect(self.player.rect):
                self.playing = False
                self.running = False
        
        for fireball in fireball_list:
            fireball.update()
            
            if fireball.rect.colliderect(self.player.rect):
                self.playing = False
                self.running = False
                
        for homing_fireball in homing_fireball_list:
            homing_fireball.update()
            
            if homing_fireball.rect.colliderect(self.player.rect):
                self.playing = False
                self.running = False
                
        for fast_fireball in fast_fireball_list:
            fast_fireball.update()
            
            if self.fast_fireball.max_bounce == 0:
                fast_fireball_list.remove(fast_fireball)
                self.shockwave = Shockwave(self.screen, self.fast_fireball)
                shockwave_list.append(self.shockwave)
                fast_fireball_sound.stop()
                explosion_sound.play()
            
            if fast_fireball.rect.colliderect(self.player.rect):
                self.playing = False
                self.running = False
                
        for coin in powerup_list:
            coin.update()
            
            if coin.rect.colliderect(self.player.rect):
                self.player.score += 50
                powerup_list.remove(coin)    
    
    # Metode som tegner ting på skjermen
    def draw(self):
        # Fyller skjermen med en farge
        self.screen.fill(DARKGREY)
        #self.player.shockwave()
        
        for shockwave in shockwave_list:
            shockwave.update()
        
        #pg.draw.rect(self.screen, GREEN, self.player.rect)
        self.screen.blit(scaled_player_image, (self.player.rect.topleft))
        
        for segment in segment_list:
            
            if segment == self.head:
                self.screen.blit(scaled_head_image, (self.head.rect.topleft))
                #pg.draw.rect(self.screen, RED, segment.rect)
            else:
                self.screen.blit(scaled_segment_image, (segment.rect.topleft))
        
        #pg.draw.rect(self.screen, RED, (self.head.point[0], self.head.point[1], 10, 10))
        
        if len(fireball_list) > 0:
            for fireball in fireball_list:
                #pg.draw.rect(self.screen, LIGHTBLUE, fireball.rect)
                self.screen.blit(fireball.sprite_list[int(fireball.current_sprite)], (fireball.rect.topleft))
                
        if len(homing_fireball_list) > 0:
            for homing_fireball in homing_fireball_list:
                #pg.draw.rect(self.screen, YELLOW, homing_fireball.rect)
                self.screen.blit(homing_fireball.sprite_list[int(homing_fireball.current_sprite)], (homing_fireball.rect.topleft))
                
        if len(fast_fireball_list) > 0:
            for fast_fireball in fast_fireball_list:
                #pg.draw.rect(self.screen, YELLOW, fast_fireball.rect)
                self.screen.blit(scaled_fast_fireball_image, (fast_fireball.rect.topleft))
                
        if len(powerup_list) > 0:
            for coin in powerup_list:
                self.screen.blit(coin.sprite_list[int(coin.current_sprite)], (coin.rect.topleft))
    
        self.display_score()
        
        pg.display.flip()
    
    def display_score(self):
        text_img = self.font.render(f"{self.player.score}", True, WHITE)
        self.screen.blit(text_img, (WIDTH - 100, 20))
    
    # Metode som viser start-skjerm
    def show_start_screen(self):
        pass
        
    
# Lager et spill-objekt
game_object = Game()

# Spill-løkken
while game_object.running:
        
    # Starter et nytt spill
    game_object.new()
    

# Avslutter pygame
pg.quit()
#sys.exit() # Dersom det ikke er tilstrekkelig med pg.quit()