class Tape:
    def __init__(self, input):
        self._content = input

    def content(self):
        return self._content

    def change_value(self, position, value):
        self._content[position] = value

    def input(self, position):
        if position < 0:
            raise IndexError
        return self.content()[position]
