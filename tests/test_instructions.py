from classes.instructions import Instructions, InstructionsFileEmptyError, InvalidInstructionFileError
from io import StringIO
import pytest


def test_create_instructions_object_success():
    test_instr = StringIO("a, b, c, d, e")
    instr = Instructions(test_instr)
    assert type(instr) is Instructions


def test_command_success():
    test_instr = StringIO("a, b, c, d, e")
    instr = Instructions(test_instr)
    assert instr.command(("a", "b")) == ("c", "d", "e")


def test_content_success():
    test_instr = StringIO("a, b, c, d, e")
    instr = Instructions(test_instr)
    assert instr.content() == {("a", "b"): ("c", "d", "e")}


def test_empty_file():
    file = StringIO("")
    with pytest.raises(InstructionsFileEmptyError):
        instr = Instructions(file)


def test_invalid_file():
    file = StringIO("a, d, c, d, d, g")
    with pytest.raises(InvalidInstructionFileError):
        instr = Instructions(file)
