from enum import Enum


class Directions(str, Enum):
    LEFT = "L"
    RIGHT = "R"


class Head:
    def __init__(self, position, state):
        self._position = position
        self._state = state

    def position(self):
        return self._position

    def state(self):
        return self._state

    def change_state(self, new_state):
        self._state = new_state

    def _move_right(self):
        self._position += 1

    def _move_left(self):
        self._position -= 1

    def move(self, direction):
        if direction == Directions.RIGHT:
            self._move_right()
        elif direction == Directions.LEFT:
            self._move_left()
