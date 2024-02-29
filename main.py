import pygame as pg
import sys, random
import time
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # Initiere pygame
        pg.init()

        # Lager hovedvinduet
        self.screen = pg.display.set_mode(SIZE)

        # Lager en klokke
        self.clock = pg.time.Clock()
        
        self.font = pg.font.SysFont("Arial", 26)
        
        # Attributt som styrer om spillet skal kjøres
        self.running = True
        
        self.last_segment_time = pg.time.get_ticks()
        
        self.last_time_score_added = pg.time.get_ticks()
        
        
    # Metode for å starte et nytt spill
    def new(self):
        # Lager spiller-objekt
        self.player = Player()
        self.head = Head()
        segment_list.insert(0, self.head)
        #self.segment = Segment()
        
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

    
    # Metode som oppdaterer
    def update(self):
        self.player.update()
        
        current_time = pg.time.get_ticks()
        if current_time - self.last_segment_time >= 3000:
            self.head.add_segment()
            self.player.add_score()
            self.last_segment_time = current_time
            self.fireball = FireBall(self.head.pos.x, self.head.pos.y)
            fireball_list.append(self.fireball)
        
        for segment in segment_list:
            segment.move()
            
            if segment.rect.colliderect(self.player.rect):
                self.playing = False
                self.running = False
        
        for fireball in fireball_list:
            fireball.move()
            fireball.check_collision()
            
            if fireball.rect.colliderect(self.player.rect):
                self.playing = False
                self.running = False
    
    # Metode som tegner ting på skjermen
    def draw(self):
        # Fyller skjermen med en farge
        self.screen.fill(WHITE)
        self.display_score()
        
        pg.draw.rect(self.screen, GREEN, self.player.rect)
        
        for segment in segment_list:
            pg.draw.rect(self.screen, RED, segment.rect)
        
        #pg.draw.rect(self.screen, RED, (self.head.point[0], self.head.point[1], 10, 10))
        
        if len(fireball_list)>0:
            for fireball in fireball_list:
                pg.draw.rect(self.screen, LIGHTBLUE, fireball.rect)
    
        pg.display.flip()
    
    def display_score(self):
        text_img = self.font.render(f"{self.player.score}", True, BLACK)
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