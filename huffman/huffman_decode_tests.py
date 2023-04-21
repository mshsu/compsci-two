import io
import unittest

# NOTE: Similar to part a, do not import anything else from huffman.
from huffman import parse_header, huffman_decode


class TestList(unittest.TestCase):
    def test_parse_header_01(self):
        header = '97 2 98 4 99 8 100 16 102 2\n'

        frequencies = parse_header(header)
        expected = [0] * 256
        expected[97:103] = [2, 4, 8, 16, 0, 2]

        self.assertEqual(frequencies, expected)

    def test_parse_header_02(self):
        header = '\n'

        frequencies = parse_header(header)
        expected = [0] * 256

        self.assertEqual(frequencies, expected)

    def test_huffman_decode_01(self):
        in_file = io.StringIO(
            '32 3 97 4 98 3 99 2 100 1\n'
            '11011011000011011010011010011'
        )
        out_file = io.StringIO()

        huffman_decode(in_file, out_file)
        result = out_file.getvalue()

        in_file.close()
        out_file.close()

        self.assertEqual(result, 'abcd abc ab a')

    # NOTE: This is the same test as decode_01, but with real files
    def test_huffman_decode_02(self):
        with open('text_files/file1_encoded.txt') as in_file, \
             open('text_files/file1_decoded.txt', 'w') as out_file:
            huffman_decode(in_file, out_file)

        with open("text_files/file1_decoded.txt") as student_out, \
             open("text_files/file1.txt") as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    def test_huffman_decode_03(self):
        in_file = io.StringIO('\n')
        out_file = io.StringIO()

        huffman_decode(in_file, out_file)
        result = out_file.getvalue()

        in_file.close()
        out_file.close()

        self.assertEqual(result, '')

    def test_huffman_decode_04(self):
        in_file = io.StringIO('97 5\n')
        out_file = io.StringIO()

        huffman_decode(in_file, out_file)
        result = out_file.getvalue()

        in_file.close()
        out_file.close()

        self.assertEqual(result, 'aaaaa')

    def test_huffman_decode_05(self):
        with open('text_files/file2_encoded.txt') as in_file, \
             open('text_files/file2_decoded.txt', 'w') as out_file:
            huffman_decode(in_file, out_file)

        with open("text_files/file2_decoded.txt") as student_out, \
             open("text_files/file2.txt") as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    def test_huffman_decode_06(self):
        with open('text_files/multiline_encoded.txt') as in_file, \
             open('text_files/multiline_decoded.txt', 'w') as out_file:
            huffman_decode(in_file, out_file)

        with open("text_files/multiline_decoded.txt") as student_out, \
             open("text_files/multiline.txt") as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    def test_huffman_decode_07(self):
        with open('text_files/declaration_encoded.txt') as in_file, \
             open('text_files/declaration_decoded.txt', 'w') as out_file:
            huffman_decode(in_file, out_file)

        with open("text_files/declaration_decoded.txt") as student_out, \
             open("text_files/declaration.txt") as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())


if __name__ == '__main__':
    unittest.main()
