from classes.head import Head, Directions


def test_create_object_success():
    header = Head(1, "q0")
    assert header.position() == 1
    assert header.state() == "q0"


def test_change_state_success():
    header = Head(1, "q0")
    header.change_state("q1")
    assert header.state() == "q1"


def test_change_position_general_success():
    header = Head(1, "q0")
    header.move("L")
    assert header.position() == 0
    header.move("R")
    assert header.position() == 1


def test_directions_class():
    assert "R" == Directions.RIGHT
    assert "L" == Directions.LEFT
