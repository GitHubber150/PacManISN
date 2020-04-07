import pygame
from game import *

pygame.init()
screen = pygame.display.set_mode((1080,720))
pygame.display.set_caption("PacMan vISN")


#importe/charge le fichier dans la variable bg
background = pygame.image.load('assets/black_bg.png')

game = Game()

run = True #+game.player.velocity pour que le programme prévoie l'arret du perso à l'avance
while run:
    pygame.time.Clock().tick(200) #fps
    screen.blit(background,(0,0)) #appliquer à screen le bg
    screen.blit(game.player.image,game.player.rect) #appliquer à screen le perso

    #screen.blit(game.point.image,game.point.rect)
    
    if (game.key_pressed.get(pygame.K_RIGHT) == True) and game.player.rect.x + game.player.rect.width + game.player.velocity < screen.get_width():
        game.player.move_right()
    if (game.key_pressed.get(pygame.K_LEFT) == True) and game.player.rect.x > 0:
        game.player.move_left()
    if (game.key_pressed.get(pygame.K_DOWN) == True) and game.player.rect.y + game.player.rect.height + game.player.velocity < screen.get_height():
        game.player.move_down()
    if (game.key_pressed.get(pygame.K_UP) == True) and game.player.rect.y > 0:
        game.player.move_up()
    
    pygame.display.flip() #actualise l'écran
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            print("Closing the game.")
            break

        elif event.type == pygame.KEYDOWN:
            game.key_pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.key_pressed[event.key] = False
