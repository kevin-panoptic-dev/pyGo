from constants import (
    button_font,
    middle_label_position,
    confirm_label_position,
    font_color,
    terminate,
    FPS,
    resign_button_position,
    font,
)
import pygame
from pygame.time import Clock
from typing import Literal


class interface:
    @classmethod
    def raise_warning(
        cls,
        window: pygame.Surface,
        warning: str,
        size: tuple[float, float, float, float],
        color: tuple[int, int, int],
    ) -> None:
        button = pygame.Rect(*size)
        label: pygame.Surface = button_font.render(warning, 1, font_color)
        font_x = int(size[0] + size[2] / 2 - label.get_width() / 2)
        font_y = int(size[1] + size[3] / 2 - label.get_height() / 2)
        pygame.draw.rect(window, color, button, border_radius=label.get_width() // 5)
        window.blit(label, (font_x, font_y))

    @classmethod
    def dentro(
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
    def warning_screen(
        cls,
        window: pygame.Surface,
        warning_type: Literal["suicide", "arrogate", "downfall", "resign"],
    ) -> None:
        if warning_type == "suicide":
            message = "Invalid suicide move"
        elif warning_type == "arrogate":
            message = "Invalid arrogate move"
        elif warning_type == "downfall":
            message = "Out of border"
        elif warning_type == "resign":
            message = "Are you sure to resign?"

        background = window.copy()
        window.blit(background, (0, 0))
        cls.raise_warning(window, message, middle_label_position, (255, 204, 0))
        cls.raise_warning(window, "OK", confirm_label_position, (121, 188, 255))
        pygame.display.update()

    @classmethod
    def warning_event(
        cls,
        window: pygame.Surface,
        clock: Clock,
        warning_type: Literal["suicide", "arrogate", "downfall", "resign"],
    ):
        process = True
        while process:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    if cls.dentro(mouse_position, confirm_label_position):
                        process = False
            cls.warning_screen(window, warning_type)

        return "resign" if warning_type == "resign" else "continue"

    @classmethod
    def add_resign(cls, window: pygame.Surface):
        cls.raise_warning(window, "resign", resign_button_position, (226, 114, 113))

    @classmethod
    def player_bar(cls, window: pygame.Surface, player: Literal["black", "white"]):
        message = font.render(f"{player} move!", 1, font_color)
        window.blit(message, (100, 800))

# Thanks for scrolling 😊