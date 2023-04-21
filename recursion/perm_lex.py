from __future__ import annotations


def perm_gen_lex(string: str) -> list[str]:
    """
    Generates all possible permutations of a given string in lexicographic
    order.

    Input: A string, string.
    Output: A list of all permutations of the characters s in lexicographic
        order.
    """
    # Base case
    if len(string) == 0:
        return ['']

    # Induction step
    perms = []
    # For for each character c in string s do:
    for i in range(len(string)):
        # Form a simpler string, t, by removing c from s
        simple_str = list(string)
        char = simple_str.pop(i)  # c
        simple_str = ''.join(simple_str)  # t

        # Generate all permutations of t recursive (ie. call perm_gen_lex(t))
        new_perms = perm_gen_lex(simple_str)

        # For each permutation p of t do:
        for perm in new_perms:
            # Add c to the front of p and add the result to the list of
            # permutations
            perms.append(char + perm)

    # Return the list of permutations
    return perms
