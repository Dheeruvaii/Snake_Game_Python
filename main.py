import pygame
pygame.init()
dis=pygame.display.set_mode((400,400)) 
"""create screen using pygame library and display.set_mode()"""
pygame.display.update()
pygame.display.set_caption('Dheeruvaii_Snake_Game')
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            game_over=True

pygame.quit()
quit()