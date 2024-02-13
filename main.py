"""Needed libraries"""
import pygame
import time
import random


pygame.init()
"""pygame takes color as a RGB format"""

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)


# x1= dis_width/2 
# y1= dis_height/2

# x1_change = 0
# y1_change = 0
"""
foods created time pass into loop functions

"""


"""screen width and height (for boundries)"""
dis_width=600
dis_height=400

dis=pygame.display.set_mode((dis_width,dis_height)) 
"""create screen using pygame library and display.set_mode()"""
# pygame.display.update()
pygame.display.set_caption('Dheeruvaii_Snake_Game')

clock=pygame.time.Clock()

snake_block=10
snake_speed=15


font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def my_score(score):
    value=font_style.render("my score :" + str(score),True,yellow)
    dis.blit(value, [0,0])
    """
    Blit (draw) the rendered text onto the game screen at the specified position [0, 0].
    This position represents the top-left corner of the screen.
    """

snake_icon = pygame.image.load("snake.png")  # Load snake icon image
snake_icon = pygame.transform.scale(snake_icon, (snake_block, snake_block))  # Resize image to match snake block size

def my_snake(snake_block ,snake_list):
    for x,y in snake_list:
        # pygame.draw.rect(dis ,black, [x[0],x[1],snake_block,snake_block])
        dis.blit(snake_icon,(x,y))


        """Draw a rectangle representing each segment of the snake's body.
        The position and size of the rectangle are determined by the corresponding values in the snake_list.
        The color of the rectangle is black, and its size is determined by snake_block.
        """

"""for game over message"""
def message(msg,color):
    mesg=font_style.render(msg,True,color)
    dis.blit(mesg,  [dis_width/6 ,dis_height/3] ) 
    """blit draws the  message  on the display """

def gameloop():
    """
    This function represents the main game loop for the Snake game.

    The game loop manages the game state, handles user input, updates the positions
    of the snake and food, and renders the game graphics.

    Parameters:
        None

    Returns:
        None
    """
    game_over=False  
    """Flag to indicate if the game is over"""
    game_close=False  
    """Flag to indicate if the game is in a "game over" state"""

    """ Initialize the position of the snake's head at the center of the game screen"""
    x1= dis_width/2
    y1= dis_height/2


    """Initialize the direction of the snake's movement"""
    x1_change = 0
    y1_change = 0

    snake_list=[]
    length_of_snake=1

    """Generate random positions for the food within the game screen boundaries"""
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0


    while not game_over:
        """
        Main game loop.
        """
        while game_close == True:
            
            dis.fill(blue)
            message("you Lost Press Q-Quit and C-play again ",red)
            pygame.display.update()
    
            for event in pygame.event.get():
                """
                Iterate through all the events that have occurred since the last call to pygame.event.get().
            """
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
            """
            Check if the snake's head is out of bounds of the game screen.
            If any of the following conditions are true, it indicates that the snake's head
            has collided with the boundaries of the game screen:
            - If x-coordinate of the snake's head (x1) is greater than or equal to the width of the game screen (dis_width).
            - If x-coordinate of the snake's head (x1) is less than 0.
            - If y-coordinate of the snake's head (y1) is greater than or equal to the height of the game screen (dis_height).
            - If y-coordinate of the snake's head (y1) is less than 0."""

            game_over=True
            """
                If the snake's head goes out of bounds of the game screen, set the game_over flag to True.
                This indicates that the game should be ended.
                """
            
        """key press operations
        Update the position of the snake's head based on the current direction of movement
        """
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis,green,[foodx,foody,snake_block,snake_block])
        # pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        """rectangle object created on then screen"""

        snake_head=[]
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
             if x == snake_head:
                game_close=True

        my_snake(snake_block,snake_list)
        my_score(length_of_snake -1)
        pygame.display.update()


        if x1 == foodx and y1==foody:
            """Generate random positions for the food within the game screen boundaries"""
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            # print("yummy")
        clock.tick(snake_speed)
    pygame.quit()
    quit()

gameloop()


    

 


