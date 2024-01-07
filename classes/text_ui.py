class TextUi:
    """Class of functions with the purpose of displaying text in the curses terminal."""
    def program_stop_message(stdscr):
        """Creates the display of the program stop message when checking whetehr to continue the program in step-by-step mode of the machine."""
        stdscr.move(4, 0)
        stdscr.clrtoeol()
        stdscr.addstr(3, 0, "The program has been stopped")
        stdscr.getch()

    def wrong_input_message(stdscr):
        """Creates the display for the wrong input message when checking whether to continue the mahcine in step-by-step mode."""
        stdscr.move(3, 0)
        stdscr.clrtoeol()
        stdscr.addstr(4, 0, "Wrong input detected, try again.")

    def instant_end_message(stdscr, color, last_pos, tape, header):
        """Creates the display for the end values of the instant mode of the machine."""
        stdscr.addstr(1, 0, "End values:   ")
        write_tape_content(stdscr, color, last_pos, tape)
        stdscr.addstr(2, 0, f"Header: {(header.position(), header.state())}")
        stdscr.addstr(3, 0, "Program reached the end")
        stdscr.getch()

    def instant_start_message(stdscr, header, color, tape):
        """Creates the display for the initial values of the instant mode of the machine."""
        stdscr.clear()
        stdscr.addstr("Start values: ")
        write_tape_content(stdscr, header.position(), color, tape)

    def steps_content_message(stdscr, color, last_pos, tape, header):
        """Creates the display for the step-by-step mode of the machine."""
        stdscr.clear()
        stdscr.addstr(0, 0, "Values: ")
        write_tape_content(stdscr, color, last_pos, tape)
        stdscr.addstr(1, 0, f"Header: {(header.position(), header.state())}")
        stdscr.addstr(2, 0, "Continue to next line? [Y/n]")


def write_tape_content(stdscr, color, last_pos, tape):
    """Writes tape content in the curses terminal.

    Args:
        color (curses.color_pair): Colors to distinguish the latest changed value in the tape.
        last_pos (int): Position of the last changed value in the tape.
    """
    stdscr.addstr('[')
    for item_id, item in enumerate(tape.content()):
        if item_id == last_pos:
            stdscr.addstr(item, color)
        else:
            stdscr.addstr(item)
        if item_id != len(tape.content())-1:
            stdscr.addstr(", ")
    stdscr.addstr("]")