# 3 цели двигаются
import math
from random import choice, randint as rnd 
 
import pygame
 
FPS = 30
 
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [ BLUE, YELLOW, GREEN, MAGENTA, CYAN]
 
WIDTH = 800
HEIGHT = 600
 
class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball
 
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 1
        self.grav = 0.5 #  гравитация

    def move(self):
        """Переместить мяч по прошествии единицы времени.
 
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME -   гравитация и отскок от стен
        self.vy -= self.grav
        self.x += self.vx
        self.y -= self.vy
        
        # Отскок от стен
        if self.x + self.r > WIDTH or self.x - self.r < 0:
            self.vx = -self.vx * 0.8
            if self.x + self.r > WIDTH:
                self.x = WIDTH - self.r
            else:
                self.x = self.r
                
        if self.y + self.r > HEIGHT:
            self.vy = -self.vy * 0.8
            self.vx *= 0.9
            self.y = HEIGHT - self.r
            if abs(self.vy) < 1:
                self.vy = 0

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
 
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME -  проверка столкновения
        distance = math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)
        return distance <= self.r + obj.r
 
class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = 20 # координаты пушки
        self.y = 450

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
 
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, self.x, self.y) # передача координат пушки
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        # FIXIT  рисуется пушка
        gun_length = 20 + self.f2_power / 2
        end_x = self.x + gun_length * math.cos(self.an)
        end_y = self.y + gun_length * math.sin(self.an)
        
        pygame.draw.line(
            self.screen,
            self.color,
            (self.x, self.y),
            (end_x, end_y),
            7
        )
        
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            10
        )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY
 
class Target:
    # self.points = 0
    # self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()
    
    def __init__(self):
        # инициализация
        self.screen=screen
        self.points = 0
        self.live = 1
        self.vx = 0
        self.vy = 0
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = RED
    # Случайная начальная скорость
        self.vx = rnd(-5, 5)
        self.vy = rnd(-5, 5)
        
        # Гарантируем минимальную скорость
        if abs(self.vx) < 2:
            self.vx = 2 if self.vx >= 0 else -2
        if abs(self.vy) < 2:
            self.vy = 2 if self.vy >= 0 else -2
            

    def move(self):
        """Переместить цель по прошествии единицы времени."""
        if self.live:
            self.x += self.vx
            self.y += self.vy
            # Отскок от границ экрана
            if self.x + self.r > WIDTH or self.x - self.r < 0:
                self.vx = -self.vx
                # Корректировка позиции, чтобы не застревать в стене
                if self.x + self.r > WIDTH:
                    self.x = WIDTH - self.r
                else:
                    self.x = self.r
                    
            if self.y + self.r > HEIGHT or self.y - self.r < 0:
                self.vy = -self.vy
                # Корректировка позиции
                if self.y + self.r > HEIGHT:
                    self.y = HEIGHT - self.r
                else:
                    self.y = self.r

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        # FIXME - рисуется цель
        if self.live:
            pygame.draw.circle(self.screen, self.color,(self.x, self.y),self.r)
 
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
score = 0 # Счетчик очков
font = pygame.font.Font(None, 36) # Шрифт для отображения счета

clock = pygame.time.Clock()
gun = Gun(screen)
# Создаем несколько движущихся мишеней
targets = []
for i in range(3): # Создаем 3 мишени
    target = Target()
    targets.append(target)
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    # Двигаем и рисуем все мишени
    for target in targets:
        target.move()
        target.draw()
    
    for b in balls:
        b.draw()
    
    # Отображаем счет
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
 

    for b in balls:
        b.move()
        b.live-=1
        # Проверяем столкновение с мишенями
        for target in targets:
            if b.hittest(target) and target.live:
                target.live = 0
                target.hit()
                score += 1 # Увеличиваем счет
                # Создаем новую мишень через короткую задержку
                pygame.time.delay(100)
                target.new_target()
    gun.power_up()

pygame.quit()
