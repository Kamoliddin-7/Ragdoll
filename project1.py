import pygame

pygame.init()
screen = pygame.display.set_mode((1500, 770))
pygame.display.set_caption("Add shapes and gravity")
clock = pygame.time.Clock()
running = True

gravity = 0.1
left, right, floor, ceil = 300, 500, 700, 300
x,y = 400, 300
vx,vy = 5, 0
r = 10


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if y>floor-1.1*r:
        y=floor-r
        vy = -vy*0.9
        vx = vx*0.9
        if abs(vy)<2*gravity:
            vy = 0
            y = floor-r
        if abs(vx)<2*gravity:
            vx = 0
    else:
        vy += gravity
    if x<=left+r:
        x=left+r
        vx = -vx*0.9
    if x>=right-r:
        x=right-r
        vx = -vx*0.9

    x += vx
    y += vy

    screen.fill((0,0,50))
    pygame.draw.circle(screen,"orange",(x,y),10)
    pygame.draw.line(screen,"white",(left,ceil),(left,floor),5)
    pygame.draw.line(screen,"white",(right,ceil),(right,floor),5)
    pygame.draw.line(screen,"white",(left,floor),(right,floor),5)
    pygame.display.flip()
    clock.tick(120)

pygame.quit()