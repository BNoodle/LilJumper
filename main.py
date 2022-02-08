import pygame
import os
import constants
import player
import group
import menu
import save_managing

pygame.init()

SCREEN_DIMENSIONS = WIDTH, HEIGHT = constants.SCREEN_SIZE
screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
FPS = 60
clock = pygame.time.Clock()

# save file
default_data = {
    'highscore': 0
}
save_file = save_managing.SaveFile(os.path.join(os.path.dirname(__file__), 'save'), default_data)

my_menu = menu.Menu(screen)
platforms = group.PlatformGroup(screen)
my_player = player.Player(screen, my_menu, platforms, WIDTH//2-(0.5*constants.PLAYER_SIZE), HEIGHT-200)

running = True
while running:  
    screen.fill(constants.BG_COLOR)
    
    if my_menu.get_mode() == 'play':
        platforms.update()
        my_player.update()
    elif my_menu.get_mode() == 'game over':
        platforms.update()
        my_player.update()
    elif my_menu.get_mode() == 'restart':
        platforms = group.PlatformGroup(screen)
        my_player = player.Player(screen, my_menu, platforms, WIDTH//2-(0.5*constants.PLAYER_SIZE), HEIGHT-200)

    my_menu.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(FPS)