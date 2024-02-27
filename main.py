import pygame as pg
import sys, random
import time
from settings import *
from sprites import *

segment_list = []

dt = 0
t1 = time.time()

class Game:
    def __init__(self):
        # Initiere pygame
        pg.init()

        # Lager hovedvinduet
        self.screen = pg.display.set_mode(SIZE)

        # Lager en klokke
        self.clock = pg.time.Clock()
        
        # Attributt som styrer om spillet skal kjøres
        self.running = True
        
        
    # Metode for å starte et nytt spill
    def new(self):
        # Lager spiller-objekt
        self.player = Player()
        self.head = Head()
        self.segment = Segment()
        
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
        self.head.move()
        self.segment.move()
        """
        segment_list.append(self.segment)
        for segment in segment_list:
            self.segment.move()
        """
        
    
    # Metode som tegner ting på skjermen
    def draw(self):
        # Fyller skjermen med en farge
        self.screen.fill(WHITE)
        
        pg.draw.rect(self.screen, GREEN, self.player.rect)
        pg.draw.rect(self.screen, RED, self.head.rect)
        pg.draw.rect(self.screen, LIGHTRED, self.segment.rect)
        #pg.draw.rect(self.screen, RED, (self.head.point[0], self.head.point[1], 10, 10))
        
        # "Flipper" displayet for å vise hva vi har tegnet
        pg.display.flip()
    
    
    # Metode som viser start-skjerm
    def show_start_screen(self):
        pass
    
# Lager et spill-objekt
game_object = Game()

# Spill-løkken
while game_object.running:
    # Starter et nytt spill
    game_object.new()
    
    """
    t2 = time.time()
    
    dt = t2 - t1
    
    if dt > 1:
        segment = Segment()
        pg.draw.rect(self.screen, LIGHTRED, self.segment.rect)
        segment.move()
        t1 = time.time()
    """

# Avslutter pygame
pg.quit()
#sys.exit() # Dersom det ikke er tilstrekkelig med pg.quit()