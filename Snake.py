# Snake
# Dhruti Gandhi
# 10/23/2023

import pygame
import time
import random

pygame.init() # initializes pygame

background_colour = (245, 233, 233)
white = (255, 255, 255)
black = (0, 0, 0)
red = (201, 24, 18)
red_1 = (255, 0, 0)
blue = (0, 0, 255)
green = (34,139,34)
yellow = (255, 255, 102)

width = 600
height = 400

display = pygame.display.set_mode((width,height))
pygame.display.set_caption('Snake Game by Dhruti Gandhi')

clock = pygame.time.Clock() # helps track time

snake_block = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

levels = {"Easy": 10, "Medium": 15, "Hard": 20}

# score
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    display.blit(value, [5, 0])

# snake
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

# message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width/20, height/2.3])

def choose_level():
    level_chosen = False
    while not level_chosen:
        display.fill(background_colour)
        message("CHOOSE LEVEL: 1 - Easy, 2 - Medium, 3 - Hard", blue)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "Easy"
                if event.key == pygame.K_2:
                    return "Medium"
                if event.key == pygame.K_3:
                    return "Hard"

# the game itself
def gameLoop(level):
    snake_speed = levels[level]
    
    game_over = False
    game_close = False
    
    x1 = width / 2
    y1 = height / 2
    
    x1_change = 0
    y1_change = 0
    
    snake_list = []
    snake_length = 1
    
    food_1 = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_2 = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    
    while not game_over:
        
        while game_close == True:
            display.fill(white)
            message("You Lost! Press E to end game or P to play again", red_1)
            your_score(snake_length - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        chosen_level = choose_level()
                        gameLoop(chosen_level)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        display.fill(background_colour)
        pygame.draw.rect(display, red, [food_1, food_2, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
            
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        
        snake(snake_block, snake_list)
        your_score(snake_length - 1)
        
        pygame.display.update()
        
        if x1 == food_1 and y1 == food_2:
            food_1 = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_2 = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1
            print("Yum!!")
        
        clock.tick(snake_speed)
        
    # uninitialize everything
    pygame.quit()
    quit()
    
if __name__ == "__main__":
    chosen_level = choose_level()
    gameLoop(chosen_level)