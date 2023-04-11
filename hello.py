import pygame
from pygame import mixer
import sys

pygame.init()                                   # Pygameの初期化
screen = pygame.display.set_mode((800, 600))    # 大きさ800*600の画面を生成
# screen.fill((150, 150, 150))                    #背景の塗りつぶし
pygame.display.set_caption("Invadars Game")              # タイトルバーに表示する文字

# Player
PlayerImg = pygame.image.load("player.png")
playerX, playerY = 370, 480
player_change = 0

def player(x, y):
    screen.blit(PlayerImg, (x, y))

#音声の出力:ぴゅん
# mixer.Sound("laser.wav").play()


running = True
while running:
    screen.fill((0, 0, 0))
    # font = pygame.font.SysFont(None, 80)
    # message = font.render("Hello World", False, (255, 255, 255))
    # screen.blit(message, (20, 50))
    # イベント処理
    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # 閉じるボタンが押されたら終了
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.5
            

    # playerX += 1.5
    player(playerX, playerY)

    pygame.display.update()



