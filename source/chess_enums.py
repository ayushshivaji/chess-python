from enum import Enum
import pygame


class Misc(Enum):
    STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

class Colors(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)


class Pieces(Enum):
    BLACK_ROOK = pygame.image.load("source/assets/black_rook.png")
    BLACK_KNIGHT = pygame.image.load("source/assets/black_knight.png")
    BLACK_BISHOP = pygame.image.load("source/assets/black_bishop.png")
    BLACK_KING = pygame.image.load("source/assets/black_king.png")
    BLACK_QUEEN = pygame.image.load("source/assets/black_queen.png")
    BLACK_PAWN = pygame.image.load("source/assets/black_pawn.png")

    WHITE_ROOK = pygame.image.load("source/assets/white_rook.png")
    WHITE_KNIGHT = pygame.image.load("source/assets/white_knight.png")
    WHITE_BISHOP = pygame.image.load("source/assets/white_bishop.png")
    WHITE_KING = pygame.image.load("source/assets/white_king.png")
    WHITE_QUEEN = pygame.image.load("source/assets/white_queen.png")
    WHITE_PAWN = pygame.image.load("source/assets/white_pawn.png")


class PieceMapping(Enum):
    r = Pieces.BLACK_ROOK.value
    n = Pieces.BLACK_KNIGHT.value
    b = Pieces.BLACK_BISHOP.value
    k = Pieces.BLACK_KING.value
    q = Pieces.BLACK_QUEEN.value
    p = Pieces.BLACK_PAWN.value

    R = Pieces.WHITE_ROOK.value
    N = Pieces.WHITE_KNIGHT.value
    B = Pieces.WHITE_BISHOP.value
    K = Pieces.WHITE_KING.value
    Q = Pieces.WHITE_QUEEN.value
    P = Pieces.WHITE_PAWN.value
