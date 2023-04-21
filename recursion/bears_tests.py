import unittest

from bears import bears


class Tests(unittest.TestCase):
    def test_bears_40(self):
        self.assertFalse(bears(40))

    def test_bears_42(self):
        self.assertTrue(bears(42))

    # TODO: add more tests
    def test_bears_250(self):
        self.assertTrue(bears(250))

    def test_bears_53(self):
        self.assertFalse(bears(53))

    def test_bears_0(self):
        self.assertFalse(bears(0))


if __name__ == '__main__':
    unittest.main()
