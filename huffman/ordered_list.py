from __future__ import annotations

from typing import Any, Optional


class Node:
    """Represents a node to be used in a doubly linked list."""
    def __init__(
            self,
            value: Any,
            prev: Optional[Node] = None,
            nxt: Optional[Node] = None):
        self.value = value

        # NOTE: This means that if prev and nxt are None, self.prev and
        # self.next will be self.  You may find this useful.  This means
        # that self.prev and self.next aren't Optional Nodes, they are
        # always Nodes.
        self.prev: Node = prev or self
        self.next: Node = nxt or self


class OrderedList:
    """A circular, doubly linked list of items, from lowest to highest.

    The contents of the list *must* have a accurate notation of less
    than and of equality.  That is to say, the contents of the list must
    implement both __lt__ and __eq__.  This *does not* mean that your
    OrderedList (or your Nodes) should have __lt__ and __eq__.

    Your implementation should use a single dummy node as the "head".
    """
    def __init__(self):
        self.head = Node(None)
        self.size = 0


def insert(lst: OrderedList, value: Any) -> None:
    """Inserts the value into the list in the proper (ordered) location."""
    lst.size += 1

    while lst.head.next.value is not None and lst.head.next.value < value:
        lst.head = lst.head.next

    new_node = Node(value, lst.head, lst.head.next)
    lst.head.next.prev = new_node
    lst.head.next = new_node

    while lst.head.value is not None:
        lst.head = lst.head.next


def remove(lst: OrderedList, value: Any) -> None:
    """Removes the first occurrence of value from the list.

    Raises ValueError if the value is not present.
    """
    if contains(lst, value) is False:
        raise ValueError

    while lst.head.next.value != value:
        lst.head = lst.head.next

    lst.head.next.next.prev = lst.head
    lst.head.next = lst.head.next.next

    while lst.head.value is not None:
        lst.head = lst.head.next

    lst.size -= 1


def contains(lst: OrderedList, value: Any) -> bool:
    """Returns True if the value is in the list, False otherwise."""
    if is_empty(lst):
        return False

    pointer = lst.head
    while pointer.value != value:
        if pointer.next.value is None:
            return False
        pointer = pointer.next

    return True


def index(lst: OrderedList, value: Any) -> int:
    """Returns the index of the first occurrence of value in the list.

    Raises ValueError if the value is not present.
    """
    if contains(lst, value) is False:
        raise ValueError
    pointer = lst.head.next
    index = 0
    while pointer.value != value:
        pointer = pointer.next
        index += 1

    return index


def get(lst: OrderedList, index: int) -> Any:
    """Returns the value at index in the list.

    Raises IndexError if the index is out of range.
    """
    if index >= lst.size or index < 0:
        raise IndexError
    pointer = lst.head.next
    while index > 0:
        pointer = pointer.next
        index -= 1

    return pointer.value


def pop(lst: OrderedList, index: int) -> Any:
    """Removes and returns the value at index in the list.

    Raises IndexError if the index is out of range.
    """
    if index >= lst.size or index < 0:
        raise IndexError
    while index > 0:
        lst.head = lst.head.next
        index -= 1

    value = lst.head.next.value
    lst.head.next.next.prev = lst.head
    lst.head.next = lst.head.next.next
    lst.size -= 1

    while lst.head.value is not None:
        lst.head = lst.head.next

    return value


def is_empty(lst: OrderedList) -> bool:
    """Returns True if the list is empty, False otherwise."""
    return size(lst) == 0


def size(lst: OrderedList) -> int:
    """Returns the number if items in the list."""
    return lst.size
