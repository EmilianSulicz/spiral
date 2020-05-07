import unittest
from spiral import spiral


class TestSpiral(unittest.TestCase):
    input_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    input_2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    input_3 = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]]

    input_4 = [[1, 2, 3, 4, 5, 6],
               [7, 8, 9, 10, 11, 12],
               [13, 14, 15, 16, 17, 18]]

    input_5 = [[1],
               [2],
               [3],
               [4]]

    input_6 = [[1, 2, 3, 4, 5, 6, 7, 8]]

    output_1 = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    output_2 = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    output_3 = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    output_4 = [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11]
    output_5 = [1, 2, 3, 4]
    output_6 = [1, 2, 3, 4, 5, 6, 7, 8]

    def test_spiral_on_example_tables(self):
        self.assertEqual(spiral(self.input_1), self.output_1, 'Given example 1 failed')
        self.assertEqual(spiral(self.input_2), self.output_2, 'Given example 2 failed')

    def test_spiral_on_bigger_tables(self):
        self.assertEqual(spiral(self.input_3), self.output_3, 'Big table 1 failed')
        self.assertEqual(spiral(self.input_4), self.output_4, 'Big table 2 failed')

    def test_spiral_on_small_tables(self):
        self.assertEqual(spiral(self.input_5), self.output_5, 'Small table 1 failed')
        self.assertEqual(spiral(self.input_6), self.output_6, 'Small table 2 failed')


if __name__ == '__main__':
    unittest.main()
