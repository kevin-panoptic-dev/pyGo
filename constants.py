import pygame
import sys
from typing import Literal, NoReturn
from pygame.font import Font
from pygame.time import Clock
from pymodule import circulis
from pymodule.utility import prismelt

pygame.font.init()

# width, height
screen_size: tuple[Literal[800], Literal[800]] = 800, 800

# 19 vertical lines, 19 horizontal lines, 40 margin left + 18 • 40 middle + 40 margin right
horizontal_line_position: circulis = circulis((x for x in range(40, 761, 40)))
vertical_line_position: circulis = horizontal_line_position[:]


# design constants
FPS: Literal[60] = 60
background_color: tuple[Literal[205], Literal[192], Literal[190]] = 205, 192, 190
line_thickness: Literal[10] = 10
title: Font = pygame.font.SysFont("comiscans", 100)
font: Font = pygame.font.SysFont("comicsans", 50)
button_font: Font = pygame.font.SysFont("comicsans", 35)
font_color: tuple[Literal[0], Literal[0], Literal[0]] = 0, 0, 0
button_color: tuple[Literal[255], Literal[0], Literal[0]] = 255, 0, 0


def terminate() -> NoReturn:
    pygame.quit()
    sys.exit()


def set_window() -> pygame.Surface:
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Go")
    return pygame.display.set_mode(screen_size)


def set_clock() -> Clock:
    return pygame.time.Clock()
