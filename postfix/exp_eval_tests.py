import unittest

from exp_eval import postfix_eval, infix_to_postfix
from array_stack import empty_stack, pop, peek


class Tests(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval('1 2 +'), 3)

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix('1 + 2'), '1 2 +')

    # TODO: add more tests!
    def test_pop_err(self):
        my_stack = empty_stack()
        with self.assertRaises(IndexError):
            pop(my_stack)

    def test_peek_err(self):
        my_stack = empty_stack()
        with self.assertRaises(IndexError):
            peek(my_stack)

    def test_postfix_eval_02(self):
        self.assertAlmostEqual(postfix_eval('5 1 2 + 4 ^ + 3 -'), 83)

    def test_postfix_eval_03(self):
        self.assertAlmostEqual(postfix_eval('2 1 -'), 1)

    def test_postfix_eval_04(self):
        self.assertAlmostEqual(postfix_eval('2 3 *'), 6)

    def test_postfix_eval_05(self):
        self.assertAlmostEqual(postfix_eval('6 3 /'), 2)

    def test_postfix_eval_06(self):
        self.assertAlmostEqual(postfix_eval('4 3 //'), 1)

    def test_postfix_eval_07(self):
        self.assertAlmostEqual(postfix_eval('2 2 ^'), 4)

    def test_postfix_eval_08(self):
        self.assertAlmostEqual(postfix_eval('6 4 3 + 2 - * 6 /'), 5)

    def test_postfix_eval_err_01(self):
        with self.assertRaises(ValueError):
            postfix_eval('')

    def test_postfix_eval_err_02(self):
        with self.assertRaises(ValueError):
            postfix_eval('2 a +')

    def test_postfix_eval_err_03(self):
        with self.assertRaises(ValueError):
            postfix_eval('2 +')

    def test_postfix_eval_err_04(self):
        with self.assertRaises(ValueError):
            postfix_eval('2 3 4 +')

    def test_postfix_eval_err_05(self):
        with self.assertRaises(ValueError):
            postfix_eval('+')

    def test_postfix_eval_err_06(self):
        with self.assertRaises(ZeroDivisionError):
            postfix_eval('2 0 /')

    def test_postfix_eval_err_07(self):
        with self.assertRaises(ZeroDivisionError):
            postfix_eval('2 0 //')

    def test_infix_to_postfix_02(self):
        infix = '3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3'
        postfix = '3 4 2 * 1 5 - 2 3 ^ ^ / +'
        self.assertEqual(infix_to_postfix(infix), postfix)

    def test_infix_to_postfix_03(self):
        infix = '1 + 2 + 3 + 4 + 5'
        postfix = '1 2 + 3 + 4 + 5 +'
        self.assertEqual(infix_to_postfix(infix), postfix)

    def test_infix_to_postfix_04(self):
        infix = '1 / ( 2 / ( 3 / 4 * 5 * ( 6 + 7 - 8 ) ) )'
        postfix = '1 2 3 4 / 5 * 6 7 + 8 - * / /'
        self.assertEqual(infix_to_postfix(infix), postfix)


if __name__ == '__main__':
    unittest.main()
