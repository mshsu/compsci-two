from __future__ import annotations

from typing import Optional, TextIO
from ordered_list import OrderedList, insert, size, is_empty, pop, get


# Project 3a
class HuffmanNode:
    """Represents a node in a Huffman tree.

    Attributes:
        char: The character as an integer ASCII value
        frequency: The frequency of the character in the file
        left: The left Huffman sub-tree
        right: The right Huffman sub-tree
    """
    def __init__(
            self,
            char: int,
            frequency: int,
            left: Optional[HuffmanNode] = None,
            right: Optional[HuffmanNode] = None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    def __eq__(self, other) -> bool:
        """Returns True if and only if self and other are equal."""
        return (self.char == other.char and
                self.frequency == other.frequency and
                self.left == other.left and
                self.right == other.right)

    def __lt__(self, other) -> bool:
        """Returns True if and only if self < other."""
        if self.frequency == other.frequency:
            return self.char < other.char
        return self.frequency < other.frequency


def count_frequencies(file: TextIO) -> list[int]:
    """Reads the given file and counts the frequency of each character.

    The resulting Python list will be of length 256, where the indices
    are the ASCII values of the characters, and the value at a given
    index is the frequency with which that character occured.
    """
    frequencies = [0] * 256
    chars = list(file.read())
    for char in chars:
        frequencies[ord(char)] += 1
    return frequencies


def build_huffman_tree(frequencies: list[int]) -> Optional[HuffmanNode]:
    """Creates a Huffman tree of the characters with non-zero frequency.

    Returns the root of the tree.
    """
    trees = OrderedList()
    for i in range(len(frequencies)):
        if frequencies[i] != 0:
            tree_node = HuffmanNode(i, frequencies[i])
            insert(trees, tree_node)

    while size(trees) > 1:
        tree_1 = pop(trees, 0)
        tree_2 = pop(trees, 0)
        new_node = HuffmanNode(min(tree_1.char, tree_2.char),
                               tree_1.frequency + tree_2.frequency,
                               tree_1, tree_2)
        insert(trees, new_node)

    if is_empty(trees):
        return None
    return get(trees, 0)


def create_codes(tree: Optional[HuffmanNode]) -> list[str]:
    """Traverses the tree creating the Huffman code for each character.

    The resulting Python list will be of length 256, where the indices
    are the ASCII values of the characters, and the value at a given
    index is the Huffman code for that character.
    """
    codes = [''] * 256
    for i in range(len(codes)):
        codes[i] = make_code(tree, i)
    return codes


def search_htree(tree: Optional[HuffmanNode], char: int) -> bool:
    """Finds a char ASCII value in a given tree.

    Helper function for make_code and create_codes.
    """
    if tree is None:
        return False
    elif tree.char == char:
        return True
    else:
        return search_htree(tree.left, char) or search_htree(tree.right, char)


def make_code(tree: Optional[HuffmanNode], char: int,
              code: str = '') -> str:
    """Makes the encoding for a given ASCII value, given a Huffman tree.

    Helper function for create_codes.
    """
    if search_htree(tree, char) is False:
        return ''
    elif tree.char == char and tree.left is None and tree.right is None:
        return ''
    elif (tree.left.char == char and
          tree.left.left is None and
          tree.left.right is None):
        return code + '0'
    elif (tree.right.char == char and
          tree.right.left is None and
          tree.right.right is None):
        return code + '1'
    elif search_htree(tree.left, char):
        return make_code(tree.left, char, code + '0')
    elif search_htree(tree.right, char):
        return make_code(tree.right, char, code + '1')


def create_header(frequencies: list[int]) -> str:
    """Returns the header for the compressed Huffman data.

    For example, given the file "aaabbbbcc", this would return:
    "97 3 98 4 99 2"
    """
    header = []
    for i in range(len(frequencies)):
        if frequencies[i] != 0:
            header.append(str(i))
            header.append(str(frequencies[i]))

    return ' '.join(header)


def huffman_encode(in_file: TextIO, out_file: TextIO) -> None:
    """Encodes the data in the input file, writing the result to the
    output file.
    """
    frequencies = count_frequencies(in_file)
    header = create_header(frequencies)
    out_file.write(header + '\n')

    hm_tree = build_huffman_tree(frequencies)
    codes = create_codes(hm_tree)

    in_file.seek(0)
    chars = list(in_file.read())
    hm_encode = []
    for char in chars:
        hm_encode.append(codes[ord(char)])
    hm_encode = ''.join(hm_encode)
    out_file.write(hm_encode)


# Project 3b
def parse_header(header: str) -> list[int]:
    """Takes as an argument a string (the first line of the file) and returns
    a list of frequencies.

    The list of frequencies should be in the same form at that
    count_frequencies returned in the first part of the assignment,
    i.e., a list with 256 entries, indexed by the ASCII value of the
    characters.
    """
    header = [int(item) for item in header.split()]

    frequencies = [0] * 256

    for i in range(0, len(header), 2):
        frequencies[header[i]] = header[i + 1]

    return frequencies


def huffman_decode(in_file: TextIO, out_file: TextIO) -> None:
    """Takes as arguments two already open files (for the input and output),
    decodes the input file, and stores the resulting decoded data in the
    output file.

    This will be done by parsing the first line, then building the
    Huffman tree (using functions you’ve already written), and now
    recreating the original file one character at a time using the
    tree traversing method described above.
    """
    frequencies = parse_header(in_file.readline())
    hm_tree = build_huffman_tree(frequencies)
    code = list(in_file.readline())

    hm_decode = ''
    if hm_tree is None:
        hm_decode = ''
    elif hm_tree.left is None and hm_tree.right is None and code == []:
        hm_decode = hm_decode + (chr(hm_tree.char) * hm_tree.frequency)
    else:
        pointer = hm_tree
        for item in code:
            if item == '0':
                pointer = pointer.left
            elif item == '1':
                pointer = pointer.right
            if pointer.right is None and pointer.left is None:
                hm_decode = hm_decode + chr(pointer.char)
                pointer = hm_tree

    out_file.write(hm_decode)
