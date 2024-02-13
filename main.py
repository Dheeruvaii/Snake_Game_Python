import pygame
import time
import random


pygame.init()
"""pygame takes color as a RGB format"""
white=(255,255,255)
black=(0,255,0)
red=(255,0,0)
blue=(0,0,255)


# x1= dis_width/2 
# y1= dis_height/2

# x1_change = 0
# y1_change = 0
"""
foods created time pass into loop functions

"""


"""screen width and height (for boundries)"""
dis_width=800
dis_height=600

dis=pygame.display.set_mode((dis_width,dis_height)) 
"""create screen using pygame library and display.set_mode()"""
# pygame.display.update()
pygame.display.set_caption('Dheeruvaii_Snake_Game')

clock=pygame.time.Clock()

snake_block=10
snake_speed=30


font_style = pygame.font.SysFont(None, 50)


"""for game over message"""
def message(msg,color):
    mesg=font_style.render(msg,True,color)
    dis.blit(mesg,  [dis_width/2 ,dis_height/2] ) 
    """blit draws the  message  on the display """

def gameloop():
    game_over=False
    game_close=False

    x1= dis_width/2
    y1= dis_height/2

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0


    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("you Lost Press Q-Quit and C-play again ",red)
            pygame.display.update()
    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_q:
                    game_over=True
                    game_close=False
                if event.key == pygame.K_c:
                    gameloop()

        """this code block displays a message indicating that the player lost, 
        gives them options to either quit or play again, and waits for their input. 
        If the player chooses to quit by pressing 'Q', the game ends. 
        If the player chooses to play again by pressing 'C', the game loop restarts by calling the gameLoop() function."""

        """holds scrren time until the game not finished/over"""
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                """KEYDOWN is a pygame class which helps to move a snake by pressing key up/down """
                if event.key== pygame.K_LEFT:
                    x1_change= -snake_block
                    y1_change= 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        """if x1 &amp;gt;= dis_width or x1 &amp;lt; 0 or y1 &amp;gt;= dis_height or y1 &amp;lt; 0:
                Replace &amp;gt; with > and &amp;lt; with <. These symbols are used to compare values in Python, and Visual Studio Code should recognize them without issue."""
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over=True
        """key press operations"""
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis,blue,[foodx,foody,snake_block,snake_block])
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        """rectangle object created on then screen"""

        pygame.display.update()
        if x1 == foodx and y1==foody:
            print("yummy")
        clock.tick(snake_speed)
    pygame.quit()
    quit()

gameloop()


    
# """pass message parameters"""
# message("OH Game-Over",red)
# pygame.display.update()
# time.sleep(2)

 


