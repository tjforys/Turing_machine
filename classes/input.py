class Input:
    """Input class is responsible for reading the input file and setting the initial values of the tape and header.
    """
    def __init__(self, file):
        """Creates an instance of the Input class. Reads an input file and assigns values inside to its arguments.

        Args:
            file (txt file): Input file containing the inital contents of the turing machine.
        """
        machine_input = file.read().split('\n')
        self._tape_content = machine_input[0].split(', ')
        self._header_content = machine_input[1].split(', ')

    def tape_content(self):
        """Gets the initial tape content from the input file.

        Returns:
            list: List of initial values inside the tape.
        """
        return self._tape_content

    def header_content(self):
        """Gets header content from the input file.

        Returns:
            tuple: Returns a tuple with the position and state of the header.
        """
        return self._header_content

    def header_position(self):
        """Returns integer value of the position of the header on the tape from the input file.

        Returns:
            int: Header position.
        """
        return int(self.header_content()[0])

    def header_state(self):
        """Returns state of the header from the input file.

        Returns:
            str: Header state.
        """
        return self.header_content()[1]
