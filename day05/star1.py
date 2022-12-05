import re
from dataclasses import dataclass


@dataclass
class Instruction:
    how_many: int
    origin: int
    destination: int


def parse_initial_state(lines):
    nb_stacks = len(lines[-1]) // 4 + 1
    stacks = [[] for _ in range(nb_stacks)]
    nb_lines = len(lines)
    for i in range(nb_lines - 2, -1, -1):
        for j in range(nb_stacks):
            if 4*j+1 < len(lines[i]) and lines[i][4*j+1] != " ":
                stacks[j].append(lines[i][4*j+1])
    return stacks


def parse_instructions(lines):
    # Compile a regex to parse instructions "Move X from A to B" with X and A and B being integers
    regex = re.compile(r"move (\d+) from (\d+) to (\d+)")
    move_instructions = [Instruction(*map(int, regex.match(line).groups())) for line in lines]
    return move_instructions


with open("./input.txt", 'r') as f:
    data = f.readlines()
    # Initial state
    separator = data.index('\n')
    stacks = parse_initial_state(data[:separator])
    instructions = parse_instructions(data[separator + 1:])
    # Apply instructions

    for instruction in instructions:
        for _ in range(instruction.how_many):
            stacks[instruction.destination-1].append(stacks[instruction.origin-1].pop())

    # Print top of stacks
    print("".join([stack[-1] for stack in stacks]))