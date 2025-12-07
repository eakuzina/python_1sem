
import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
FCOLORS = [WHITE]

nb = 4 #количество шариков
score = 0  # подсчет очков
nfb = 2 #количество ложных шаров

speed = [] #список векторов скоростей
coord= [] #список координат
r = [] #список радиусов
colors = [] #список цветов

# создаём новый шар
def new_fball():
    coord.append( [randint(100, 1100), randint(100, 600)] )
    r.append( randint(20, 45) )
    colors.append( FCOLORS[0])
    speed.append( [randint(-5, 5), randint(-5, 5)] )
def new_ball():
    coord.append( [randint(100, 1100), randint(100, 600)] )
    r.append( randint(20, 45) )
    colors.append( COLORS[randint(0, 5)] )
    speed.append( [randint(-5, 5), randint(-5, 5)] )




# проверка попадания,замена на новый в случае попадания
def click(event):
    global score
    for i in range(nb):
        if (coord[i][0]-event.pos[0])**2+(coord[i][1]-event.pos[1])**2 <= (r[i])**2:
            score += 1
            coord[i] = [randint(100, 1100), randint(100, 600)]
            r[i] = randint(20, 45)
            speed[i] = [randint(-5, 5), randint(-5, 5)]
            colors[i] = COLORS[randint(0, 5)]
            break
    for i in range(nfb):
        if (coord[i][0]-event.pos[0])**2+(coord[i][1]-event.pos[1])**2 <= (r[i])**2:
            score -= 1
            coord[i] = [randint(100, 1100), randint(100, 600)]
            r[i] = randint(20, 45)
            speed[i] = [randint(-5, 5), randint(-5, 5)]
            colors[i] = FCOLORS[0]
            break

# функция двигает шары:
# 1.1)при косании боковых стен меняет координату X вектора скорости на противоположную
# 1.2)при косании верхней или нижней стены меняет координату Y вектора скорости на противоположную
# 2) рисует все шары на новых позициях в зависимости от векторов их скоростей
def moveb(screen): 
    for i in range(nb):
        if coord[i][0]+r[i] >= 1200 or coord[i][0]-r[i] <= 0:
            speed[i][0] *= -1
        if coord[i][1]+r[i] >= 700 or coord[i][1]-r[i] <= 0:
            speed[i][1] *= -1
        coord[i][0] += speed[i][0]
        coord[i][1] += speed[i][1]
        circle(screen, colors[i], (coord[i][0], coord[i][1]), r[i])
for i in range(nb):
    new_ball()

def movefb(screen): 
    for i in range(nfb):
        if coord[i][0]+r[i] >= 1200 or coord[i][0]-r[i] <= 0:
            speed[i][0] *= -1
        if coord[i][1]+r[i] >= 700 or coord[i][1]-r[i] <= 0:
            speed[i][1] *= -1
        coord[i][0] += speed[i][0]
        coord[i][1] += speed[i][1]
        circle(screen, colors[i], (coord[i][0], coord[i][1]), r[i])

for i in range(nfb):
    new_fball()
finished = False
while not finished:
    pygame.time.Clock().tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event) # проверяем, попали ли мы в круг

    movefb(screen)
    moveb(screen)

    screen.blit(pygame.font.Font(None,50).render(str(score),True,(255, 255, 255)), (10, 10)) #выводим кол-во попаданий
    pygame.display.update()
    screen.fill(BLACK)        

pygame.quit()
