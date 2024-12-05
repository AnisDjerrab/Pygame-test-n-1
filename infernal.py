import pygame
import time
import random
import winsound

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Arcade Quest")

CUSTOM_COLOR = ((50, 0, 100))
WHIDTH, HIGHT = 1000, 800
FPS = 60
RED = ((255, 0, 0))
DARK_RED = ((100, 0, 0))
GREEN = ((0, 75, 50))
weird_green = ((0, 50, 50)) 
BLACK = ((0, 0, 0))
PLAYER_SPEED = 8
PLAYER_RADIUS = 20
TILE_SIZE = 40
JUMP = 12
GRAVITY = 0.3
BLUE = ((0, 0, 100))
player_x, player_y = 100, 500
velocity_y = 0
ORANGE = (255, 165, 0)
WORLD_HEIGHT = 1600
WORLD_WEIDTH = 15040
MAX_FALL_SPEED = 20
screen = pygame.display.set_mode((WHIDTH, HIGHT))
DARK_DARK_RED = ((20, 0, 0))

def Background(camera_offset_x):
    for largeur in range(0, HIGHT, TILE_SIZE):
        for hauteur in range(-camera_offset_x, -camera_offset_x + WHIDTH, TILE_SIZE):
            pygame.draw.rect(screen, weird_green, (hauteur, largeur, TILE_SIZE, TILE_SIZE))

granit = []
triangle = []




def granit_rocks():
    x = 40
    u = 760
    for s in range(2):
        for i in range(5):
            tile_x = x
            tile_y = u
            granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            x += 40
        u -= 40
        x = 40
    x = 760
    for s in range(40):
        tile_x = 0
        tile_y = x
        granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
        x -= 40
    x = 360
    u = 760
    for s in range(2):
        for i in range(5):
            tile_x = x
            tile_y = u
            granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            x += 40
        u -= 40
        x = 360
    u = 760
    x = 640
    for i in range(2):
        for s in range(4):
            tile_x = x
            tile_y = u
            granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            u -= 40
        x += 40
        u = 760
    u = 760
    x = 880
    for i in range(2):
        for s in range(6):
            tile_x = x
            tile_y = u
            granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            u -= 40
        x += 40
        u = 760
    u = 760
    x = 1120
    for i in range(2):
        for s in range(8):
            tile_x = x
            tile_y = u
            granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            u -= 40
        x += 40
        u = 760
    u = 760
    x = 1440
    for i in range(2):
        for s in range(12):
            tile_x = x
            tile_y = u
            granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            u -= 40
        x += 40
        u = 760
    u = 760
    x = 1760
    for i in range(2):
        for s in range(16):
            tile_x = x
            tile_y = u
            granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            u -= 40
        x += 40
        u = 760
    u = 200
    x = 2000
    for i in range(4):
        tile_x = x
        tile_y = u
        granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
        u += 40
        x += 400
    x -= 200
    u += 40

    for i in range(4):
        tile_x = x
        tile_y = u
        granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
        x += 40
    x = 3640
    u = 760
    for s in range(2):
        for i in range(3):
            tile_x = x
            tile_y = u
            granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            x += 40
        x = 3640
        u -= 40
    x = 3680
    u = 680
    
    for i in range(5):
            tile_x = x
            tile_y = u
            granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            x += 150
            u -= 150
    x = 4320
    u = 760
    for i in range(19):
        tile_x = x
        tile_y = u
        granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
        u -= 40
    x = 4480
    u = 760
    for i in range(19):
        tile_x = x
        tile_y = u
        granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
        u -= 40
    x = 4520
    u = 160
    for i in range(2):
        tile_x = x
        tile_y = u
        granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
        x += 40
    x = 4600
    u = 160
    for i in range(2):
        tile_x = x
        tile_y = u
        granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
        x += 400
        u += 400
    x = 5150
    u = 370
    
    for i in range(2):
            tile_x = x
            tile_y = u
            granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            u -= 150
            x += 133
    x = 5483
    u = 370
    for i in range(2):
            tile_x = x
            tile_y = u
            granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            u -= 150
            x += 133
    x = 5816
    u = 370
    for i in range(2):
            tile_x = x
            tile_y = u
            granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            u -= 150
            x += 133
    x = 7480
    u = 780
    for i in range(2):
        for i in range(10):
            tile_x = x
            tile_y = u
            granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            u -= 40
        x += 200
        u = 780
    x = 7480
    u = 780
    for s in range(12):
        for i in range(6):
            tile_x = x
            tile_y = u
            granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            x += 40
        x = 7480
        u -= 40
    x = 9800
    u = 520
    for i in range(5):
            tile_x = x
            tile_y = u
            granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            u -= 120
    x = 9800
    u = 640
    for i in range(4):
        for s in range(5):
            tile_x = x
            tile_y = u
            granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            x += 80
        u -= 160
        x = 9800
    x = 10240
    u = 640
    for i in range(5):
            tile_x = x
            tile_y = u
            granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            u -= 120
    x = 12350
    u = 560
    for i in range(3):
        tile_x = x
        tile_y = u
        granit.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
        x += 700
    x = 14800
    u = 600
    for i in range(5):
        tile_x = x
        tile_y = u
        granit.append(( pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE)))
        x += 40
    x = 15000
    u = 760
    for i in range(50):
        tile_x = x
        tile_y = u
        granit.append(( pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE)))
        u -= 40
        



lave = []
def lave_mortelle():
    x = 240
    for i in range(3):
        tile_x = x
        tile_y = 760
        lave.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
        x += 40
    x = 560
    for i in range(2):
        tile_x = x
        tile_y = 760
        lave.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
        x += 40
    x = 720
    u = 760
    for s in range(2):
        for i in range(4):
            tile_x = x
            tile_y = u
            lave.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            x += 40
        x = 720
        u -= 40
    x = 960
    u = 760
    for s in range(4):
        for i in range(4):
            tile_x = x
            tile_y = u
            lave.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            x += 40
        x = 960
        u -= 40
    x = 1200
    u = 760
    for s in range(6):
        for i in range(6):
            tile_x = x
            tile_y = u
            lave.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            x += 40
        x = 1200
        u -= 40
    x = 1520
    u = 760
    for s in range(10):
        for i in range(6):
            tile_x = x
            tile_y = u
            lave.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            x += 40
        x = 1520
        u -= 40
    x = 3760
    u = 760
    for i in range(14):
        tile_x = x
        tile_y = u
        lave.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
        x += 40
    x = 1840
    u = 760
    for i in range(1):
        for s in range(45):
            tile_x = x
            tile_y = u
            lave.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            x += 40
        x = 1840
        u -= 40
    x = 4360
    u = 760
    for s in range(3):
        for i in range(19):
            tile_x = x
            tile_y = u
            lave.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            u -= 40
        x += 40
        u = 760
    x = 4520
    u = 760
    for s in range(74):
        tile_x = x
        tile_y = u
        lave.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
        x += 40
    x = 4640
    u = 200
    for i in range(3):
        tile_x = x
        tile_y = u
        lave.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
        x += 120
        u += 120
    x = 5100
    u = 460
    for s in range(11):
        tile_x = x
        tile_y = u
        lave.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
        x += 80.0005
    u = 70
    x = 5100
    for s in range(11):
        tile_x = x
        tile_y = u
        lave.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
        x += 80.0005
    x = 7480
    u = -65
    for i in range(2):
        for i in range(9):
            tile_x = x
            tile_y = u
            lave.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            u += 40
        x += 200
        u = -65
    x = 7480
    u = -65
    for s in range(9):
        for i in range(6):
            tile_x = x
            tile_y = u
            lave.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            x += 40
        x = 7480
        u += 40
    x = 9800
    u = 480
    for s in range(5):
        for i in range(2):
            tile_x = x
            tile_y = u
            lave.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            u -= 40
        u -= 40
    x = 10240
    u = 600
    for s in range(5):
        for i in range(2):
            tile_x = x
            tile_y = u
            lave.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
            u -= 40
        u -= 40
    x = 7720
    u = 760
    for i in range(182):
        tile_x = x
        tile_y = u
        lave.append(pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE))
        x += 40

variable = 0
disapperaing_tiles = []

def herbe():
    x = 6200
    u = 300
    for i in range(8):
        tile_x = x
        tile_y = u
        disapperaing_tiles.append(( pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE), 0))
        x += 40
    x = 6650
    u = 300
    for i in range(3):
        for i in range(2):
            tile_x = x
            tile_y = u
            disapperaing_tiles.append(( pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE), 0))
            x += 144
            u += 120
        u = 300
    x = 9840
    u = 640
    for i in range(4):
        for s in range(5):
            tile_x = x
            tile_y = u
            disapperaing_tiles.append((pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE), 0))
            x += 80
        u -= 160
        x = 9840
    x = 10640
    u = 180
    for i in range(4):
        tile_x = x
        tile_y = u
        disapperaing_tiles.append(( pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE), 0))
        x += 500
        u += 90
    x = 12550
    u = 460
    for i in range(3):
        for s in range(4):
            tile_x = x
            tile_y = u
            disapperaing_tiles.append(( pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE), 0))
            x += 120
            u -= 120
        u = 460
        x += 200
    x = 14800
    u = 720
    for i in range(5):
        tile_x = x
        tile_y = u
        disapperaing_tiles.append(( pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE), 0))
        x += 40
    
less_dangerous_lava = []
def dangerous_rocks():
    x = 7880
    u = 360
    for i in range(7):
        tile_x = x
        tile_y = u
        less_dangerous_lava.append(( pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE)))
        x += 220
        u -= 40
    x = 10400
    u = 120
    for i in range(4):
        tile_x = x
        tile_y = u
        less_dangerous_lava.append(( pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE)))
        x += 500
        u += 90
    x = 14400
    u = 250
    for i in range(3):
        tile_x = x
        tile_y = u
        less_dangerous_lava.append(( pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE)))
        x += 125
        u += 125
    x = 14800
    u = 680
    for i in range(5):
        tile_x = x
        tile_y = u
        less_dangerous_lava.append(( pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE)))
        x += 40

liste_random_tiles = []
def random_tiles():
    x = 9600
    u = 680
    
    for i in range(1):
        tile_x = x
        tile_y = u
        nn = random.choice([True, False])
        liste_random_tiles.append(( pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE), nn))
        x += 40
    x = 14800
    u = 640
    for i in range(5):
        tile_x = x
        tile_y = u
        nn = random.choice([True, False])
        print(nn)
        liste_random_tiles.append(( pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE), nn))
        x += 40
    x = 3665
    u = 290
    for i in range(1):
        tile_x = x
        tile_y = u
        nn = random.choice([True, False])
        liste_random_tiles.append(( pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE), nn))
    x = 9355
    u = 680
    for i in range(1):
        tile_x = x
        tile_y = u
        nn = random.choice([True, False])
        liste_random_tiles.append(( pygame.Rect(tile_x, tile_y, TILE_SIZE, TILE_SIZE), nn))



images = []
def images_cools():
    image_path = "C:/Users/Anis Djerrab/downloads/New Piskel.PNG"
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (50, 50))
    rect = image.get_rect(topleft=(50, 91))
    images.append((image, rect))

imges_utiles = []
def images_utils():
    image_path = "C:/Users/Anis Djerrab/downloads/New Piskel.PNG"
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (50, 50))
    rect = image.get_rect(topleft=(3660, 250))
    imges_utiles.append((image, rect))
    image_path = "C:/Users/Anis Djerrab/downloads/New Piskel.PNG"
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (50, 50))
    rect = image.get_rect(topleft=(9350, 640))
    imges_utiles.append((image, rect))

font = pygame.font.Font(None, 60)
def show_score(text, color, score):
    text_surface = font.render("Score", True, ORANGE)
    text_rect = text_surface.get_rect(center=(WHIDTH // 9, HIGHT // 14))
    screen.blit(text_surface, text_rect)
    pygame.display.update(text_rect)
    text_surface = font.render(text, True, color)
    text_rect2 = text_surface.get_rect(center=(WHIDTH // 8, HIGHT // 7))
    screen.blit(text_surface, text_rect2)
    pygame.display.update(text_rect2)
    text_surface = font.render(score, True, (0, 0, 255))
    text_rect2 = text_surface.get_rect(center=(WHIDTH // 4.625, HIGHT // 14))
    screen.blit(text_surface, text_rect2)
    pygame.display.update(text_rect2)
    
    return text_rect, text_rect2

"""pygame.mixer.music.load("C:/Users/Anis Djerrab/downloads/Slope Main Theme.mp3")
pygame.mixer.music.set_volume(0.75)
pygame.mixer.music.play(-1, 0.0)""" # link --> https://www.youtube.com/watch?v=Ylo3Kt9Feac


camera_offset_y = 0
camera_offset_x = 0
def main():
    global camera_offset_x, player_x, player_y, velocity_y, PLAYER_RADIUS, camera_offset_y, camera_offset_u, b, color, confirmation, GRAVITY, PLAYER_SPEED, JUMP, confirmation2, s, to_remov, disapperaing_tile
    clock = pygame.time.Clock()
    run = True
    camera_offset_u = camera_offset_x
    granit_rocks()
    lave_mortelle()
    herbe()
    dangerous_rocks()
    random_tiles()
    images_cools()
    images_utils()
    color = RED
    nombre = 5
    color = BLACK
    y = 0
    in_air = True
    x = 0
    confirmation = False
    liste = []
    s = 0
    for i in range(1, 100):
            liste.append(i)
    data = 0
    disapperaing_tile = {}
    to_remov = []
    confirmation2 = False
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        new_x, new_y = player_x, player_y
        
        

        if keys[pygame.K_UP] and in_air == True:
            new_y -= 120
            
        if keys[pygame.K_UP] and in_air == False:
            new_y -= 5
        if keys[pygame.K_LEFT]:
            new_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            new_x += PLAYER_SPEED
        if in_air == False:
            velocity_y += GRAVITY
            new_y += velocity_y
            if velocity_y > MAX_FALL_SPEED:
                    velocity_y = MAX_FALL_SPEED
        in_air = False

        

        player_x = max(PLAYER_RADIUS, min(player_x, WORLD_WEIDTH - PLAYER_RADIUS))
        player_y = max(PLAYER_RADIUS, min(player_y, WORLD_HEIGHT - PLAYER_RADIUS))
        camera_offset_x = max(0, min(player_x - WHIDTH // 2, WORLD_WEIDTH - WHIDTH))
        camera_offset_y = 0
        n = 0
        Background(n)

    
        
        player_x, player_y = new_x, new_y
        pygame.draw.circle(screen, CUSTOM_COLOR, (player_x - camera_offset_x, player_y - camera_offset_y), PLAYER_RADIUS)  


           
                
        player_rect = pygame.Rect(
            player_x - PLAYER_RADIUS,
            player_y - PLAYER_RADIUS,
            PLAYER_RADIUS * 2,
            PLAYER_RADIUS * 2,
        )
            
        for tile2 in granit:
            if player_rect.colliderect(tile2):
                delta_x = player_rect.centerx - tile2.centerx
                delta_y = player_rect.centery - tile2.centery
                
                
                if abs(delta_y) > abs(delta_x):  
                    if delta_y > 0:  
                        player_y = tile2.bottom + PLAYER_RADIUS
                        velocity_y = max(0, velocity_y)
                        
                    else:  
                        in_air = True
                        player_y = tile2.top - PLAYER_RADIUS
                        velocity_y = 0
                else: 
                    in_air = False
                    if delta_x > 0:  
                        player_x = tile2.right + PLAYER_RADIUS
                    else:  
                        player_x = tile2.left - PLAYER_RADIUS
            else:
                pass
        for tile2 in lave:
            if player_rect.colliderect(tile2):
                delta_x = player_rect.centerx - tile2.centerx
                delta_y = player_rect.centery - tile2.centery
                color = RED    
                confirmation = True

                if abs(delta_y) > abs(delta_x):  
                    if delta_y > 0: 
                        
                        player_y = tile2.bottom + PLAYER_RADIUS 
                        velocity_y = max(0, velocity_y)
                        
                    else:  
                        player_y = tile2.top - PLAYER_RADIUS 
                        velocity_y = 0
                        in_air = True
                
                else: 
                    in_air = False
                    if delta_x > 0:  
                        player_x = tile2.right + PLAYER_RADIUS 
                    else:  
                        player_x = tile2.left - PLAYER_RADIUS 
            else:
                pass

        to_remove = []

        for tile2 in granit:
            if player_rect.colliderect(tile2):
                delta_x = player_rect.centerx - tile2.centerx
                delta_y = player_rect.centery - tile2.centery
                
                
                if abs(delta_y) > abs(delta_x):  
                    if delta_y > 0:  
                        player_y = tile2.bottom + PLAYER_RADIUS
                        velocity_y = max(0, velocity_y)
                        
                    else:  
                        in_air = True
                        player_y = tile2.top - PLAYER_RADIUS
                        velocity_y = 0
                else: 
                    in_air = False
                    if delta_x > 0:  
                        player_x = tile2.right + PLAYER_RADIUS

                    else:  
                        player_x = tile2.left - PLAYER_RADIUS
            else:
                pass
        
        for i, item in enumerate(disapperaing_tiles):
                rect, horloge = item
                if player_rect.colliderect(rect):
                        horloge += 1
        
                        delta_x = player_rect.centerx - rect.centerx
                        delta_y = player_rect.centery - rect.centery
                        print(horloge)
                    
                        
            
                        if abs(delta_y) > abs(delta_x):  
                            if delta_y > 0: 
                                
                                player_y = rect.bottom + PLAYER_RADIUS 
                                velocity_y = max(0, velocity_y)
                                
                            else:  
                                player_y = rect.top - PLAYER_RADIUS 
                                velocity_y = 0
                                in_air = True
                        
                        else: 
                            in_air = False
                            if delta_x > 0:  
                                player_x = rect.right + PLAYER_RADIUS 
                            else:  
                                player_x = rect.left - PLAYER_RADIUS 

                        if horloge >= 5:
                            to_remove.append(i)
                disapperaing_tiles[i] = (rect, horloge)
        
        for index in sorted(to_remove, reverse=True):
            del disapperaing_tiles[index]
        
        for tile2 in granit:
            if player_rect.colliderect(tile2):
                delta_x = player_rect.centerx - tile2.centerx
                delta_y = player_rect.centery - tile2.centery
                
                
                if abs(delta_y) > abs(delta_x):  
                    if delta_y > 0:  
                        player_y = tile2.bottom + PLAYER_RADIUS
                        velocity_y = max(0, velocity_y)
                        
                    else:  
                        in_air = True
                        player_y = tile2.top - PLAYER_RADIUS
                        velocity_y = 0
                else: 
                    in_air = False
                    if delta_x > 0:  
                        player_x = tile2.right + PLAYER_RADIUS
                    else:  
                        player_x = tile2.left - PLAYER_RADIUS
            else:
                pass
        
        for hot in less_dangerous_lava:
                if player_rect.colliderect(hot):
        
                        delta_x = player_rect.centerx - hot.centerx
                        delta_y = player_rect.centery - hot.centery
                    
                        rando = random.choice(range(0, 4))
                        if rando == 0:
                            confirmation = True
                            color = DARK_RED
                        else:
                            pass
            
                        if abs(delta_y) > abs(delta_x):  
                            if delta_y > 0: 
                                
                                player_y = hot.bottom + PLAYER_RADIUS 
                                velocity_y = max(0, velocity_y)
                                
                            else:  
                                player_y = hot.top - PLAYER_RADIUS 
                                velocity_y = 0
                                in_air = True
                        
                        else: 
                            in_air = False
                            if delta_x > 0:  
                                player_x = hot.right + PLAYER_RADIUS 

                            else:  
                                player_x = hot.left - PLAYER_RADIUS 
        for stuff, criteria in liste_random_tiles:
                if player_rect.colliderect(stuff):
                    if criteria == True:
                        delta_x = player_rect.centerx - stuff.centerx
                        delta_y = player_rect.centery - stuff.centery
                    
            
                        if abs(delta_y) > abs(delta_x):  
                            if delta_y > 0: 
                                
                                player_y = stuff.bottom + PLAYER_RADIUS 
                                velocity_y = max(0, velocity_y)
                                
                            else:  
                                player_y = stuff.top - PLAYER_RADIUS 
                                velocity_y = 0
                                in_air = True
                        
                        else: 
                            in_air = False
                            if delta_x > 0:  
                                player_x = stuff.right + PLAYER_RADIUS 

                            else:  
                                player_x = stuff.left - PLAYER_RADIUS

        for w, (rr, rectgle) in enumerate(imges_utiles):
                if player_rect.colliderect(rectgle):
                        delta_x = player_rect.centerx - rectgle.centerx
                        delta_y = player_rect.centery - rectgle.centery      
                        rect_affiche.x -= 2000
                        del imges_utiles[w]
                        nombre += 1
                        break

                              
                            
        if confirmation == True:
            x += 1
            y += 1
            data = 0
            if y == 5:
                    nombre -= 1
            if y == 10:
                    nombre -= 1
            if y  == 15:
                    nombre -= 1
            if y  == 20:
                    nombre -= 1
            if y  == 25:
                    nombre -= 1  
            if y == 30:
                nombre -= 1
            if y == 35:
                nombre -= 1
        else:
            data += 1
            if data == 60:
                data = 0   
                color = BLACK
        
        for tile in granit:
            pygame.draw.rect(screen, BLACK, (tile.x - camera_offset_x, tile.y - camera_offset_y, TILE_SIZE, TILE_SIZE), border_radius=3)
        
        for ite, _ in disapperaing_tiles:
            pygame.draw.rect(screen, GREEN, (ite.x - camera_offset_x, ite.y - camera_offset_y, TILE_SIZE, TILE_SIZE), border_radius=3)


        for chose in lave:
            pygame.draw.rect(screen, DARK_RED, (chose.x - camera_offset_x, chose.y - camera_offset_y, TILE_SIZE, TILE_SIZE), border_radius=3)
        
        for thing_2 in less_dangerous_lava:
            pygame.draw.rect(screen, DARK_DARK_RED, (thing_2.x - camera_offset_x, thing_2.y - camera_offset_y, TILE_SIZE, TILE_SIZE), border_radius=3)

        for stuff, _ in liste_random_tiles:
            pygame.draw.rect(screen, BLUE, (stuff.x - camera_offset_x, stuff.y - camera_offset_y, TILE_SIZE, TILE_SIZE), border_radius=3)

        for photo, rectangle in images:
            screen.blit(photo, rectangle)
        
        for image, rect in imges_utiles:
            rect_affiche = rect.copy()
            rect_affiche.x -= camera_offset_x
            screen.blit(image, rect_affiche)
            
        score_to_show = player_x//100
        if s < score_to_show:
            pass
        else:
            score_to_show = s
        show_score(str(nombre), color, str(score_to_show))
        s = score_to_show
        confirmation = False

        if nombre == 0:
            pygame.mixer.music.stop()
            winsound.Beep(500, 500)
            font3 = pygame.font.Font(None, 200)
            text_surface = font3.render(f"""GAME OVER!""", True, DARK_DARK_RED)
            text_rect = text_surface.get_rect(center=(WHIDTH // 2, HIGHT // 4))
            screen.blit(text_surface, text_rect)
            pygame.display.update(text_rect)
            font4 = pygame.font.Font(None, 100)
            text_surface = font4.render(f"""Best score: {player_x//100}""", True, DARK_DARK_RED)
            text_rect = text_surface.get_rect(center=(WHIDTH // 2, HIGHT // 1.6))
            screen.blit(text_surface, text_rect)
            pygame.display.update(text_rect)
            time.sleep(3)
            break

        if player_x > 14900 or player_x == 14900:
            pygame.mixer.music.stop()
            winsound.Beep(500, 500)
            font3 = pygame.font.Font(None, 200)
            text_surface = font3.render(f"""YOU WON!""", True, BLUE)
            text_rect = text_surface.get_rect(center=(WHIDTH // 2, HIGHT // 4))
            screen.blit(text_surface, text_rect)
            pygame.display.update(text_rect)
            font4 = pygame.font.Font(None, 100)
            text_surface = font4.render(f"""Best Score: {player_x//100}""", True, BLUE)
            text_rect = text_surface.get_rect(center=(WHIDTH // 2, HIGHT // 1.6))
            screen.blit(text_surface, text_rect)
            pygame.display.update(text_rect)
            time.sleep(3)
            break
        
        pygame.display.flip()
    pygame.quit()

if __name__=="__main__":
    main()