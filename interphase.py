import pygame, os
from constants import (
    FPS,
    font,
    font_color,
    title,
    background_color,
    button_font,
    screen_size,
    terminate,
    first_label_position,
    second_label_position,
    text_font,
)
from pygame.time import Clock
from typing import Literal

GO = pygame.image.load(os.path.join("assets", "Go.png"))
GO = pygame.transform.scale(GO, (400, 200))
help_text = [
    "Go, a timeless strategy game, is played on a grid of 19x19, ",
    "13x13, or 9x9 intersections. Two players, Black and White, ",
    "alternate placing stones to claim territory, aiming to surround",
    "empty spaces and capture opposing stones by encircling them. ",
    "",
    "Stones with no liberties (empty adjacent points) are removed. ",
    "The game concludes when both players pass consecutively, signaling",
    "no beneficial moves remain. Scores are tallied by counting",
    "controlled territory and captured stones, with White receiving",
    "a point advantage for balance. Strategy emphasizes balance between",
    "offense and defense, requiring foresight, adaptability, and ",
    "precision. Go embodies elegance through its simple rules yet ",
    "profound depth.",
]
text_y = [x * 50 for x in range(1, len(help_text) + 1)]
text_x = 20


class interphase:
    @classmethod
    def render_text(cls, window: pygame.Surface):
        index = 0
        for text in help_text:
            text = text_font.render(text, 1, (0, 0, 0))
            window.blit(text, (text_x, text_y[index]))
            index += 1

    @classmethod
    def close_screen(
        cls,
        window: pygame.Surface,
        player: Literal["black", "white"],
        button_positions: tuple[tuple, tuple],
    ):
        label: pygame.Surface = title.render(f"{player} wins!", 1, (255, 223, 98))
        window.fill(background_color)
        window.blit(label, (int(screen_size[0] / 2 - label.get_width() / 2), 400))
        cls.create_button(window, "restart", button_positions[0], (248, 215, 123))
        cls.create_button(window, "exit", button_positions[1], (248, 215, 123))
        pygame.display.update()

    @classmethod
    def create_button(
        cls,
        window: pygame.Surface,
        text: str,
        size: tuple[float, float, float, float],
        color: tuple[int, int, int],
    ) -> None:
        button = pygame.Rect(*size)
        label: pygame.Surface = button_font.render(text, 1, font_color)
        font_x = int(size[0] + size[2] / 2 - label.get_width() / 2)
        font_y = int(size[1] + size[3] / 2 - label.get_height() / 2)
        pygame.draw.rect(window, color, button, border_radius=5)
        window.blit(label, (font_x, font_y))

    @classmethod
    def dentro(  # inside
        cls,
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

    @classmethod
    def open_screen(cls, window: pygame.Surface, button_positions: tuple[tuple, tuple]):
        window.fill(background_color)
        window.blit(
            GO,
            (
                int(screen_size[0] / 2 - GO.get_width() / 1.5),
                int(screen_size[1] / 2 - GO.get_height()),
            ),
        )
        description: pygame.Surface = font.render(
            "Click the buttons to begin", 1, font_color
        )
        window.blit(
            description,
            (
                int(screen_size[0] / 2 - description.get_width() / 2),
                int(screen_size[1] / 2 + description.get_height()),
            ),
        )
        cls.create_button(window, "Start", button_positions[0], (161, 227, 168))
        cls.create_button(window, "Help", button_positions[1], (150, 217, 223))
        pygame.display.update()

    @classmethod
    def help_screen(
        cls, window: pygame.Surface, button_position: tuple[float, float, float, float]
    ) -> None:
        window.fill(background_color)
        cls.render_text(window)
        cls.create_button(window, "return", button_position, (103, 193, 202))
        pygame.display.update()

    @classmethod
    def open_event(cls, window: pygame.Surface, clock: Clock):
        process = True
        call_main = False
        call_help = False
        while process:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position: tuple[int, int] = pygame.mouse.get_pos()
                    if cls.dentro(position, first_label_position):
                        call_main = True
                        process = False
                    elif cls.dentro(position, second_label_position):
                        call_help = True
                        process = False
            cls.open_screen(window, (first_label_position, second_label_position))

        if call_help:
            cls.help_event(window, clock)
        elif call_main:
            return "start"

    @classmethod
    def help_event(cls, window: pygame.Surface, clock: Clock) -> None:
        process = True
        call_open = False
        while process:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position: tuple[int, int] = pygame.mouse.get_pos()
                    if cls.dentro(position, second_label_position):
                        call_open = True
                        process = False

            cls.help_screen(window, second_label_position)
        if call_open:
            cls.open_event(window, clock)

    @classmethod
    def close_event(
        cls, window: pygame.Surface, clock: Clock, player: Literal["black", "white"]
    ):
        process = True
        call_main = False
        while process:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    if cls.dentro(position, first_label_position):
                        call_main = True
                        process = False
                    elif cls.dentro(position, second_label_position):
                        terminate()

            cls.close_screen(
                window, player, (first_label_position, second_label_position)
            )
        if call_main:
            return "start"

# Thanks for scrolling 😊