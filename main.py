import pygame as pg
import sys
from settings import *
from sprites import *
from button import Button

pg.init()

BG = pg.image.load("bilder/background_menu.png")

SCREEN = pg.display.set_mode((1280, 720))
pg.display.set_caption("Serpiente de Fuego")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pg.font.Font("Bilder/font.ttf", size)


class Game:
    def __init__(self):
        # Lager hovedvinduet
        self.screen = pg.display.set_mode(SIZE)

        # Lager en klokke
        self.clock = pg.time.Clock()

        self.font = pg.font.SysFont("Arial", 26)
        self.title_font = pg.font.SysFont("Arial", 60)
        self.instructions_font = pg.font.SysFont("Arial", 30)

        # Attributt som styrer om spillet skal kjøres
        self.running = True  # Initially set to False
        self.playing = False  # Initially set to False
        
        self.main_menu_active = True
        
        self.player = Player(SCREEN)

        self.last_segment_time = pg.time.get_ticks()
        self.last_time_coin_collected = pg.time.get_ticks()

        self.last_time_shot = pg.time.get_ticks()
        self.last_time_homing_shot = pg.time.get_ticks()
        self.last_time_fast_shot = pg.time.get_ticks()
        
        self.lose_counter = 0

    # Metode for å starte et nytt spill
    def new(self):
            self.playing = True
            self.reset_game_state()
            self.head = Head()
            segment_list.insert(0, self.head)
            self.running = True
            self.run()

    # Metode som kjører spillet
    def run(self):
        while self.running:
        # Show main menu only if not currently playing
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
   

    # Method to reset game state after game over
    def reset_game_state(self):
        # Clear all the lists
        segment_list.clear()
        fireball_list.clear()
        homing_fireball_list.clear()
        fast_fireball_list.clear()
        powerup_list.clear()
        # Reset player score
        self.player.score = 0
        self.player.rect.center = (
            100,
            100
        )
        Segment.segment_nr=0
        # Method to show the main menu
    def show_main_menu(self):
        SCREEN.fill("BLACK")
        self.main_menu_active = True
        while self.main_menu_active:
            SCREEN.fill("BLACK")
            MENU_MOUSE_POS = pg.mouse.get_pos()

            MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = Button(image=pg.image.load("Bilder/Play Rect.png"), pos=(640, 250),
                                 text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pg.image.load("Bilder/Options Rect.png"), pos=(640, 400),
                                    text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pg.image.load("Bilder/Quit Rect.png"), pos=(640, 550),
                                 text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

            SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.new()
                        print("2")# Start a new game
                        self.main_menu_active = False
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        options()
                        self.main_menu_active = False
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pg.quit()
                        sys.exit()
                        self.main_menu_active = False

            pg.display.update()

    # Metode som håndterer hendelser
    def events(self):
        """
        # Går gjennom hendelser (events)
        for event in pg.event.get():
            # Sjekker om vi ønsker å lukke vinduet
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False  # Spillet skal avsluttes

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    pass
                    # self.shockwave = Shockwave(self.screen, self.fast_fireball)
                    # shockwave_list.append(self.shockwave)
                    # self.shockwave.activate()
        """
        if self.playing:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.playing = False
                    self.running = False
                    
                    
                    
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        pass  # Handle space key event here
        # Handle events in the main menu
        else:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    MENU_MOUSE_POS = pg.mouse.get_pos()
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.new()
                        print("1")
                        self.main_menu_active = False
                    elif OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        options()
                        self.main_menu_active = False
                    elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pg.quit()
                        sys.exit()
                        self.main_menu_active = False
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
            segment.update()
            
            #if segment == self.head:
                #segment.animate()
            
            if segment.rect.colliderect(self.player.rect):
                self.playing = False
                self.running = False
                self.show_main_menu()
                
                
        
        for fireball in fireball_list:
            fireball.update()
            
            if fireball.rect.colliderect(self.player.rect):
                self.playing = False
                self.running = False
                
                self.show_main_menu()
                
                
        for homing_fireball in homing_fireball_list:
            homing_fireball.update()
            
            if homing_fireball.rect.colliderect(self.player.rect):
                self.playing = False
                self.running = False
                self.show_main_menu()
            
                
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
                self.show_main_menu()
                
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
                self.screen.blit(segment.sprite_list[int(segment.current_sprite)], (segment.rect.topleft))
                #pg.draw.rect(self.screen, RED, segment.rect)
            else:
                self.screen.blit(segment.sprite_list[int(segment.current_sprite)], (segment.rect.topleft))
        
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


game_object = Game()
game_object.show_main_menu()  # Start with the main menu

# Avslutter pygame
pg.quit()
# sys.exit() # Dersom det ikke er tilstrekkelig med pg.quit()
