import pygame
from pygame.locals import *
from source.chess_enums import *
from source.chessboard import Chessboard

SCREEN_LENGTH = 1000
SCREEN_WIDTH = 1000
SCREEN = pygame.display.set_mode([SCREEN_LENGTH, SCREEN_WIDTH])

def main():
    pygame.init()
    running = True
    kwargs = {
        "screen_length": SCREEN_LENGTH,
        "screen_width": SCREEN_WIDTH,
        "screen": SCREEN,
        "fen": "r1r3k1/4qpp1/4bn1p/pp1pN3/2pP1P2/4P3/PPQ3PP/1BR2RK1 w - - 0 19"
    }
    Chess = Chessboard(**kwargs)
    Chess.draw_fen()
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
