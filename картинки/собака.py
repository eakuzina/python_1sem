import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 800))

rect(screen, (64,245, 255), (0, 0, 500, 150))
rect(screen, (255,179, 64), (0, 150, 500, 450))
rect(screen, (115,255, 64), (0, 450, 500, 800))
line(screen, 'black',(0,450),(500,450), 3)
line(screen, 'black',(40,450),(40,150), 3)
line(screen, 'black',(80,450),(80,150), 3)
line(screen, 'black',(120,450),(120,150), 3)
line(screen, 'black',(160,450),(160,150), 3)
line(screen, 'black',(200,450),(200,150), 3)
line(screen, 'black',(240,450),(240,150), 3)
line(screen, 'black',(280,450),(280,150), 3)
line(screen, 'black',(320,450),(320,150), 3)
line(screen, 'black',(360,450),(360,150), 3)
line(screen, 'black',(400,450),(400,150), 3)
line(screen, 'black',(440,450),(440,150), 3)
line(screen, 'black',(480,450),(480,150), 3)

# будка
polygon(screen, "black", [(350, 550), (350, 650), (450, 650), (450, 550)])
polygon(screen, (139, 69, 19), [(352, 552), (352, 648), (448, 648), (448, 552)])

# крыша
polygon(screen, "black", [(340, 550), (400, 500), (460, 550)])
polygon(screen, (178, 34, 34), [(342, 548), (400, 502), (458, 548)])

# Вход в будку
circle(screen, "black", (400, 600), 25)
circle(screen, (0, 0, 0, 0), (400, 600), 23)
circle(screen, (115, 255, 64), (400, 600), 23)

# Собака 
# Тело
ellipse(screen, (150, 150, 150), (280, 580, 120, 60))
# Голова
ellipse(screen, (150, 150, 150), (390, 570, 60, 50))
# Уши
polygon(screen, (150, 150, 150), [(400, 570), (390, 550), (410, 565)])
polygon(screen, (150, 150, 150), [(440, 570), (450, 550), (430, 565)])
# Лапы
ellipse(screen, (150, 150, 150), (290, 630, 30, 40))
ellipse(screen, (150, 150, 150), (350, 630, 28, 40))
# Хвост
polygon(screen, (150, 150, 150), [(400, 590), (420, 570), (410, 610)])
# Глаза
circle(screen, "black", (410, 585), 4)
circle(screen, "black", (430, 585), 4)
# Нос
circle(screen, "black", (445, 590), 5)
# Пасть
line(screen, "black", (425, 600), (440, 600), 3)

# Ошейник(повязка)
rect(screen, "red", (395, 568, 50, 8))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()