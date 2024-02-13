import pygame
pygame.init()
dis=pygame.display.set_mode((400,400)) 
"""create screen using pygame library and display.set_mode()"""
pygame.display.update()
pygame.display.set_caption('Dheeruvaii_Snake_Game')

blue=(0,0,255)
"""  color variable """
red=(255,0,0)

game_over=False
while not game_over:
    """holds scrren time until the game not finished/over"""
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            game_over=True

    pygame.draw.rect(dis,blue,([200,100,20,20]))
    pygame.display.update()

pygame.quit()
quit()

"""create the snake"""
