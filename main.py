import pygame, sys
from game import Game

pygame.init()

title_font = pygame.font.Font(None, 40)

dark_blue = (44, 44, 127)

# creates a display surface object called screen. the game window!
screen = pygame.display.set_mode((500, 620))
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
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()    
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()       
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down() # update block position when it has to not just when the loop executes
    # Drawing
    screen.fill(dark_blue)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
