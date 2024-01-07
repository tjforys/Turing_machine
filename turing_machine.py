from classes.head import Head
from classes.input import Input
from classes.tape import Tape
from classes.instructions import Instructions
from configparser import ConfigParser
import curses
from curses import wrapper
import argparse


def check_if_continue(stdscr):
    """Function collects user input whether to stop the program.

    Returns:
        Bool: Information whether the user decided to stop the program.
    """
    while True:
        if_continue = stdscr.getstr(3, 0).decode()
        stdscr.refresh()
        if if_continue == "n":
            stdscr.move(4, 0)
            stdscr.clrtoeol()
            stdscr.addstr(3, 0, "The program has been stopped")
            stdscr.getch()
            return True
        elif if_continue == "Y" or if_continue == "y" or if_continue == "":
            return False
        else:
            stdscr.move(3, 0)
            stdscr.clrtoeol()
            stdscr.addstr(4, 0, "Wrong input detected, try again.")


def write_output(content):
    """Function outputs machine content to an output file.

    Args:
        content (any): Content to be written to the output file.
    """
    with open(machine_output, "w", encoding="utf8") as f:
        f.write(str(content))


def turing_instant(stdscr, color):
    """Instantly goes through all the steps of the machine. Writes the output in the curses terminal. Writes to the output file.

    Args:
        color (curses.color_pair): Colors to distinguish the latest changed value in the tape.
    """
    move_cap = int(config["move_cap"]["instant_cap"])
    move_count = 0
    stdscr.clear()
    stdscr.addstr("Start values: ")
    write_tape_content(stdscr, header.position(), color)
    last_pos = None
    while True:
        try:
            instr_input = (tape.input(header.position()), header.state())
        except IndexError:
            stdscr.addstr(1, 0, "End values:   ")
            write_tape_content(stdscr, color, last_pos)
            stdscr.addstr(2, 0, f"Header: {(header.position(), header.state())}")
            stdscr.addstr(3, 0, "Program reached the end")
            stdscr.getch()
            if not args.no_write:
                write_output(
                    f'{tape.content()} {(header.position(), header.state())}')
            break
        try:
            new_value, new_state, direction = instructions.command(instr_input)
        except KeyError:
            stdscr.addstr(3, 0, f'Command not found for {instr_input} input')
            stdscr.getch()
            break
        if move_count > move_cap:
            stdscr.addstr(1, 0, f"Move count exceeded {move_cap}, program closed")
            stdscr.getch()
            break
        last_pos = header.position()
        tape.change_value(header.position(), new_value)
        header.change_state(new_state)
        header.move(direction)
        move_count += 1


def write_tape_content(stdscr, color, last_pos):
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


def turing_steps(stdscr, color):
    """Goes through the turing machine step by step, writing evry one in the curses terminal. Writes to the output file.

    Args:
        color (curses.color_pair): Colors to distinguish the latest changed value in the tape.
    """
    last_pos = None
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Values: ")
        write_tape_content(stdscr, color, last_pos)
        stdscr.addstr(1, 0, f"Header: {(header.position(), header.state())}")
        stdscr.addstr(2, 0, "Continue to next line? [Y/n]")
        # print(f'{tape.content()} {(header.position(), header.state())}')
        try:
            instr_input = (tape.input(header.position()), header.state())
        except IndexError:
            stdscr.addstr(3, 0, "Program reached the end")
            stdscr.refresh()
            stdscr.getch()
            if not args.no_write:
                write_output(
                    f'{tape.content()} {(header.position(), header.state())}')
            break
        try:
            new_value, new_state, direction = instructions.command(instr_input)
        except KeyError:
            stdscr.addstr(3, 0, f'Command not found for {instr_input} input')
            stdscr.getch()
            break

        tape.change_value(header.position(), new_value)
        last_pos = header.position()
        header.change_state(new_state)
        header.move(direction)
        if check_if_continue(stdscr):
            if not args.no_write:
                write_output(tape.content())
            break


def terminal_writing(stdscr):
    """Main function of the machine. Distinguishes between instand and step-by-step mode of the machine. Creates the curses terminal.
    """
    stdscr.clear()
    stdscr.refresh()
    curses.echo()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    RED_BLACK = curses.color_pair(1)
    if args.instant:
        turing_instant(stdscr, RED_BLACK)
    else:
        turing_steps(stdscr, RED_BLACK)


if __name__ == "__main__":
    config = ConfigParser()
    config.read("config.ini")
    machine_input = config["filepaths"]["machine_input"]
    machine_instructions = config["filepaths"]["machine_instructions"]
    machine_output = config["filepaths"]["machine_output"]
    instructions = Instructions(open(machine_instructions, "r"))
    file_input = Input(open(machine_input, "r"))
    tape = Tape(file_input.tape_content())
    header = Head(file_input.header_position(), file_input.header_state())
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--instant",
                        help="instantly gives end result and writes to a file",
                        action="store_true")
    parser.add_argument("-nw", "--no_write",
                        help="disables writing result to output file",
                        action="store_true")
    args = parser.parse_args()
    wrapper(terminal_writing)
