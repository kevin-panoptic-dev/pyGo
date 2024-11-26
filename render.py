from constants import (
    background_color,
    message_font,
    middle_label_position,
    confirm_label_position,
    font_color,
    set_clock,
    terminate,
    FPS,
    set_window,
)
from pymodule import metaclarion, circulis
from pymodule.utility import prismelt
import pygame
from pygame.time import Clock
from typing import Literal


class interface(metaclass=metaclarion):
    @classmethod
    def raise_warning(
        cls,
        window: pygame.Surface,
        warning: str,
        size: tuple[float, float, float, float],
        color: tuple[int, int, int],
    ) -> None:
        button = pygame.Rect(*size)
        label: pygame.Surface = message_font.render(warning, 1, font_color)
        font_x = int(size[0] + size[2] / 2 - label.get_width() / 2)
        font_y = int(size[1] + size[3] / 2 - label.get_height() / 2)
        pygame.draw.rect(window, color, button, border_radius=5)
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
        warning_type: Literal["suicide", "arrogate", "downfall"],
    ) -> None:
        if warning_type == "suicide":
            message = (
                "Place the stone in place where is surrounded by enemies is invalid."
            )
        elif warning_type == "arrogate":
            message = "Cannot place the stone above another stone"
        elif warning_type == "downfall":
            message = "Place the stone outside the boundary is invalid"

        background = window.copy()
        window.blit(background, (0, 0))
        cls.raise_warning(window, message, middle_label_position, (0, 0, 255))
        cls.raise_warning(window, "OK", confirm_label_position, (0, 255, 0))
        pygame.display.update()

    @classmethod
    def warning_event(
        cls,
        window: pygame.Surface,
        clock: Clock,
        warning_type: Literal["suicide", "arrogate", "downfall"],
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
        ...  # return to main loop


WIN = set_window()
clock = set_clock()
interface.warning_event(WIN, clock, "suicide")
