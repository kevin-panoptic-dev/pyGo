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
)


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


def open_screen(window: pygame.Surface, buttons: tuple[tuple, tuple]):
    label = title.render("GO!", 1, font_color)
    description = font.render("Click the buttons to begin", 1, font_color)
    window.fill(background_color)
    create_button(window, "Start", buttons[0])
    create_button(window, "Help", buttons[1])
    pygame.display.update()


WIN = set_window()
CLOCK = set_clock()

while True:
    CLOCK.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

    open_screen(WIN, ((100, 100, 100, 100), (500, 500, 100, 100)))
