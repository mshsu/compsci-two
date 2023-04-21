from __future__ import annotations

from collections.abc import Callable
from typing import Any, List, Tuple


# An entry in the hash table is a key-value pair
HashEntry = Tuple[Any, Any]
# Each entry in the hash table array will be a list of HashEntry pairs
HashChain = List[HashEntry]


class HashTable:
    """A hash table with separate chaining."""
    def __init__(
            self,
            capacity: int = 10,
            hash_function: Callable[[Any], int] = hash):
        """Creates an empty hash table.

        Args:
            capacity:
                The initial capacity of the backing array.  The default
                capacity is 10.
            hash_function:
                The function to use to compute hash values for the given
                keys.  The default hash function is the Python builtin
                hash function.
        """
        self.table: list[HashChain] = [[] for _ in range(capacity)]

        self.size: int = 0
        self.capacity: int = capacity
        self.hash_function = hash_function


def insert(hash_table: HashTable, key: Any, value: Any) -> None:
    key_num = hash_table.hash_function(key) % hash_table.capacity

    inserted = False
    for i in range(len(hash_table.table[key_num])):
        if hash_table.table[key_num][i][0] == key:
            hash_table.table[key_num][i] = (key, value)
            inserted = True
            break
    if not inserted:
        hash_table.table[key_num].append((key, value))
        hash_table.size += 1

    if load_factor(hash_table) > 1.0:
        new_hash = HashTable(hash_table.capacity * 2,
                             hash_table.hash_function)
        for chain in hash_table.table:
            for item in chain:
                insert(new_hash, item[0], item[1])
        hash_table.table = new_hash.table
        hash_table.capacity = new_hash.capacity


def get_item(hash_table: HashTable, key: Any) -> Any:
    key_num = hash_table.hash_function(key) % hash_table.capacity
    for item in hash_table.table[key_num]:
        if item[0] == key:
            return item[1]

    raise KeyError


def contains(hash_table: HashTable, key: Any) -> bool:
    key_num = hash_table.hash_function(key) % hash_table.capacity
    for item in hash_table.table[key_num]:
        if item[0] == key:
            return True

    return False


def remove(hash_table: HashTable, key: Any) -> tuple[Any, Any]:
    key_num = hash_table.hash_function(key) % hash_table.capacity
    for i in range(len(hash_table.table[key_num])):
        if hash_table.table[key_num][i][0] == key:
            value = hash_table.table[key_num].pop(i)
            hash_table.size -= 1
            return value

    raise KeyError


def size(hash_table: HashTable) -> int:
    return hash_table.size


def keys(hash_table: HashTable) -> list[Any]:
    keys = []
    for chain in hash_table.table:
        for item in chain:
            keys.append(item[0])

    return keys


def load_factor(hash_table: HashTable) -> float:
    return hash_table.size / hash_table.capacity


def _contents(hash_table: HashTable) -> list[HashChain]:
    return hash_table.table
