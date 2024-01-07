from classes.input import Input, InputFileEmptyError, InvalidInputFileError
from io import StringIO
import pytest


def test_input_create_object_success():
    test_input = StringIO("a, b, c, 56, d\n3, q0")
    file_input = Input(test_input)
    assert type(file_input) is Input


def test_tape_content_success():
    test_input = StringIO("a, b, c, 56, d\n3, q0")
    file_input = Input(test_input)
    assert file_input.tape_content() == ['a', 'b', 'c', '56', 'd']


def test_header_content_success():
    test_input = StringIO("a, b, c, 56, d\n3, q0")
    file_input = Input(test_input)
    assert file_input.header_content() == ['3', 'q0']
    assert file_input.header_position() == 3
    assert file_input.header_state() == 'q0'


def test_file_empty():
    file = StringIO("")
    with pytest.raises(InputFileEmptyError):
        file_input = Input(file)


def test_file_one_line():
    file = StringIO("abc")
    with pytest.raises(InvalidInputFileError):
        file_input = Input(file)


def test_file_single_header_line():
    file = StringIO("a, b, c, d\na")
    with pytest.raises(InvalidInputFileError):
        instr = Input(file)
