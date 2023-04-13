import pygame
from pygame import mixer
import sys
import random
import math

pygame.init()                                   # Pygameの初期化
screen = pygame.display.set_mode((800, 600))    # 大きさ800*600の画面を生成
# screen.fill((150, 150, 150))                    #背景の塗りつぶし
pygame.display.set_caption("Invadars Game")              # タイトルバーに表示する文字

# Player
playerImg = pygame.image.load("player.png")
playerX, playerY = 370, 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change, enemyY_change = 1, 40

#Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX, bulletY = 0, 480
bulletX_change, bulletY_change = 0, 1
bullet_state = "ready"

# score
score_value = 0

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False

#音声の出力:ぴゅん
# mixer.Sound("laser.wav").play()


running = True
while running:
    screen.fill((0, 0, 0))
    
    # イベント処理
    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # 閉じるボタンが押されたら終了
            running = False
        
        # プレイヤーの操作
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    # プレイヤーの移動制限
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY) # playerの描写

    # enemyの移動
    if enemyY > 440:
        break
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.2
        enemyY += enemyY_change

    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score_value += 1
        enemyX = random.randint(0, 736)
        enemyY = random.randint(50, 150)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    enemy(enemyX, enemyY)

    #score
    font = pygame.font.SysFont(None, 32)
    score = font.render(f"Score : {str(score_value)}", True, (255, 255, 255))
    screen.blit(score, (20, 50))

    pygame.display.update()



