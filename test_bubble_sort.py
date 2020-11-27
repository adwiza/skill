import unittest

from any_sort import bubble_sort


class BubleSortTest(unittest.TestCase):
    # нужно отнаследоваться от этого класса, чтобы заработала ммагия тестирования
    def test_normal(self):
        # Запускаем тестируфемую функцию
        result = bubble_sort([3, 4, 2, 8, 1, 6, 4])
        self.assertEqual(result, [1, 2, 3, 4, 4, 6, 8])

    def test_sorted(self):
        result = bubble_sort([3, 4, 5])
        self.assertEqual(result, [3, 4, 5], 'не работает сортировка отсортированного списка')

    def test_reversed(self):
        result = bubble_sort([3, 2, 1])
        self.assertEqual(result, [1, 2, 3])

    def test_empty(self):
        result = bubble_sort([])
        self.assertEqual(result, [])

    def test_with_negative(self):
        result = bubble_sort([9, 3, -7, 2])
        self.assertEqual(result, [-7, 2, 3, 9])