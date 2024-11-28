from typing import Literal


class algorithm:
    def __init__(self, size: int) -> None:
        self.board: list[list[str]] = list(
            ["empty" for _ in range(size)] for _ in range(size)
        )
        self.size: int = size

    def __is_vacant(self, x: int, y: int) -> bool:
        return self.board[x][y] == "empty"

    def __is_downfall(self, x: int, y: int) -> bool:
        return not (0 <= x < self.size) or not (0 <= y < self.size)

    def __adjacent(self, x: int, y: int) -> list:
        return list(
            (x + appendage_x, y + appendage_y)
            for appendage_x, appendage_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if not self.__is_downfall(x + appendage_x, y + appendage_y)
        )

    def __remove_group(self, group: list) -> None:
        for x, y in group:
            self.board[x][y] = "empty"

    def __cohort(
        self, x: int, y: int, player: Literal["black", "white"]
    ) -> tuple[int, list]:
        visited: set = set()
        cohort: list = []
        waiting: list[tuple[int, int]] = [(x, y)]
        liberties = 0
        self.board[x][y] = player
        while waiting:
            x, y = waiting.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            cohort.append((x, y))
            for next_x, next_y in self.__adjacent(x, y):
                if self.board[next_x][next_y] == "empty":
                    liberties += 1
                elif self.board[next_x][next_y] == player:
                    waiting.append((next_x, next_y))

        return (liberties, cohort)

    def __suicide(
        self, x: int, y: int, player: Literal["black", "white"]
    ) -> (
        tuple[Literal[False], None]
        | tuple[Literal[False], list]
        | tuple[Literal[True], None]
    ):
        liberties, _ = self.__cohort(x, y, player)
        if liberties:
            # quick check: the stone is not suicide, nothing to remove
            return (False, None)
        else:
            if player == "black":
                result: list = self.__switch(x, y, "white")
            else:
                result: list = self.__switch(x, y, "black")

            if len(result):
                # switch to check enemy condition: the stone is not suicide by removing the enemies.
                return (False, result)

        # suicide condition: the stone is suicide, nothing to remove
        return (True, None)

    def __switch(
        self, this_x: int, this_y: int, enemy: Literal["black", "white"]
    ) -> list:
        danger_enemies: list = []
        for enemy_x, enemy_y in self.__adjacent(this_x, this_y):
            if self.board[enemy_x][enemy_y] != enemy:
                continue
            liberties, group = self.__cohort(enemy_x, enemy_y, enemy)
            if not liberties:
                danger_enemies.extend(group)

        return danger_enemies

    def main(
        self, x: int, y: int, player: Literal["black", "white"]
    ) -> (
        Literal["arrogate"]
        | Literal["downfall"]
        | Literal["suicide"]
        | Literal["success"]
    ):
        """
        The algorithm first check for `arrogate`,if it's arrogate -> return "arrogate".
        The algorithm also check for `downfall`, if it's downfall -> return "downfall".
        Then it checks for `suicide`: {
            `case 1`: suicide -> return "suicide"
            `case 2`: quick check -> not suicide, pass
            `case 3`: not suicide, return the search result -> place stone and remove enemies.
        }
        Next it places the stone.
        Finally use `switch` to check for the removable enemies.
        -> return "success"

        Args:
            x (int): x coordinate
            y (int): y coordinate
            player: "black" | "white: player
        """
        if self.__is_downfall(x, y):
            return "downfall"
        if not self.__is_vacant(x, y):
            return "arrogate"
        suicide, removable_enemies = self.__suicide(x, y, player)
        if suicide:
            return "suicide"

        if removable_enemies is not None:
            self.__remove_group(removable_enemies)
            return "success"

        if player == "black":
            removable_enemies = self.__switch(x, y, "white")
        else:
            removable_enemies = self.__switch(x, y, "black")
        if len(removable_enemies):
            self.__remove_group(removable_enemies)

        return "success"

    def __iadd__(self, stone: tuple[int, int, Literal["white", "black"]]):
        self.board[stone[0]][stone[1]] = stone[2]
        return self

    def __isub__(self, stone: tuple[int, int, Literal["white", "black"]]):
        if self.board[stone[0]][stone[1]] == stone[2]:
            self.board[stone[0]][stone[1]] = "empty"
            return self
        raise ValueError("Invalid suicide remove")

    @property
    def get(self) -> list:
        return self.board

    @property
    def restart(self) -> None:
        self.board = list(["empty" for _ in range(self.size)] for _ in range(self.size))


# Thanks for scrolling 😊
