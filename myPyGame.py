# Date: 20 July 2021

# Author: Njabulo Nxumalo

# Purpose: Create a game using pygame library.

import sys, pygame
import random as ran

pygame.init()

# size of screen
size = width , height = 950, 700

# screen initialization.
screen = pygame.display.set_mode(size)
green = (36,83,43)

player_pos = [475,350]

# square size.
rect_size = [25,25]

# initializing player square.
player = pygame.Rect(player_pos,rect_size)

# initial direction of square.
x_direct = 25
y_direct = 0

# Prize square initial postion. Randomly generated.
prize_pos = [ran.randrange(0, width, 25),ran.randrange(0, height, 25)]

# Prize square intialized
prize = pygame.Rect(prize_pos, (25,25))

speed = 100

# Enemy intial position. Begins on right side edge of display, y position randomized. 
enemy_pos = [950,ran.randrange(0, height, 25)]

# Enemy colors to differentiate each enemy
enemy1_color = [255, 227, 56]
enemy2_color = [231, 84, 129]
enemy3_color = [0, 0, 255]

# Enemy color list
enemy_list = [enemy1_color,enemy2_color,enemy3_color]

# Enemy square intialization
enemy = pygame.Rect(enemy_pos,(25,25))

enemy_count = 0
consume = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        # Key input checked to move player square in left, right, down or up directions.
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP  and y_direct == 0:
                y_direct = -25
                x_direct = 0

            elif event.key == pygame.K_DOWN and y_direct == 0 :
                y_direct = 25
                x_direct = 0

            elif  event.key == pygame.K_LEFT and x_direct == 0:
                y_direct = 0
                x_direct = -25

            elif event.key == pygame.K_RIGHT and x_direct == 0:
                y_direct = 0
                x_direct = 25

    
    
        
    # Player collision block. Player loses if touched by enemy.
    if player[0] == enemy[0] and player[1] == enemy[1]:
        print("You lose!")
   
        # Quite game and exit window: 
    
        pygame.quit()
        exit(0)
    
    # Player has to consume prize twice to win. Before all three enemies have crossed the display.
    if player[0] == prize[0] and player[1] == prize[1]:    
        
        prize_pos = [ran.randrange(0, width, 25),ran.randrange(0, height, 25)]
        prize = pygame.Rect(prize_pos, (25,25))
        consume += 1
        if consume == 2:
            print("You Win!")
       
            # Quite game and exit window: 
        
            pygame.quit()
    
    # If 3 of the enemies make it across the display before player consumes 2 prizes, player loses.    
    if enemy_count > 2:
        print("You lose!")
       
        # Quite game and exit window: 
    
        pygame.quit()
        
    
    # Block tracks enemy crossing left side of boundary
    # New enemy is generated to start from right side of display.
    elif enemy[0] == -25:
        enemy_count += 1
        enemy_pos = [950,ran.randrange(0, height, 25)]
        enemy = pygame.Rect(enemy_pos,(25,25))
        
        
        
            
    # Screen boundary detection block.
    # Checks if player square crosses window boundary.
    # Sets squares position to the opposite boundary of the boundary crossed.
    
    if player[0] == width :
       player[0] = -25
       
    elif player[0] == -25:
        player[0] = 950
        
    if player[1] == height:
        player[1] = -25

    elif player[1] == -25:
        player[1] = 700


    
    # Enemy right to left movement.    
    enemy = enemy.move(-25, 0)        
    player = player.move(x_direct,y_direct)
    
    screen.fill(green)
    
    # Enemy square updated onto surface
    if enemy_count <= 2:
        pygame.draw.rect(screen,enemy_list[enemy_count], enemy)
    
    # Prize square updated onto surface.    
    pygame.draw.rect(screen, (0,0,0), prize)

    # Player square updated onto surface
    pygame.draw.rect(screen, (255,0,0), player)
    
    pygame.display.update()
    pygame.time.delay(speed)
    
