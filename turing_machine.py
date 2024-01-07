from classes.head import Head
from classes.input import Input
from classes.tape import Tape
from classes.instructions import Instructions
from configparser import ConfigParser
import curses
from curses import wrapper
import argparse
from classes.text_ui import TextUi


def check_if_continue(stdscr):
    """Function collects user input whether to stop the program.

    Returns:
        Bool: Information whether the user decided to stop the program.
    """
    while True:
        if_continue = stdscr.getstr(3, 0).decode()
        if if_continue == "n":
            TextUi.program_stop_message(stdscr=stdscr)
            return True
        elif if_continue == "Y" or if_continue == "y" or if_continue == "":
            return False
        else:
            TextUi.wrong_input_message(stdscr=stdscr)


def write_output(content, machine_output):
    """Function outputs machine content to an output file.

    Args:
        content (any): Content to be written to the output file.
    """
    with open(machine_output, "w", encoding="utf8") as f:
        f.write(str(content))


def turing_instant(stdscr, color, instructions, header, tape, machine_output, args, config):
    """Instantly goes through all the steps of the machine. Writes the output in the curses terminal. Writes to the output file.

    Args:
        color (curses.color_pair): Colors to distinguish the latest changed value in the tape.
        instructions (classInstructions): Instructions class instance conatining instructions for the machine.
        header (classHead): The turing machine's header moving on the tape.
        tape (classTape): The turing machine's tape.
        machine_output (str): Target destination to the output file.
        args : Arguments given in the terminal.
        config: Configurations regarding the working of the machine.
    """
    move_cap = int(config["move_cap"]["instant_cap"])
    move_count = 0
    TextUi.instant_start_message(stdscr=stdscr,
                                 header=header,
                                 color=color,
                                 tape=tape)
    last_pos = None
    while True:
        try:
            instr_input = (tape.input(header.position()), header.state())
        except IndexError:
            TextUi.instant_end_message(stdscr=stdscr,
                                       color=color,
                                       last_pos=last_pos,
                                       tape=tape,
                                       header=header
                                       )
            if not args.no_write:
                write_output(
                    f'{tape.content()} {(header.position(), header.state())}',
                    machine_output)
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


def turing_steps(stdscr, color, instructions, header, tape, machine_output, args):
    """Goes through the turing machine step by step, writing every one in the curses terminal. Writes to the output file.

    Args:
        color (curses.color_pair): Colors to distinguish the latest changed value in the tape.
        instructions (classInstructions): Instructions class instance conatining instructions for the machine.
        header (classHead): The turing machine's header moving on the tape.
        tape (classTape): The turing machine's tape.
        machine_output (str): Target destination to the output file.
        args : Arguments given in the terminal.
    """
    last_pos = None
    while True:
        TextUi.steps_content_message(stdscr=stdscr,
                                     color=color,
                                     last_pos=last_pos,
                                     tape=tape,
                                     header=header)
        try:
            instr_input = (tape.input(header.position()), header.state())
        except IndexError:
            stdscr.addstr(3, 0, "Program reached the end")
            stdscr.getch()
            if not args.no_write:
                write_output(
                    f'{tape.content()} {(header.position(), header.state())}',
                    machine_output)
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
                write_output(tape.content(), machine_output)
            break


def terminal_writing(stdscr):
    """Main function of the machine. Distinguishes between instand and step-by-step mode of the machine. Creates the curses terminal.
    """
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

    stdscr.clear()
    stdscr.refresh()
    curses.echo()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    RED_BLACK = curses.color_pair(1)

    if args.instant:
        turing_instant(stdscr=stdscr,
                       color=RED_BLACK,
                       instructions=instructions,
                       header=header,
                       tape=tape,
                       machine_output=machine_output,
                       args=args,
                       config=config)
    else:
        turing_steps(stdscr=stdscr,
                     color=RED_BLACK,
                     instructions=instructions,
                     header=header,
                     tape=tape,
                     machine_output=machine_output,
                     args=args)


if __name__ == "__main__":
    wrapper(terminal_writing)
