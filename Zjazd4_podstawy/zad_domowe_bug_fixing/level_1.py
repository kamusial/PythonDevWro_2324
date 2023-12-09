"""
Wymagania:
pip install pygame

Ten kod powinien włączyć 'grę' z chodzącym prostokątem, ale nie działa :D
Pls fix
"""

import pygame


def create_screen():
    screen = pygame.display.set_mode((800, 600))
    return screen


def keypress_handling(player: pygame.Rect):
    key = pygame.key.get_pressed()
    moves = {
        pygame.K_LEFT: (-1, 0),
        pygame.K_RIGHT: (1, 0),
        pygame.K_UP: (0, -1),
        pygame.K_DOWN: (0, 1),
    }
    for button, movement in moves:
        if key[button]:
            player.move_ip(*movement)


def main():
    pygame.init()
    screen = create_screen()
    player = pygame.Rect((300, 250, 50, 50))

    quit_game = False
    while not quit_game:
        keypress_handling(player)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 255, 0), player)
        pygame.display.update()
    pygame.quit()


main()
