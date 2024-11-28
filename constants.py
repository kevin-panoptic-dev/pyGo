import pygame
import sys
from typing import Literal, NoReturn
from pygame.font import Font
from pygame.time import Clock

pygame.font.init()

# width, height
screen_size: tuple[Literal[800], Literal[900]] = 800, 900

# design constants
FPS: Literal[60] = 60
background_color: tuple[Literal[205], Literal[192], Literal[190]] = 205, 192, 190
title: Font = pygame.font.SysFont("comiscans", 100)
font: Font = pygame.font.SysFont("comicsans", 50)
button_font: Font = pygame.font.SysFont("comicsans", 35)
font_color = 61, 61, 61
message_font = pygame.font.SysFont("comicsans", 33)
text_font = pygame.font.SysFont("comicsans", 24)
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
first_label_position: tuple[Literal[100], Literal[700], Literal[150], Literal[50]] = (
    100,
    700,
    150,
    50,
)
second_label_position: tuple[Literal[550], Literal[700], Literal[150], Literal[50]] = (
    550,
    700,
    150,
    50,
)


middle_label_position = (
    150,
    300,
    500,
    200,
)
confirm_label_position: tuple[Literal[350], Literal[530], Literal[100], Literal[50]] = (
    350,
    530,
    100,
    50,
)
resign_button_position: tuple[Literal[550], Literal[825], Literal[150], Literal[50]] = (
    550,
    825,
    150,
    50,
)

# Thanks for scrolling 😊