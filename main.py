import pygame
pygame.init()
"""pygame takes color as a RGB format"""
white=(255,255,255)
black=(0,0,255)
red=(255,0,0)

dis=pygame.display.set_mode((400,400)) 
"""create screen using pygame library and display.set_mode()"""
pygame.display.update()
pygame.display.set_caption('Dheeruvaii_Snake_Game')

# blue=(0,0,255)
# """  color variable initializations """
# red=(255,0,0)

game_over=False
x1=300
y1=300


x1_change=0
y1_change=0

while not game_over:
    """holds scrren time until the game not finished/over"""
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            game_over=True
        if event.type==pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                x1_change=-10
                y1_change=0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis,black,([x1,y1,10,10]))
    """rectangle object created on then screen"""
    pygame.display.update()

pygame.quit()
quit()


