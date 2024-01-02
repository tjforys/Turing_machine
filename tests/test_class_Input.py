from classes.class_Input import Input
from io import StringIO


def test_input_create_object_success():
    test_input = StringIO("a, b, c, 56, lol\n3, q0")
    file_input = Input(test_input)
    assert type(file_input) is Input


def test_tape_content_success():
    test_input = StringIO("a, b, c, 56, lol\n3, q0")
    file_input = Input(test_input)
    assert file_input.tape_content() == ['a', 'b', 'c', '56', 'lol']


def test_header_content_success():
    test_input = StringIO("a, b, c, 56, lol\n3, q0")
    file_input = Input(test_input)
    assert file_input.header_content() == ['3', 'q0']
    assert file_input.header_position() == 3
    assert file_input.header_state() == 'q0'
