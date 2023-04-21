from typing import Any


class ArrayStack:
    def __init__(self, capacity: int = 5):
        self.items: list[Any] = [None] * capacity
        self.capacity: int = capacity
        self.size: int = 0


def empty_stack() -> ArrayStack:
    """
    This function takes no arguments and returns an empty stack.
    """
    return ArrayStack()


def push(stack: ArrayStack, value: Any) -> None:
    """
    This function takes a stack and a value as arguments and places the value
    on the “top” of the stack.

    For this project, because we’re only using the array-based approach, we
    should be mutating the given stack and thus our function won’t return
    anything.
    """
    if size(stack) + 1 > stack.capacity:
        new_stack = ArrayStack(stack.capacity * 2)
        for i in range(size(stack)):
            new_stack.items[i] = stack.items[i]
            new_stack.size += 1
        stack.items = new_stack.items
        stack.capacity = new_stack.capacity

    stack.items[stack.size] = value
    stack.size += 1


def pop(stack: ArrayStack) -> Any:
    """
    This function takes a stack as an argument and removes (and returns) the
    element at the “top” of the stack. If the stack is empty, then this
    operation should raise an IndexError.

    For this project, because we’re mutating the stack directly, we only need
    return the value being popped.
    """
    if is_empty(stack):
        raise IndexError

    value = peek(stack)
    stack.items[stack.size - 1] = None
    stack.size -= 1
    return value


def peek(stack: ArrayStack) -> Any:
    """
    This function takes a stack as an argument and returns (without removing)
    the value on the “top” of the stack. If the stack is empty, then this
    operation should raise an IndexError.
    """
    if is_empty(stack):
        raise IndexError

    return stack.items[stack.size - 1]


def is_empty(stack: ArrayStack) -> bool:
    """
    This function takes a stack as an argument and returns whether or not the
    stack is empty.
    """
    return size(stack) == 0


def size(stack: ArrayStack) -> int:
    """
    This function takes a stack as an argument and returns the number of items
    in the stack.
    """
    return stack.size
