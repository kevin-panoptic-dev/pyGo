import pygame, os
from pygame.time import Clock
from interface import interface
from interphase import interphase
from constants import (
    set_clock,
    set_window,
    background_color,
    FPS,
    terminate,
    interim,
    distance,
    resign_button_position,
)
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
        if result == "suicide":
            board -= (x, y, player)
        return False

    board += (x, y, player)
    return True


def ambiguous(mouse_position: tuple[int, int]):
    if not (interim <= mouse_position[0] <= 800 - interim) or not (
        interim <= mouse_position[1] <= 800 - interim
    ):  # out of border, ambiguous
        return True
    if (
        1 / 4 * distance < (mouse_position[0] - interim) % distance < 3 / 4 * distance
    ) or (
        1 / 4 * distance < (mouse_position[1] - interim) % distance < 3 / 4 * distance
    ):
        return True  # middle of the tile, ambiguous
    return False


def convert_to_coordinate(mouse_position: tuple[int, int]):
    if not ambiguous(mouse_position):
        converter = lambda position: round((position - interim) / distance)
        return converter(mouse_position[0]), converter(mouse_position[1])


def render_images(
    window: pygame.Surface,
    background: pygame.Surface,
    white_stone: pygame.Surface,
    black_stone: pygame.Surface,
    board: list,
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


def dentro(  # inside
    mouse_position: tuple[int, int],
    button_position: tuple[float, float, float, float],
) -> bool:
    if (
        button_position[0]
        < mouse_position[0]
        < (button_position[0] + button_position[2])
    ) and (
        button_position[1]
        < mouse_position[1]
        < (button_position[1] + button_position[3])
    ):
        return True
    return False


def game_event(
    window: pygame.Surface,
    clock: Clock,
    turn: Literal["black", "white"],
    board: algorithm,
):
    player: Literal["black"] | Literal["white"] = turn
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                # adjust the real mouse position
                mouse_position = (mouse_position[0] - 15, mouse_position[1] - 15)
                if dentro(mouse_position, resign_button_position):
                    if interface.warning_event(window, clock, "resign") == "resign":
                        if player == "black":
                            return "white"
                        return "black"
                abstract_position = convert_to_coordinate(mouse_position)
                if abstract_position is not None:
                    if place_stone(window, clock, *abstract_position, board, player):
                        if player == "black":
                            player = "white"
                        else:
                            player = "black"

        render_images(window, BACKGROUND, WHITE_STONE, BLACK_STONE, board.get, player)


def loop(window: pygame.Surface, clock: Clock, board: algorithm):
    restart = False
    while True:
        if not restart:
            interphase.open_event(window, clock)
        winner = game_event(window, clock, "black", board)
        restart = interphase.close_event(window, clock, winner)
        board.restart
        if restart == "start":
            restart = True
            continue
        restart = False


loop(WIN, CLOCK, BOARD)



# Thanks for scrolling 😊