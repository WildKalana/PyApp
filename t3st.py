import pygame
pygame.init()

win = pygame.display.set_mode((700, 700))

pygame.display.set_caption("Testicle")

#walkRight = [pygame.image.load("Sprites/PNG/Players/p1_walk11.png"), pygame.image.load("Sprites/PNG/Players/p1_walk07.png"), pygame.image.load("Sprites/PNG/Players/p1_walk06.png"), pygame.image.load("Sprites/PNG/Players/p1_walk05.png"), pygame.image.load("Sprites/PNG/Players/p1.walk04.png"), pygame.image.load("Sprites/PNG/Players/p1_walk03.png"), pygame.image.load("Sprites/PNG/Players/p1.walk02.png"), pygame.image.load("Sprites/PNG/Players/p1_walk01.png")
#walkLeft = [pygame.image.load("Sprites/PNG/Players/walk_left1.png"), pygame.image.load("Sprites/PNG/Players/walk_left2.png"), pygame.image.load("Sprites/PNG/Players/walk_left3.png"), pygame.image.load("Sprites/PNG/Players/walk_left4.png"), pygame.image.load("Sprites/PNG/Players/walk_left5.png"), pygame.image,load("Sprites/PNG/Players/walk_left6.png"), pygame.image.load("Sprites/PNG/Players/walk_left7.png"), pygame.image.load("Sprites/PNG/Players/walk_left8.png")
bg = pygame.image.load("Desktop/Sprites/PNG/Backgrounds/blue_grass.png")
char = pygame.image.load("p1_walk10.png")

x = 50
y = 425
width = 64
height = 64
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    
    win.blit(bg, (0,0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    pygame.display.update()

run = True 
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 700 - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
    if not(isJump) :
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount< 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    
    redrawGameWindow()

pygame.quit()    