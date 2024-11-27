import pygame
import sys
from typing import Literal, NoReturn
from pygame.font import Font
from pygame.time import Clock

pygame.font.init()

# width, height
screen_size: tuple[Literal[800], Literal[1000]] = 800, 1000

# design constants
FPS: Literal[60] = 60
background_color: tuple[Literal[205], Literal[192], Literal[190]] = 205, 192, 190
title: Font = pygame.font.SysFont("comiscans", 100)
font: Font = pygame.font.SysFont("comicsans", 50)
button_font: Font = pygame.font.SysFont("comicsans", 35)
font_color: tuple[Literal[0], Literal[0], Literal[0]] = 0, 0, 0
button_color: tuple[Literal[255], Literal[0], Literal[0]] = 255, 0, 0
message_font = pygame.font.SysFont("comiscans", 25)
interim: Literal[11] = 11
distance = 41.5


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


# label constants
first_label_position: tuple[float, float, float, float] = (
    screen_size[0] / 4,
    screen_size[1] * 3 / 4,
    150.0,
    50.0,
)
second_label_position: tuple[float, float, float, float] = (
    screen_size[0] * 3 / 4,
    screen_size[1] * 3 / 4,
    150.0,
    50.0,
)


middle_label_position: tuple[Literal[100], Literal[400], Literal[600], Literal[200]] = (
    100,
    400,
    600,
    200,
)
confirm_label_position: tuple[Literal[350], Literal[530], Literal[100], Literal[50]] = (
    350,
    530,
    100,
    50,
)
resign_button_position: tuple[Literal[600], Literal[850], Literal[100], Literal[50]] = (
    600,
    850,
    100,
    50,
)
