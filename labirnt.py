
from pygame import *
import pygame

pygame.init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
   def update(self):
      keys = key.get_pressed()
      if keys[K_LEFT] and self.rect.x > 5:
         self.rect.x -= self.speed
      if keys[K_RIGHT] and self.rect.x < win_width - 90:
         self.rect.x += self.speed
      if keys[K_UP] and self.rect.y > 5:
         self.rect.y -= self.speed
      if keys[K_DOWN] and self.rect.y < win_height - 90:
         self.rect.y += self.speed

class Enemy(GameSprite):
   direction = "left"
   def update(self):
      if self.rect.x <= 470:
          self.direction = "right"
      if self.rect.x >= win_width-85:
          self.direction = "left"
      if self.direction == "left":
          self.rect.x -= self.speed
      else:
          self.rect.x += self.speed
color_1 = (0, 0, 0)
color_2 = (0, 255, 0)
color_3 = (255, 0, 0)
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        # картинка стіни - прямокутник потрібних розмірів та кольору
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        # кожен спрайт повинен зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y


    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 700
win_height = 500

window = display.set_mode((700, 500))
display.set_caption("Лабіринт")
background = transform.scale(
image.load("mike-no3.jpg"),
(win_width, win_height)
)

mixer.init()
mixer.music.load('love.ogg')
mixer.music.play()

game = True
clock = time.Clock()
FPS = 80
player = Player("mike.webp", 5, win_height-80, 4)
monster = Enemy("cyborg.png", win_width-80, 280, 2)
final = GameSprite("treasure.png", win_width-120, win_height-80, 0)
w1 = Wall(154, 205, 250, 100, 120, 450, 10)
w2 = Wall(154, 205, 200, 100, 0, 350, 10)
w3 = Wall(154, 205, 50, 300, 100, 10, 380)
finish = False
font.init()
font = font.Font(None, 70)
win = font.render(
'YOU WIN!', True, (255, 215, 0)
)
los = font.render(
'YOU LOST!', True, (255, 215, 0)
)
lost = mixer.Sound('lost.ogg')
money = mixer.Sound('money.ogg')
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:

        window.blit(background, (0, 0))
        player.update()
        monster.update()
        player.reset()
        monster.reset()
        final.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        if sprite.collide_rect(player, final):
            window.blit(win, (200, 200))
            finish = True
            mixer.music.stop()
            money.play()
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3):
            window.blit(los, (200, 200))
            finish = True
            mixer.music.stop()
            lost.play()
    display.update()
    clock.tick(80)


