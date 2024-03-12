import pygame as pg

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

# Innstillinger til spilleren
PLAYER_WIDTH = 25
PLAYER_HEIGHT = 25
PLAYER_SPEED = 5

# Innstillinger til slangehodet
HEAD_WIDTH = 80
HEAD_HEIGHT = 80

# Innstillinger til slangesegment
SEGMENT_WIDTH = 50
SEGMENT_HEIGHT = 50

# Innstillinger til ildkule
FIREBALL_WIDTH = 30
FIREBALL_HEIGHT = 30




#Bilder og lydeffekter
pg.mixer.init()

add_segment_sound = pg.mixer.Sound("./Sound/add_segment.mp3")
shoot_fireball_sound = pg.mixer.Sound("./Sound/shoot_fireball.mp3")
shoot_homing_fireball_sound = pg.mixer.Sound("./Sound/shoot_homing_fireball.mp3")

fireball_image = pg.image.load("./Sprites/fireball.png")
homing_fireball_image = pg.image.load("./Sprites/homing_fireball.png")
segment_image = pg.image.load("./Sprites/snake_segment_2.png")
head_image = pg.image.load("./Sprites/snake_head_2.png")
background_image = pg.image.load("./Sprites/background.png")

scaled_fireball_image = pg.transform.scale(fireball_image, (FIREBALL_WIDTH, FIREBALL_HEIGHT))
scaled_homing_fireball_image = pg.transform.scale(homing_fireball_image, (FIREBALL_WIDTH, FIREBALL_HEIGHT))
scaled_segment_image = pg.transform.scale(segment_image, (SEGMENT_WIDTH, SEGMENT_HEIGHT))
scaled_head_image = pg.transform.scale(head_image, (HEAD_WIDTH, HEAD_HEIGHT))
scaled_background_image = pg.transform.scale(background_image, (WIDTH, HEIGHT))

