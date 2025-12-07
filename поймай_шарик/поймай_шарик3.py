#при нажатии получается новый шарик
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
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

number_of_balls = 9
score = 0  # подсчет очков

# соответственно списки векторов скоростей, координат, радиусов и цветов шаров
vector_of_speed = []
coordinates = []
radiuses = []
colours = []

# создаёт и записывает параметры нового шара в массив шаров
def new_ball():
    coordinates.append( [randint(100, 1100), randint(100, 600)] )
    radiuses.append( randint(20, 45) )
    colours.append( COLORS[randint(0, 5)] )
    vector_of_speed.append( [randint(-5, 5), randint(-5, 5)] )

# проверка на попадание в шар, и замена на новый в случае попадания
def click(event):
    global score
    for i in range(number_of_balls):
        if (coordinates[i][0]-event.pos[0])**2+(coordinates[i][1]-event.pos[1])**2 <= (radiuses[i])**2:
            score += 1
            coordinates[i] = [randint(100, 1100), randint(100, 600)]
            radiuses[i] = randint(20, 45)
            vector_of_speed[i] = [randint(-5, 5), randint(-5, 5)]
            colours[i] = COLORS[randint(0, 5)]
            break

# функция двигает шары:
# 1.1)при косании боковых стен меняет координату X вектора скорости на противоположную
# 1.2)при косании верхней или нижней стены меняет координату Y вектора скорости на противоположную
# 2) рисует все шары на новых позицияч в зависимости от векторов их скоростей
def move_balls(screen):
    for i in range(number_of_balls):
        if coordinates[i][0]+radiuses[i] >= 1200 or coordinates[i][0]-radiuses[i] <= 0:
            vector_of_speed[i][0] *= -1
        if coordinates[i][1]+radiuses[i] >= 700 or coordinates[i][1]-radiuses[i] <= 0:
            vector_of_speed[i][1] *= -1
        coordinates[i][0] += vector_of_speed[i][0]
        coordinates[i][1] += vector_of_speed[i][1]
        circle(screen, colours[i], (coordinates[i][0], coordinates[i][1]), radiuses[i])

for i in range(number_of_balls):
    new_ball()

finished = False

while not finished:
    pygame.time.Clock().tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    move_balls(screen)

    screen.blit(pygame.font.Font(None,50).render(str(score),True,(255, 255, 255)), (10, 10)) #выводим кол-во попаданий
    pygame.display.update()
    screen.fill(BLACK)        # заливаем все чёрным чтобы замазать предыдущие позиции шаров

pygame.quit()