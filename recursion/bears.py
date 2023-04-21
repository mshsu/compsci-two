def bears(n: int) -> bool:
    """Returns whether it is possible to win the bear game starting with
    n bears.

    Implemented recursively
    """
    if n == 42:
        return True

    elif n < 42 or (0 not in [n % 2, n % 3, n % 4, n % 5]):
        return False

    else:
        possibilibears = []
        if n % 2 == 0:
            possibilibears.append(n // 2)
        if n % 3 == 0 or n % 4 == 0:
            digits = list(str(n))
            digits = [int(digit) for digit in digits]
            subtract = digits[-1] * digits[-2]
            if subtract != 0:
                possibilibears.append(n - subtract)
        if n % 5 == 0:
            possibilibears.append(n - 42)

        for i in range(len(possibilibears)):
            if bears(possibilibears[i]) is True:
                return True

        return False
