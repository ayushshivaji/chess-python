import pygame
from source.chess_enums import *

class Chessboard():
    def __init__(self, *arg, **kwarg):
        self.SCREEN_LENGTH = kwarg.get("screen_length")
        self.SCREEN_WIDTH = kwarg.get("screen_width")
        self.SCREEN = kwarg.get("screen")
        self.FEN = kwarg.get("fen", Misc.STARTING_FEN.value)
        self.position = []
        self.box_length = self.SCREEN_LENGTH//8

    def draw_white_squares(self):
        self.SCREEN.fill((255, 255, 255))

    def draw_black_squares(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 1:
                    pygame.draw.rect(self.SCREEN, Colors.GREEN.value, (j*(self.box_length), i*(self.box_length), (self.box_length), (self.box_length)))

    def draw_piece(self, piece: str, x: int = 0, y: int = 0):
        piece_to_draw = pygame.transform.scale(PieceMapping[piece].value, (self.box_length, self.box_length))
        self.SCREEN.blit(piece_to_draw, (x, y))

    def fen_to_array(self):
        pieces = self.FEN.split(" ")[0].split("/")
        for rank, iter in enumerate(pieces):
            char_array = []
            for file, char in enumerate(iter):
                if char.isdigit():
                    spaces = int(char)
                    while spaces > 0:
                        char_array.append(" ")
                        spaces -= 1
                else:
                    char_array.append(char)
            self.position.append(char_array)

    def draw_all_pieces(self, position: list):
        for rank, iter in enumerate(position):
            for file, char in enumerate(iter):
                if char == " ":
                    continue
                else:
                    self.draw_piece(char, (file)*(self.box_length), (rank)*(self.box_length))

    def draw_fen(self):
        self.draw_white_squares()
        self.draw_black_squares()
        self.fen_to_array()
        self.draw_all_pieces(self.position)

