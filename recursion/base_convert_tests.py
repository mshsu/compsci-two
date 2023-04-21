import unittest

from base_convert import convert


class Tests(unittest.TestCase):
    def test_conbert_base02_1(self):
        self.assertEqual(convert(0, 2), '0')

    def test_convert_base16_1(self):
        self.assertEqual(convert(107, 16), '6B')

    # TODO: add more tests
    def test_convert_base04_1(self):
        self.assertEqual(convert(30, 4), '132')

    def test_convert_base16_2(self):
        self.assertEqual(convert(108, 16), '6C')

    def test_convert_base16_3(self):
        self.assertEqual(convert(109, 16), '6D')

    def test_convert_base16_4(self):
        self.assertEqual(convert(110, 16), '6E')

    def test_convert_base16_5(self):
        self.assertEqual(convert(111, 16), '6F')

    def test_convert_base16_6(self):
        self.assertEqual(convert(106, 16), '6A')


if __name__ == '__main__':
    unittest.main()
