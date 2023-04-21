def convert(num: int, base: int) -> str:
    """Returns a string representing num in the given base.

    Implemented recursively.
    """
    hex_val = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'A', 'B', 'C', 'D', 'E', 'F']

    if num // base == 0:
        remainder = hex_val[num % base]
        return remainder

    quotient = num // base
    remainders = convert(quotient, base)
    remainders = list(remainders)

    new_r = hex_val[num % base]
    remainders.append(new_r)

    return ''.join(remainders)
