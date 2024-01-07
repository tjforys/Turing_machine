class InstructionsFileEmptyError(Exception):
    """Custom error for when the instructions file is empty."""
    pass


class InvalidInstructionFileError(Exception):
    """Custom error for when the instructions file contains invalid data."""
    pass


class Instructions:
    """Instructions class is responsible for reading the instructions file and managing commands according to the input.
    """
    def __init__(self, file):
        """Creates an instance of an Instructions class. Creates a input: command dictionary from a read file.

        Raises:
        InstructionsFileEmptyError: Exception if Instruction file is empty.
        InvalidInstructionFileError: Exception if Instruction file has invalid data.

        Args:
            file (txt file): File containing instructions for the turing machine.
        """
        file_lines = file.read().split("\n")
        if all(line == "" for line in file_lines):
            raise InstructionsFileEmptyError("Instructions file is empty")
        if any(len(line.split(", ")) != 5 for line in file_lines):
            raise InvalidInstructionFileError("Invalid data in instructions file.")
        self._content = {}
        for instruction in file_lines:
            instructions = instruction.split(", ")
            input = (instructions[0], instructions[1])
            output = (instructions[2], instructions[3], instructions[4])
            self._content[input] = output

    def content(self):
        """Gets instruction content.

        Returns:
            dict: Returns a dictionary where the keys are inputs and values are commands.
        """
        return self._content

    def command(self, input):
        """Returns a command matching with the input value and state

        Args:
            input (tuple): Tuple containing the value on the tape and the state of the header.

        Returns:
            tuple: Returns a tuple containing the new value to be put in the tape, a new state of the header, and the direction it should move.
        """
        return self.content()[input]
