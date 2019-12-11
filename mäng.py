import pygame
import random
pygame.init()

valge = (255, 255, 255)
must = (0, 0, 0)
punane = (255, 0, 0)
roheline = (0, 255, 0)
sinine = (0, 0, 255)

pygame.display.set_caption("Mäng")

clock = pygame.time.Clock()

kõik_vastased = pygame.sprite.Group()

class vastane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(punane)
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(0, 100)
        self.rect.x = random.randrange(0, 500)
    def update(self):
        self.rect.y += 10
        if self.rect.y > ekraanikõrgus:
            self.uus_positsioon()
    def uus_positsioon(self): 
        self.rect.y = random.randrange(0, 100)
        self.rect.x = random.randrange(10, 490)


for i in range(15):
    
    vast = vastane()

    kõik_vastased.add(vast)



ekraanilaius = 500
ekraanikõrgus = 500

aken = pygame.display.set_mode((ekraanilaius, ekraanikõrgus))

kiirus = 15
x=250
y=450

run=True
while run:
    pygame.time.delay(100)
    nooled=pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    
    if nooled[pygame.K_LEFT] and x > kiirus:
        x -=kiirus
    if nooled[pygame.K_RIGHT] and x < ekraanilaius - 40 - kiirus:
        x += kiirus
    if nooled[pygame.K_DOWN] and y < ekraanikõrgus- 70 -kiirus:
        y +=kiirus
        
    aken.fill((0, 0, 0))
    
    pygame.draw.rect(aken,(131, 234, 255), (x, y, 30, 30)) 
   
    kõik_vastased.update()
    kõik_vastased.draw(aken)
    pygame.display.update()
    clock.tick(27)
    pygame.display.flip()
    

pygame.quit()