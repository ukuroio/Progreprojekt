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

ekraanilaius = 600
ekraanikõrgus = 600

pygame.display.set_caption("Mäng")

clock = pygame.time.Clock()

kõik_vastased = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

x=300
y=570

font = pygame.font.SysFont('Comic Sans MS', 30)

def skoor(skoor):
    skoor = pygame.time.get_ticks()
    tekst = font.render("Skoor: "+str(skoor), True, valge)
    aken.blit(tekst, [0,0])
      
class mängija(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(sinine)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.kiirus = 9
        
class vastane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(punane)
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(0, 200)
        self.rect.x = random.randrange(0, 700)
    def update(self):
        self.rect.y += 4
        if self.rect.y > ekraanikõrgus:
            self.uus_positsioon()
    def uus_positsioon(self): 
        self.rect.y = random.randrange(0, 170)
        self.rect.x = random.randrange(10, 700)
        
mängija1 = mängija()
all_sprites.add(mängija1)

for i in range(15):
    vast = vastane()
    all_sprites.add(vast)
    kõik_vastased.add(vast)

aken = pygame.display.set_mode((ekraanilaius, ekraanikõrgus))

run=True
while run:
    
    pygame.time.delay(10)
    nooled=pygame.key.get_pressed()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    
    if nooled[pygame.K_LEFT] and mängija1.rect.x > mängija1.kiirus:
        mängija1.rect.x -=mängija1.kiirus
    if nooled[pygame.K_RIGHT] and mängija1.rect.x < ekraanilaius - 30 - mängija1.kiirus:
        mängija1.rect.x += mängija1.kiirus
        
    aken.fill((0, 0, 0))
    
    all_sprites.update()
    
    collision = pygame.sprite.spritecollide(mängija1, kõik_vastased, False)
    if collision:
        #tekst1 = font.render("Tulemus: ",str(skoor) + True, valge)
        #pygame.time.wait(5000)
        #aken.blit(tekst1, [300,300]) 
        run = False
        
    all_sprites.draw(aken)
    
    #kõik_vastased.update()
    #kõik_vastased.draw(aken)
    
    skoor(skoor)
    pygame.display.update()
    
    clock.tick(60)
    
pygame.quit()