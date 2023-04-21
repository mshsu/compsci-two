from __future__ import annotations

from typing import TextIO

# Add more imports here as you use functions from your hash table.
from hash_table import HashTable, insert, contains, get_item, keys
import string


def djbx33a(s: str) -> int:
    """Returns a modified DJBX33A hash of the given string.

    See the project specification for the formula.
    """
    lst = list(s)
    n = min(len(lst), 8)
    hash_val = 5381 * 33**n
    for i in range(n):
        hash_val += ord(lst[i]) * 33**(n - 1 - i)

    return hash_val


def build_stop_words_table(stop_words_file: TextIO) -> HashTable:
    """Returns a hash table whose keys are the stop words.

    This will read the stop words from the file and add them to the stop
    words table.  The values stored in the table will not matter.

    Args:
        stop_words_file: the open stop words file.

    Returns:
        A hash table whose keys are the stop words.
    """
    stop_table = HashTable(100, djbx33a)
    for word in stop_words_file:
        insert(stop_table, word.strip(), None)

    return stop_table


def build_concordance_table(file: TextIO, stop_table: HashTable) -> HashTable:
    """Returns the concordance table for the given file.

    This will read the given file and build a concordance table
    containing all valid words in the file.

    Args:
        file: the open file to read
        stop_table: a hash table whose keys are the stop words

    Returns:
        A concordance table built from the given file.
    """
    concordance = HashTable(10000, djbx33a)
    lines = file.read()
    lines = lines.lower()
    lines = lines.replace("'", '')
    for symbol in list(string.punctuation):
        lines = lines.replace(symbol, ' ')
    lines = lines.split('\n')
    j = 1
    for line in lines:
        line = line.split()
        for word in line:
            if word.isalpha() is True and contains(stop_table, word) is False:
                try:
                    item = get_item(concordance, word)
                    if j != item[-1]:
                        item.append(j)
                except KeyError:
                    insert(concordance, word, [j])
        j += 1

    return concordance


def write_concordance_table(
        file: TextIO, concordance_table: HashTable) -> None:
    """Writes the concordance table to the given file.

    This will sort the strings in the concordance table alphabetically
    and write them to the given file along with the line numbers on
    which they occurred.

    Args:
        file: the open file in which to store the table
        concordance_table: the concordance table
    """
    strings = keys(concordance_table)
    strings.sort()
    for word in strings:
        lines = ' '.join(map(str, get_item(concordance_table, word)))
        file.write('%s: %s\n' % (word, lines))
