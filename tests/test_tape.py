from classes.tape import Tape
import pytest


def test_create_Tape_object_success():
    tape = Tape(['a', 'b', 'c', '4'])
    assert type(tape) is Tape


def test_Tape_content_success():
    tape = Tape(['a', 'b', 'c', '4'])
    assert tape.content() == ['a', 'b', 'c', '4']


def test_change_value_success():
    tape = Tape(['a', 'b', 'c', '4'])
    tape.change_value(1, '5')
    assert tape.content() == ['a', '5', 'c', '4']


def test_input_regular_success():
    tape = Tape(['a', 'b', 'c', '4'])
    assert tape.input(1) == "b"


def test_input_negative_success():
    tape = Tape(['a', 'b', 'c', '4'])
    with pytest.raises(IndexError):
        tape.input(-1)


def test_input_over_tape_range_success():
    tape = Tape(['a', 'b', 'c', '4'])
    with pytest.raises(IndexError):
        tape.input(4)
