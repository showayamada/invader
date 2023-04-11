import pygame
import sys

pygame.init()                                   # Pygameの初期化
screen = pygame.display.set_mode((400, 300))    # 大きさ400*300の画面を生成
pygame.display.set_caption("Test")              # タイトルバーに表示する文字

while (1):
    screen.fill((0,0,0))        # 画面を黒色(#000000)に塗りつぶし
    pygame.display.update()     # 画面を更新
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 閉じるボタンが押されたら終了
            pygame.quit()       # Pygameの終了(画面閉じられる)
            sys.exit()



