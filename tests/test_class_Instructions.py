from classes.class_Instructions import Instructions
from io import StringIO


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
