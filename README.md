# Lukian-Vorobetsimport pygame
from pygame import *
from random import randint
pygame.init()

back = (200,255,255)
win_width = 700
win_height = 500
display.set_caption("пінгпонг")
window = pygame.display.set_mode((700,500))
window.fill(back)

class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)

        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # метод, що малює героя у вікні
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# клас головного гравця
class Player(GameSprite):
    # метод для керування спрайтом стрілками клавіатури
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

class Play(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed


Ball = GameSprite("ball.jpg", 100,200,100,30,4)

racket_x = 200
racket_y = 430

racket = Player("racket.png", racket_x,racket_y ,200,14,4)
racketet = Play("racket.png", 200,70,200,14,4)

speed_x = 4
speed_y = 4

move_right = False
move_left = False

game = True
finish = False
clock = time.Clock()
FPS = 40

font1 = font.Font(None, 35)
lose1 = font1.render(
    'PLAYER 1 LOSE!', True, (180, 0, 0))
font1 = font.Font(None, 35)
lose2 = font1.render(
    'PLAYER 2 LOSE!', True, (180, 0, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        Ball.rect.x += speed_x
        Ball.rect.y += speed_y

        window.fill(back)
        racket.update()
        racketet.update()
        Ball.update()
        Ball.reset()
        racketet.reset()
        racket.reset()


    if Ball.rect.y < 0:
        speed_y *= -1
    if Ball.rect.x > 600 or Ball.rect.x < 0:
        speed_x *= -1

    if Ball.rect.colliderect(racket.rect):
        speed_y *= -1
    if Ball.rect.colliderect(racketet.rect):
        speed_y *= -1

    if Ball.rect.y > racket_y + 20:
        finish = True
        window.blit(lose1, (200, 200))
    if Ball.rect.y < 20:
        finish = True
        window.blit(lose2, (200, 200))

    display.update()
    clock.tick(40)
