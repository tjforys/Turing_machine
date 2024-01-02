class Instructions:
    def __init__(self, file):
        file_lines = file.read().split("\n")
        self._content = {}
        for instruction in file_lines:
            instructions = instruction.split(", ")
            input = (instructions[0], instructions[1])
            output = (instructions[2], instructions[3], instructions[4])
            self._content[input] = output

    def content(self):
        return self._content

    def command(self, input):
        return self.content()[input]
