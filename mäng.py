import pygame
import random
pygame.init()

valge = (255, 255, 255)
must = (0, 0, 0)
punane = (255, 0, 0)
roheline = (0, 255, 0)
sinine = (0, 0, 255)

pygame.display.set_caption("Mäng")

kõik_vastased = pygame.sprite.Group()

class vastane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(punane)
        self.rect = self.image.get_rect() 
        self.rect.y = random.randrange(0, 100) #random koht kus see ruut spawnib
        self.rect.x = random.randrange(0, 500)
    def update(self):
        self.rect.y += 5
        if self.rect.y > ekraanikõrgus:
            self.uus_positsioon()
    def uus_positsioon(self): # saadab ruudu tagasi üles kui see mapist alla kukub
        self.rect.y = random.randrange(0, 100)
        self.rect.x = random.randrange(0, 500)
        
vast = vastane()
kõik_vastased.add(vast) # lisab ruudu sprite gruppi

ekraanilaius = 500
ekraanikõrgus = 500

aken = pygame.display.set_mode((ekraanilaius, ekraanikõrgus))

kiirus = 10
x=250
y=410

run=True
while run:#peatsükkel
    pygame.time.delay(100)
    nooled=pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    
    if nooled[pygame.K_LEFT] and x > kiirus:#piirid ja nupud
        x -=kiirus
    if nooled[pygame.K_RIGHT] and x < ekraanilaius - 40 - kiirus:
        x += kiirus
    if nooled[pygame.K_UP] and y > kiirus:
        y -=kiirus
    if nooled[pygame.K_DOWN] and y < ekraanikõrgus- 70 -kiirus:
        y +=kiirus
        
    aken.fill((0, 0, 0))
    pygame.draw.rect(aken,(131, 234, 255), (x, y, 40, 70))#peategelane
    
    kõik_vastased.update()
    kõik_vastased.draw(aken)
    pygame.display.update()
    pygame.display.flip()
    

pygame.quit()