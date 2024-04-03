import pygame as pg
import random

# Konstanter
WIDTH = 1100  # Bredden til vinduet
HEIGHT = 650 # Høyden til vinduet

# Størrelsen til vinduet
SIZE = (WIDTH, HEIGHT)

# Frames Per Second (bilder per sekund)
FPS = 60

# Farger (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (20, 20, 20)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHTBLUE = (100, 100, 255)
GREY = (142, 142, 142)
LIGHTRED = (255, 100, 100)
YELLOW = (252, 220, 42)
PURPLE = (200, 75, 255)

BASE_COLOR = (255, 175, 69)
HOVER_COLOR = (255, 220, 100)
TITLE_COLOR = (251, 109, 72)

# Fontstørrelser
FONT_SIZE = 26
TITLE_FONT_SIZE = 60
INSTRUCTIONS_FONT_SIZE = 30

# Innstillinger til spilleren
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40
PLAYER_SPEED = 5

# Innstillinger til slangehodet
HEAD_WIDTH = 80
HEAD_HEIGHT = 80

# Innstillinger til slangesegment
SEGMENT_WIDTH = 50
SEGMENT_HEIGHT = 50

# Innstillinger til ildkuler
FIREBALL_WIDTH = 35
FIREBALL_HEIGHT = 35

# Innstillinger til powerups
COIN_WIDTH = 50
COIN_HEIGHT = 50

SHOCKWAVE_WIDTH = 50
SHOCKWAVE_HEIGHT = 50


# Spawning-intervaller av spillobjekter
fireball_spawn_interval = random.randint(3000, 5000)
homing_fireball_spawn_interval = 10_000
fast_fireball_spawn_interval = random.randint(12_000, 16_000)
coin_spawn_interval = 15_000


# Lydeffekter og musikk
pg.mixer.init()

segment_sound = pg.mixer.Sound("./Sound/segment.wav")
fireball_sound = pg.mixer.Sound("./Sound/fireball.wav")
homing_fireball_sound = pg.mixer.Sound("./Sound/homing_fireball.wav")
fast_fireball_sound = pg.mixer.Sound("./Sound/fast_fireball.wav")
explosion_sound = pg.mixer.Sound("./Sound/explosion.wav")
menu_sound = pg.mixer.Sound("./Sound/menu.wav")
coin_sound = pg.mixer.Sound("./Sound/coin.wav")

segment_sound.set_volume(0.1)
homing_fireball_sound.set_volume(0.5)
fast_fireball_sound.set_volume(0.7)
menu_sound.set_volume(0.2)
coin_sound.set_volume(0.5)

# Bilde for spiller
player_image = pg.image.load("./Sprites/player.png")
scaled_player_image = pg.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))

# Frames og sprites for slangehodet
head_image = pg.image.load("./Sprites/snake_head/head.png")
head_image_2 = pg.image.load("./Sprites/snake_head/head_2.png")
head_image_3 = pg.image.load("./Sprites/snake_head/head_3.png")
head_image_4 = pg.image.load("./Sprites/snake_head/head_4.png")
head_image_5 = pg.image.load("./Sprites/snake_head/head_5.png")
scaled_head_image = pg.transform.scale(head_image, (HEAD_WIDTH, HEAD_HEIGHT))
scaled_head_image_2 = pg.transform.scale(head_image_2, (HEAD_WIDTH, HEAD_HEIGHT))
scaled_head_image_3 = pg.transform.scale(head_image_3, (HEAD_WIDTH, HEAD_HEIGHT))
scaled_head_image_4 = pg.transform.scale(head_image_4, (HEAD_WIDTH, HEAD_HEIGHT))
scaled_head_image_5 = pg.transform.scale(head_image_5, (HEAD_WIDTH, HEAD_HEIGHT))

# Frames og sprites for slangesegment
segment_image = pg.image.load("./Sprites/snake_segment/segment.png")
segment_image_2 = pg.image.load("./Sprites/snake_segment/segment_2.png")
segment_image_3 = pg.image.load("./Sprites/snake_segment/segment_3.png")
segment_image_4 = pg.image.load("./Sprites/snake_segment/segment_4.png")
scaled_segment_image = pg.transform.scale(segment_image, (SEGMENT_WIDTH, SEGMENT_HEIGHT))
scaled_segment_image_2 = pg.transform.scale(segment_image_2, (SEGMENT_WIDTH, SEGMENT_HEIGHT))
scaled_segment_image_3 = pg.transform.scale(segment_image_3, (SEGMENT_WIDTH, SEGMENT_HEIGHT))
scaled_segment_image_4 = pg.transform.scale(segment_image_4, (SEGMENT_WIDTH, SEGMENT_HEIGHT))

# Frames og sprites for standard ildkule
fireball_image = pg.image.load("./Sprites/fireball/fireball.png")
fireball_image_2 = pg.image.load("./Sprites/fireball/fireball_2.png")
fireball_image_3 = pg.image.load("./Sprites/fireball/fireball_3.png")
scaled_fireball_image = pg.transform.scale(fireball_image, (FIREBALL_WIDTH, FIREBALL_HEIGHT))
scaled_fireball_image_2 = pg.transform.scale(fireball_image_2, (FIREBALL_WIDTH, FIREBALL_HEIGHT))
scaled_fireball_image_3 = pg.transform.scale(fireball_image_3, (FIREBALL_WIDTH, FIREBALL_HEIGHT))

# Frames og sprites for homing ildkule
homing_fireball_image = pg.image.load("./Sprites/homing_fireball/homing_fireball.png")
homing_fireball_image_2 = pg.image.load("./Sprites/homing_fireball/homing_fireball_2.png")
homing_fireball_image_3 = pg.image.load("./Sprites/homing_fireball/homing_fireball_3.png")
scaled_homing_fireball_image = pg.transform.scale(homing_fireball_image, (FIREBALL_WIDTH, FIREBALL_HEIGHT))
scaled_homing_fireball_image_2 = pg.transform.scale(homing_fireball_image_2, (FIREBALL_WIDTH, FIREBALL_HEIGHT))
scaled_homing_fireball_image_3 = pg.transform.scale(homing_fireball_image_3, (FIREBALL_WIDTH, FIREBALL_HEIGHT))

# Frames og sprites for mynt_powerup
coin_image = pg.image.load("./Sprites/coin/coin.png")
coin_image_2 = pg.image.load("./Sprites/coin/coin_2.png")
coin_image_3 = pg.image.load("./Sprites/coin/coin_3.png")
coin_image_4 = pg.image.load("./Sprites/coin/coin_4.png")
coin_image_5 = pg.image.load("./Sprites/coin/coin_5.png")
coin_image_6 = pg.image.load("./Sprites/coin/coin_6.png")
scaled_coin_image = pg.transform.scale(coin_image, (COIN_WIDTH, COIN_HEIGHT))
scaled_coin_image_2 = pg.transform.scale(coin_image_2, (COIN_WIDTH, COIN_HEIGHT))
scaled_coin_image_3 = pg.transform.scale(coin_image_3, (COIN_WIDTH, COIN_HEIGHT))
scaled_coin_image_4 = pg.transform.scale(coin_image_4, (COIN_WIDTH, COIN_HEIGHT))
scaled_coin_image_5 = pg.transform.scale(coin_image_5, (COIN_WIDTH, COIN_HEIGHT))
scaled_coin_image_6 = pg.transform.scale(coin_image_6, (COIN_WIDTH, COIN_HEIGHT))

fast_fireball_image = pg.image.load("./Sprites/fast_fireball.png")
scaled_fast_fireball_image = pg.transform.scale(fast_fireball_image, (FIREBALL_WIDTH, FIREBALL_HEIGHT))
