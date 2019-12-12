import pygame
import random
import time
from sys import exit
pygame.init()

valge = (255, 255, 255)
must = (0, 0, 0)
punane = (255, 0, 0)
roheline = (0, 255, 0)
sinine = (0, 0, 255)

pygame.display.set_caption("Mäng")

clock = pygame.time.Clock()

kõik_vastased = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

kiirus = 15
x=300
y=550

class mängija(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((30, 30))
        self.image.fill(sinine)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.kiirus = 15
             

class vastane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
       
        self.image = pygame.Surface((30, 30))
        self.image.fill(punane)
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(0, 150)
        self.rect.x = random.randrange(0, 580)
        
    def update(self):
        self.rect.y += 10
        if self.rect.y > ekraanikõrgus:
            self.uus_positsioon()
    def uus_positsioon(self): 
        self.rect.y = random.randrange(0, 150)
        self.rect.x = random.randrange(10, 580)

for i in range(18):
    
    vast = vastane()

    kõik_vastased.add(vast)

mängija1 = mängija()
all_sprites.add(mängija1)

ekraanilaius = 600
ekraanikõrgus = 600

aken = pygame.display.set_mode((ekraanilaius, ekraanikõrgus))


run=True
while run:
    pygame.time.delay(100)
    nooled=pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    
    if nooled[pygame.K_LEFT] and mängija1.rect.x > mängija1.kiirus:
        mängija1.rect.x -=mängija1.kiirus
    if nooled[pygame.K_RIGHT] and mängija1.rect.x < ekraanilaius - 30 - mängija1.kiirus:
        mängija1.rect.x += mängija1.kiirus
        
    aken.fill((0, 0, 0))
    
    
        
    kõik_vastased.update()
    kõik_vastased.draw(aken)
    all_sprites.update()
    all_sprites.draw(aken)
    
    pygame.display.update()
    
    clock.tick(60)
    
    if pygame.sprite.collide_rect(mängija1, vast):
                pygame.quit()
                exit()

pygame.quit()