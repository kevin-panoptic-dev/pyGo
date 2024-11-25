import pygame
from constants import (
    FPS,
    font,
    font_color,
    title,
    background_color,
    button_font,
    button_color,
    screen_size,
    set_window,
    set_clock,
    terminate,
    first_label_position,
    second_label_position,
)
from pygame.time import Clock


def create_button(
    window: pygame.Surface,
    text: str,
    size: tuple[float, float, float, float],
):
    button = pygame.Rect(*size)
    label = button_font.render(text, 1, font_color)
    font_x = int(size[0] + size[2] / 2 - label.get_width() / 2)
    font_y = int(size[1] + size[3] / 2 - label.get_height() / 2)
    pygame.draw.rect(window, button_color, button, border_radius=5)
    window.blit(label, (font_x, font_y))


def dentro(  # inside
    mouse_position: tuple[int, int], button_position: tuple[float, float, float, float]
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


def open_screen(window: pygame.Surface, button_positions: tuple[tuple, tuple]):
    label = title.render("GO!", 1, font_color)
    description = font.render("Click the buttons to begin", 1, font_color)
    window.fill(background_color)
    window.blit(
        label,
        (
            int(screen_size[0] / 2 - label.get_width() / 2),
            int(screen_size[1] / 2 - label.get_height()),
        ),
    )
    window.blit(
        description,
        (
            int(screen_size[0] / 2 - description.get_width() / 2),
            int(screen_size[1] / 2 + description.get_height()),
        ),
    )
    create_button(window, "Start", button_positions[0])
    create_button(window, "Help", button_positions[1])
    pygame.display.update()


def help_screen(
    window: pygame.Surface, button_position: tuple[float, float, float, float]
):
    window.fill(background_color)
    create_button(window, "return", button_position)
    pygame.display.update()


WIN = set_window()
CLOCK = set_clock()


def open_event(window: pygame.Surface, clock: Clock):
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
                if dentro(position, first_label_position):
                    call_main = True
                    process = False
                elif dentro(position, second_label_position):
                    call_help = True
                    process = False
        open_screen(window, (first_label_position, second_label_position))

    if call_help:
        help_event(window, clock)
    elif call_main:
        ...


def help_event(window: pygame.Surface, clock: Clock):
    process = True
    call_open = False
    while process:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if dentro(position, second_label_position):
                    call_open = True
                    process = False

        help_screen(window, second_label_position)
    if call_open:
        open_event(window, clock)
