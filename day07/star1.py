import re
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


# Create enum with two values : DIR and FILE
class NodeType(Enum):
    DIR = 1
    FILE = 2


@dataclass
class INode:
    name: str
    type: NodeType
    size: int
    children: List['INode']
    parent: Optional['INode']

    create_dir = lambda name, parent: INode(name, NodeType.DIR, 0, [], parent)
    create_file = lambda name, size, parent: INode(name, NodeType.FILE, size, [], parent)


def compute_fs_size(folder_structure: INode) -> None:
    for child in folder_structure.children:
        if child.type == NodeType.DIR:
            compute_fs_size(child)
        folder_structure.size += child.size


def compute_deletable_files(folder_structure: INode) -> int:
    deletable_size = 0
    if folder_structure.type == NodeType.FILE:
        return 0
    else:
        for child in folder_structure.children:
            deletable_size += compute_deletable_files(child)

        if folder_structure.size <= 100000:
            deletable_size += folder_structure.size

        return deletable_size


with open("./input.txt", "r") as f:
    data = f.read().splitlines()

    # Compile a regex to match a command of the form "$ cd X" with X being "/", ".." or a string of characters
    cd = re.compile(r"^\$ cd (/|..|[a-zA-Z0-9]+)$")
    dir = re.compile(r"^dir ([a-zA-Z0-9]+)$")
    file = re.compile(r"^([0-9]+) ([a-zA-Z0-9.]+)$")

    folder_structure = INode.create_dir("/", None)
    current_folder = folder_structure

    for line in data:
        if cd.match(line):
            # If the command is a cd command, get the folder name
            folder = cd.match(line).group(1)

            if folder == "/":
                # If the folder is the root, go back to the root
                current_folder = folder_structure

            elif folder == "..":
                # If the folder is "..", go up one level
                current_folder = current_folder.parent

            else:
                # If the folder is a name, check if it exists in the current folder
                for child in current_folder.children:
                    if child.name == folder:
                        current_folder = child
                        break

        if dir.match(line):
            # If the command is a dir command, get the folder name
            folder = dir.match(line).group(1)

            new_folder = INode.create_dir(folder, current_folder)
            current_folder.children.append(new_folder)

        if file.match(line):
            # If the command is a file command, get the size and name
            size, name = file.match(line).groups()

            # Create the file and add it to the current folder
            new_file = INode.create_file(name, int(size), current_folder)
            current_folder.children.append(new_file)

    # Get the total size of the folder structure
    compute_fs_size(folder_structure)

    print(folder_structure.children[0])

    print(compute_deletable_files(folder_structure))
