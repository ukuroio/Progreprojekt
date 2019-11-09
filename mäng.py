import pygame
pygame.init()

aken = pygame.display.set_mode((500, 500))
kiirus = 10
pygame.display.set_caption("Mäng")
x=100
y=100

run=True
while run:
    pygame.time.delay(100)
    nooled=pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    
    if nooled[pygame.K_LEFT]:
        x -=kiirus
    if nooled[pygame.K_RIGHT]:
        x += kiirus
    if nooled[pygame.K_UP]:
        y -=kiirus
    if nooled[pygame.K_DOWN]:
        y +=kiirus
    aken.fill((0, 0, 0))
    pygame.draw.rect(aken,(131, 234, 255), (x, y, 40, 70))
    pygame.display.update()


pygame.quit()