import pygame
from pygame.draw import *
from random import uniform,randint

pygame.init()
screen = pygame.display.set_mode((600, 850))

#земля
rect(screen, (30, 40, 0), (0, 500, 600, 400))
#небо
rect(screen, (0, 30, 40), (0, 0, 600, 500))
#солнце
circle(screen, (255, 255, 255), (420, 250), 100)
#светлые облака
for i in [(400, -5, 400, 100), (-240, 50, 600, 170), (300, 160, 600, 100), (-200, 255, 620, 110), (240, 290, 600, 130)]:
    ellipse(screen,(100,100,100),i)
#тёмные облака
for i in [(150, 360, 500, 100), (140, 105, 500, 90), (-150, 215, 450, 105)]:
    ellipse(screen,(50,50,50),i)

#заяц с яблоком
def zajac(x,y,size,orientation):
    z_surface=pygame.Surface((200*size,300*size),pygame.SRCALPHA)

    for i in [((18, 10), 10),((29, 280), 12),((100, 285), 12),((48, 145), 14),((38, 165), 10),((35, 175), 6),
              ((113, 145), 14),((128, 165), 10),((143, 175), 6),((43, 50), 7),((40, 37), 8),((33, 22), 9),
              ((138, 50), 7),((148, 39), 8),((162, 35), 9),((183, 35), 10), ((25, 175), 6)]:
        circle(z_surface,(255, 255, 200),(i[0][0]*size,i[0][1]*size),i[1]*size)

    for i in [(48, 125, 70, 120), (38, 205, 25, 45), (38, 235, 15, 50), (98, 215, 25, 45),
              (108, 240, 15, 50), (0, 175, 20, 9), (148, 175, 20, 9), (78, 115, 15, 20)]:
        ellipse(z_surface,(255,255,200),(i[0]*size, i[1]*size, i[2]*size, i[3]*size))

    polygon(z_surface, (255, 255, 200), [(43*size, 55*size), (88*size, 125*size), (133*size, 55*size)])

    for i in [((0, 0, 0), (75, 75), 14),((0, 0, 0), (107, 75), 11),((255, 255, 255), (77, 78), 3),
              ((255, 255, 255), (109, 78), 3),((255, 50, 50), (168, 155), 20)]:
        circle(z_surface,i[0],(i[1][0]*size,i[1][1]*size),i[2]*size)

    ellipse(z_surface, (100, 255, 150), (178*size, 123*size, 20*size, 9*size))
    polygon(z_surface, (0, 0, 0), [(168*size, 135*size), (178*size, 125*size)], 2)

    screen.blit(pygame.transform.flip(z_surface, orientation, False),(x,y))

#тарелка
def ship(x,y,size):
    ship_surface=pygame.Surface((250*size,210*size),pygame.SRCALPHA)
    #прожектор
    polygon(ship_surface, (255, 255, 255, 100), [(9*size, 208*size), (120*size, 0*size), (232*size, 208*size)])
    #основная часть
    ellipse(ship_surface, (150, 150, 150), (0*size, 10*size, 250*size, 90*size))
    ellipse(ship_surface, (200, 200, 200), (35*size, 0, 180*size, 65*size))
    #белые элипсы
    for i in [(8, 46, 35, 15), (40, 65, 35, 15), (81, 75, 35, 15), (129, 75, 35, 15), (170, 65, 35, 15), (205, 50, 35, 15)]:
        ellipse(ship_surface,(255,255,255),(i[0]*size,i[1]*size,i[2]*size,i[3]*size))

    screen.blit(ship_surface, (x, y))

zajac(randint(20,100),randint(450,650),uniform(0.2,1.2),randint(1,2)==1)
ship(randint(0,550),randint(350,400),uniform(0.6,1.5))

pygame.display.update()
finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()