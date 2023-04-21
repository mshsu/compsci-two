import unittest

from two_colorable import is_two_colorable


class Tests(unittest.TestCase):
    def test_01(self) -> None:
        edges = [
            ['v1', 'v2'],
            ['v2', 'v3'],
            ['v3', 'v4'],
            ['v4', 'v1']
        ]

        self.assertTrue(is_two_colorable(edges))

    def test_02(self) -> None:
        edges = [
            ['v1', 'v2'],
            ['v2', 'v3'],
            ['v3', 'v1'],
        ]

        self.assertFalse(is_two_colorable(edges))

    def test_03(self) -> None:
        edges = [
            ['v1', 'v2'],
            ['v2', 'v3'],
            ['v3', 'v4'],
            ['v4', 'v1'],
            ['v1', 'v3'],
            ['v2', 'v4']
        ]

        self.assertFalse(is_two_colorable(edges))

    def test_04(self) -> None:
        edges = [
            ['v1', 'v2'],
            ['v1', 'v3'],
            ['v2', 'v3']
        ]

        self.assertFalse(is_two_colorable(edges))

    def test_05(self) -> None:
        edges = [
            ['v1', 'v2'],
            ['v2', 'v3'],
            ['v3', 'v4'],
            ['v4', 'v1'],
            ['v5', 'v6']
        ]

        self.assertTrue(is_two_colorable(edges))

    def test_06(self) -> None:
        edges = [
            ['v1', 'v2'],
            ['v2', 'v3'],
            ['v3', 'v4'],
            ['v4', 'v1'],
            ['v5', 'v6'],
            ['v6', 'v7'],
            ['v7', 'v5']
        ]

        self.assertFalse(is_two_colorable(edges))


if __name__ == '__main__':
    unittest.main()
