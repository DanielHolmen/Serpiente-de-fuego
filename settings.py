import pygame as pg
import random

# Konstanter
WIDTH = 1100  # Bredden til vinduet
HEIGHT = 700 # Høyden til vinduet

# Størrelsen til vinduet
SIZE = (WIDTH, HEIGHT)

# Frames Per Second (bilder per sekund)
FPS = 60

# Farger (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (25, 25, 25)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHTBLUE = (100, 100, 255)
GREY = (142, 142, 142)
LIGHTRED = (255, 100, 100)
YELLOW = (252, 220, 42)
PURPLE = (200, 75, 255)

# Innstillinger til spilleren
PLAYER_WIDTH = 45
PLAYER_HEIGHT = 45
PLAYER_SPEED = 5

# Innstillinger til slangehodet
HEAD_WIDTH = 80
HEAD_HEIGHT = 80

# Innstillinger til slangesegment
SEGMENT_WIDTH = 50
SEGMENT_HEIGHT = 50

# Innstillinger til ildkuler
FIREBALL_WIDTH = 30
FIREBALL_HEIGHT = 30

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


# Lydeffekter og mussikk
pg.mixer.init()

segment_sound = pg.mixer.Sound("./Sound/segment.wav")
fireball_sound = pg.mixer.Sound("./Sound/fireball.wav")
homing_fireball_sound = pg.mixer.Sound("./Sound/homing_fireball.wav")
fast_fireball_sound = pg.mixer.Sound("./Sound/fast_fireball.wav")
explosion_sound = pg.mixer.Sound("./Sound/explosion.wav")

segment_sound.set_volume(0.1)
homing_fireball_sound.set_volume(0.5)
fast_fireball_sound.set_volume(0.7)



# Bilder og sprites
player_image = pg.image.load("./Sprites/player.png")
fireball_image = pg.image.load("./Sprites/fireball.png")
homing_fireball_image = pg.image.load("./Sprites/homing_fireball.png")
fast_fireball_image = pg.image.load("./Sprites/fast_fireball.png")
segment_image = pg.image.load("./Sprites/snake_segment_2.png")
head_image = pg.image.load("./Sprites/snake_head_2.png")
coin_image = pg.image.load("./Sprites/coin.png")

scaled_player_image = pg.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
scaled_fireball_image = pg.transform.scale(fireball_image, (FIREBALL_WIDTH, FIREBALL_HEIGHT))
scaled_homing_fireball_image = pg.transform.scale(homing_fireball_image, (FIREBALL_WIDTH, FIREBALL_HEIGHT))
scaled_fast_fireball_image = pg.transform.scale(fast_fireball_image, (FIREBALL_WIDTH, FIREBALL_HEIGHT))
scaled_segment_image = pg.transform.scale(segment_image, (SEGMENT_WIDTH, SEGMENT_HEIGHT))
scaled_head_image = pg.transform.scale(head_image, (HEAD_WIDTH, HEAD_HEIGHT))
scaled_coin_image = pg.transform.scale(coin_image, (COIN_WIDTH, COIN_HEIGHT))

