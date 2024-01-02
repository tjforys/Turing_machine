class Input:
    def __init__(self, file):
        machine_input = file.read().split('\n')
        self._tape_content = machine_input[0].split(', ')
        self._header_content = machine_input[1].split(', ')

    def tape_content(self):
        return self._tape_content

    def header_content(self):
        return self._header_content

    def header_position(self):
        return int(self.header_content()[0])

    def header_state(self):
        return self.header_content()[1]
