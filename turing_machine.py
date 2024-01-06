from classes.class_Head import Head
from classes.class_Input import Input
from classes.class_Tape import Tape
from classes.class_Instructions import Instructions
from configparser import ConfigParser
import argparse


def check_if_continue():
    while True:
        if_continue = input("Continue to next line? [Y/n]: ")
        if if_continue == "n":
            print("The program has been stopped")
            return True
        elif if_continue == "Y" or if_continue == "y" or if_continue == "":
            return False
        else:
            print("Wrong input detected, try again.")


def write_output(content):
    with open(machine_output, "w", encoding="utf8") as f:
        f.write(str(content))


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
    args = parser.parse_args()
    if args.instant:
        while True:
            try:
                instr_input = (tape.input(header.position()), header.state())
            except IndexError:
                print(
                    f'{tape.content()} {(header.position(),header.state())}')
                write_output(
                    f'{tape.content()} {(header.position(), header.state())}')
                break
            try:
                new_value, new_state, direction = instructions.command(instr_input)
            except KeyError:
                print(f'Command not found for {instr_input} input')
                break

            tape.change_value(header.position(), new_value)
            header.change_state(new_state)
            header.move(direction)

    else:
        while True:
            print(f'{tape.content()} {(header.position(), header.state())}')
            try:
                instr_input = (tape.input(header.position()), header.state())
            except IndexError:
                print("Program reached the end")
                write_output(
                    f'{tape.content()} {(header.position(), header.state())}')
                break
            try:
                new_value, new_state, direction = instructions.command(instr_input)
            except KeyError:
                print(f'Command not found for {instr_input} input')
                break

            tape.change_value(header.position(), new_value)
            header.change_state(new_state)
            header.move(direction)
            if check_if_continue():
                write_output(tape.content())
                break
