# NOTE: You'll probably need to import some things from array_stack.
from array_stack import empty_stack, push, pop, peek, is_empty, size


def postfix_eval(input_string: str) -> float:
    """Evaluates the given RPN expression.

    Args:
        input_string: an RPN expression

    Returns:
        The result of the expression evaluation

    Raises:
        ValueError: if the input is not well-formed
        ZeroDivisionError: if the input would cause division by zero
    """
    tokens = input_string.split()
    if tokens == []:
        raise ValueError('empty input')

    stack = empty_stack()
    operators = ['+', '-', '*', '/', '//', '^']
    for token in tokens:
        try:
            float(token)
            push(stack, token)
        except Exception:
            if token not in operators:
                raise ValueError('invalid token')

        if token in operators:
            if is_empty(stack) is True:
                raise ValueError('insufficient operands')

            o2 = pop(stack)

            if is_empty(stack) is True:
                raise ValueError('insufficient operands')

            o1 = pop(stack)

            if token == '+':
                push(stack, str(float(o1) + float(o2)))
            elif token == '-':
                push(stack, str(float(o1) - float(o2)))
            elif token == '*':
                push(stack, str(float(o1) * float(o2)))
            elif token == '/':
                if float(o2) == 0:
                    raise ZeroDivisionError
                push(stack, str(float(o1) / float(o2)))
            elif token == '//':
                if float(o2) == 0:
                    raise ZeroDivisionError
                push(stack, str(float(o1) // float(o2)))
            elif token == '^':
                push(stack, str(float(o1) ** float(o2)))

    answer = float(pop(stack))
    if is_empty(stack) is False:
        raise ValueError('too many operands')

    return answer


def infix_to_postfix(input_string: str) -> str:
    """Converts the given infix string to RPN.

    Args:
        input_string: an infix expression

    Returns:
        The equivalent expression in RPN
    """
    tokens = input_string.split()
    rpn = []
    stack = empty_stack()
    operators = ['+', '-', '*', '/', '//', '^']

    for token in tokens:
        if token not in operators and token != '(' and token != ')':
            rpn.append(token)

        elif token == '(':
            push(stack, token)

        elif token == ')':
            while peek(stack) != '(':
                rpn.append(pop(stack))
            pop(stack)

        elif token in operators:
            if token == '+' or token == '-':
                while is_empty(stack) is False and peek(stack) in operators:
                    rpn.append(pop(stack))

            elif token == '*' or token == '/' or token == '//':
                while (is_empty(stack) is False and
                       peek(stack) in ['*', '/', '//', '^']):
                    rpn.append(pop(stack))

            push(stack, token)

    for i in range(size(stack)):
        rpn.append(pop(stack))

    return ' '.join(rpn)
