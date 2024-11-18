import pygame, sys
from game import Game

pygame.init()
dark_blue = (44, 44, 127)

# creates a display surface object called screen. the game window!
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT # creating custom events 
pygame.time.set_timer(GAME_UPDATE, 200) # ensuring that the game updates block position every 200 ms and not 60 times per sec

# get all the events that pygame recognizes
while True: # game loop is 60 fps and it loops 60 times per second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_UP:
                game.rotate()       
        if event.type == GAME_UPDATE:
            game.move_down() # update block position when it has to not just when the loop executes
    # Drawing
    screen.fill(dark_blue)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
