from enum import Enum


class Directions(str, Enum):
    """Direction is an enum class containing the text representation of the directions the header can move. The str parent class makes it possible to compare the enum instances and the command text.
    """
    LEFT = "L"
    RIGHT = "R"


class Head:
    """The Head class is responsible for controlling the header wchich travles on the tape and changes values inside it.
    """
    def __init__(self, position, state):
        """Creates an instance of the Head class.

        Args:
            position (int): Initial position of the header.
            state (str): initial state of the header.
        """
        self._position = position
        self._state = state

    def position(self):
        """Gets the position of the header.

        Returns:
            int: Position of the header.
        """
        return self._position

    def state(self):
        """Gets the state of the header.

        Returns:
            str: State of the header.
        """
        return self._state

    def change_state(self, new_state):
        """Changes the state of the header to a new given state.

        Args:
            new_state (str): New state that the header will change to.
        """
        self._state = new_state

    def _move_right(self):
        """Moves the header to the right on the tape."""
        self._position += 1

    def _move_left(self):
        """Moves the header to the left on the tape."""
        self._position -= 1

    def move(self, direction):
        """Checks the direction and moves the header accordingly.

        Args:
            direction (str): Direction taken from the instruction command indicating the movement of the header.
        """
        if direction == Directions.RIGHT:
            self._move_right()
        elif direction == Directions.LEFT:
            self._move_left()
