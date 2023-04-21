import unittest

from perm_lex import perm_gen_lex


class Tests(unittest.TestCase):
    def test_perm_gen_lex_empty(self) -> None:
        self.assertEqual(perm_gen_lex(''), [''])

    # TODO: add more tests
    def test_perm_gen_lex_atomic(self) -> None:
        self.assertEqual(perm_gen_lex('a'), ['a'])

    def test_perm_gen_lex1(self) -> None:
        perms = ['ab', 'ba']
        self.assertEqual(perm_gen_lex('ab'), perms)

    def test_perm_gen_lex2(self) -> None:
        perms = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        self.assertEqual(perm_gen_lex('abc'), perms)

    def test_perm_gen_lex3(self) -> None:
        perms = ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd',
                 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb',
                 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac',
                 'dbca', 'dcab', 'dcba']
        self.assertEqual(perm_gen_lex('abcd'), perms)


if __name__ == '__main__':
    unittest.main()
