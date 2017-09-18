import pygame
import time
import random

pygame.init()
display_width = 1366
display_height = 768
gameDisplay = pygame.display.set_mode((display_width, display_height))
clo = pygame.time.Clock() 
small = pygame.font.Font("Peinture Fraiche.ttf", 50)
large = pygame.font.Font("MakethemSuffeR-Regular.ttf", 100)
red = (255, 0, 0)
black = (0,0,0)
white = (255, 255, 255)
randcolor = (200, 200, 0)
random_color = (150, 150, 0)
random1_color = (100, 100, 0)
img = pygame.image.load('head.png')
img_apple = pygame.image.load('apple.jpg')
pygame.display.set_caption("EAT LIVE REPEAT")
img_icon = pygame.image.load('head1.png')
pygame.display.set_icon(img_icon)
direction = 'up'

def pause():
    paused = True
    print_message("PAUSED",random1_color, y_dist = -100, size = large)
    print_message("PRESS C TO CONTINUE OR Q TO QUIT", random_color, y_dist = 50)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
def gameIntro():
    game = True
    print_message("SNAKEZZZZZZ", (139, 69, 19), size = large, y_dist = -200)
    print_message("EAT APPLES TO LIGHT SCORE", (173,255,47), size = small, y_dist = -50)
    print_message("BEWARE OF THE TRAP ON THE TOP",(119,136,153), size = small, y_dist = 50)
    print_message("Press C to Play or Q to Quit", (100, 100, 0), y_dist = 150)
    pygame.display.update()
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    game = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                


    
def print_score(score):
    text = small.render("SCORE " + str(score), True, random_color)
    gameDisplay.blit(text,[0,0])

def print_message(msg, color, y_dist = 0, size = small, x_init = 400, y_init = 300):
    screen_text = size.render(msg, True, color)
    screen_rect = screen_text.get_rect()
    screen_rect.center = (x_init, y_init + y_dist)
    gameDisplay.blit(screen_text, screen_rect)
    
def snakesize(lead_x, lead_y,snake_list, block_size, flag):
    temp = []
    temp.append(lead_x)
    temp.append(lead_y)
    snake_list.append(temp)
    if not flag and len(snake_list) > 1:
        del snake_list[0]
    if direction == 'right':
        head = pygame.transform.rotate(img,270)
    elif direction == 'left':
        head = pygame.transform.rotate(img, 90)
    elif direction == 'down':
        head = pygame.transform.rotate(img, 180)
    elif direction == 'up':
        head = img
    for inlist in snake_list[:-1]:
        gameDisplay.fill(black, [inlist[0], inlist[1], block_size, block_size])
    gameDisplay.blit(head, [snake_list[-1][0], snake_list[-1][1]])
    pygame.display.update()

            
  
def gameLoop():
    gameEnd = False
    gameOver = False
    global direction 
    snake_size_x = 50
    snake_size_y = 50
    apple_size = 50
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_change_x = 0
    lead_change_y = 0
    apple_x = random.randrange(50, display_width - apple_size)
    apple_y = random.randrange(50, display_height - apple_size)
    apple_x = round(apple_x/50) * 50
    apple_y = round(apple_y/50) * 50
    snake_list = []
    flag = 0
    score = 0
    
    while not gameEnd:
        if gameOver == True:
            print_message("game over!!!", randcolor, size = large, y_dist = -100)
            print_message("PRESS q to quit or c to play again", randcolor, 50)
            pygame.display.update()
        while gameOver == True:
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:      
                        gameOver = False
                        gameEnd = True
                    elif event.key == pygame.K_c:
                        gameLoop()    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameEnd = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and lead_change_x == 0:
                    lead_change_x = -50
                    lead_change_y = 0
                    direction = 'left'
                    break
                elif event.key == pygame.K_RIGHT and lead_change_x == 0:
                    lead_change_x = 50
                    lead_change_y = 0
                    direction = 'right'
                    break
                elif event.key == pygame.K_UP and lead_change_y == 0:
                    lead_change_x = 0
                    lead_change_y = -50
                    direction = 'up'
                    break
                elif event.key == pygame.K_DOWN and lead_change_y == 0:
                    lead_change_y = 50
                    lead_change_x = 0
                    direction = 'down'
                    break
                elif event.key == pygame.K_p:
                    pause()
        if (apple_x <= lead_x and apple_x + apple_size > lead_x) or (apple_x < lead_x + snake_size_x and apple_x + apple_size > lead_x + snake_size_x) :
            
            if (apple_y <= lead_y and apple_y + apple_size > lead_y) or (apple_y < lead_y + snake_size_x and apple_y + apple_size > lead_y + snake_size_x):
                flag = 1
                score += 1
                snakesize(lead_x, lead_y,snake_list, snake_size_x, flag)
                apple_x = random.randrange(0, display_width - apple_size)
                apple_y = random.randrange(0, display_height - apple_size)
                apple_x = round(apple_x/50) * 50
                apple_y = round(apple_y/50) * 50
        
        lead_x += lead_change_x
        lead_y += lead_change_y
        
        for inlist in snake_list[:-1]:
            if lead_x == inlist[0] and lead_y == inlist[1]:
                gameOver = True
        if lead_x >= display_width:
            lead_x = 0
        elif lead_x < 0:
            lead_x = display_width  
        elif lead_y >= display_height:
            lead_y = 0 
        elif lead_y < 0:
            lead_y = 600 
            gameOver = True
        gameDisplay.fill((139,0,139))
        gameDisplay.blit(img_apple, [apple_x, apple_y])
        flag = 0
        snakesize(lead_x, lead_y,snake_list, snake_size_x, flag)
        print_score(score)
        pygame.display.update()
        clo.tick(10)
    pygame.quit()
    quit()

gameIntro()
gameLoop()
 
