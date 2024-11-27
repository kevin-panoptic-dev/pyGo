import pygame, os
from pygame.time import Clock
from pymodule import circulis
from interface import interface
from interphase import interphase
from constants import (
    set_clock,
    set_window,
    background_color,
    FPS,
    terminate,
    interim,
    screen_size,
    distance,
)
from pymodule.utility import prismelt
from backend import algorithm
from typing import Literal

CLOCK: Clock = set_clock()
WIN: pygame.Surface = set_window()
BOARD: algorithm = algorithm(19)
BACKGROUND: pygame.Surface = pygame.image.load(
    os.path.join("assets", "board-image.webp")
)
WHITE_STONE: pygame.Surface = pygame.image.load(
    os.path.join("assets", "white-stone.png")
)
BLACK_STONE: pygame.Surface = pygame.image.load(
    os.path.join("assets", "black-stone.png")
)

BACKGROUND = pygame.transform.scale(BACKGROUND, (800, 800))
WHITE_STONE = pygame.transform.scale(WHITE_STONE, (35, 35))
BLACK_STONE = pygame.transform.scale(BLACK_STONE, (35, 35))


def place_stone(
    window: pygame.Surface,
    clock: Clock,
    x: int,
    y: int,
    board: algorithm,
    player: Literal["black", "white"],
) -> bool:
    result: (
        Literal["arrogate"]
        | Literal["downfall"]
        | Literal["suicide"]
        | Literal["success"]
    ) = board.main(x, y, player)
    if result != "success":
        interface.warning_event(window, clock, result)
        return False

    board += (x, y, player)
    return True


def convert_to_coordinate(mouse_position: tuple[int, int]):
    if not (interim <= mouse_position[0] <= 800 - interim) or not (
        interim <= mouse_position[1] <= 800 - interim
    ):  # out of border, ignore
        return None

    converter = lambda position: round((position - interim) / distance)
    return converter(mouse_position[0]), converter(mouse_position[1])


def render_images(
    window: pygame.Surface,
    background: pygame.Surface,
    white_stone: pygame.Surface,
    black_stone: pygame.Surface,
    board: circulis,
    player: Literal["black", "white"],
):
    window.fill(background_color)
    window.blit(background, (0, 0))
    interface.add_resign(window)
    interface.player_bar(window, player)
    converter = lambda coordinate: coordinate * distance + interim
    size: int = len(board)
    for x_coordinate in range(size):
        for y_coordinate in range(size):
            if board[x_coordinate][y_coordinate] == "empty":
                continue
            elif board[x_coordinate][y_coordinate] == "white":
                window.blit(
                    white_stone,
                    (
                        converter(x_coordinate),
                        converter(y_coordinate),
                    ),
                )
            elif board[x_coordinate][y_coordinate] == "black":
                window.blit(
                    black_stone,
                    (
                        converter(x_coordinate),
                        converter(y_coordinate),
                    ),
                )
    pygame.display.update()


def game_event(
    window: pygame.Surface,
    clock: Clock,
    turn: Literal["black", "white"],
    board: algorithm,
):
    process = True
    player: Literal["black"] | Literal["white"] = turn
    while process:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                abstract_position = convert_to_coordinate(mouse_position)
                if abstract_position is not None:
                    if place_stone(window, clock, *abstract_position, board, player):
                        if player == "black":
                            player = "white"
                        else:
                            player = "black"

        render_images(
            window, BACKGROUND, WHITE_STONE, BLACK_STONE, board.circulist, player
        )


def loop(window: pygame.Surface, clock: Clock, board: algorithm):
    start = True
    turn: Literal["black", "white"] = "black"
    winner: Literal["black", "white"] = "black"
    while start:
        interphase.open_event(window, clock)
        game_event(window, clock, turn, board)
        start = interphase.close_event(window, clock, winner)


loop(WIN, CLOCK, BOARD)
