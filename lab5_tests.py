import data
import unittest
from data import Time
from data import Point
import lab5
from lab5 import is_descending, largest_between, furthest_from_origin


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 3
    def test_time_add(self):
        time1 = Time(1, 20, 30)
        time2 = Time(2, 15, 20)
        result = lab5.time_add(time1, time2)
        expected = Time(3, 35, 50)
        self.assertEqual(expected, result)

    def test_time_add2(self):
        time1 = Time(1, 59, 50)
        time2 = Time(0, 0, 15)
        result = lab5.time_add(time1, time2)
        expected = Time(2, 0, 5)
        self.assertEqual(expected, result)

    # Part 4
    def test_is_descending(self):
        list1 = [5.5, 3.3, 2.2, 1.1]
        result = is_descending(list1)
        expected = True
        self.assertEqual(expected, result)
    def test_is_descending2(self):
        list1 = [3.3, 5.5, 2.2, 1.1]
        result = is_descending(list1)
        expected = False
        self.assertEqual(expected, result)

    # Part 5
    def test_largest_between(self):
        result = largest_between([1,3,5,7,9], 1, 3)
        expected = 3
        self.assertEqual(expected, result)
    def test_largest_between2(self):
        result = largest_between([1,3,5,7,9], 3, 1)
        expected = None
        self.assertEqual(expected, result)
    def test_largest_between3(self):
        result = largest_between([1,3,5,7,9], 2, 2)
        expected = 2
        self.assertEqual(expected, result)

    # Part 6
    def test_furthest_from_origin(self):
        result = furthest_from_origin([Point(1,1),
                                       Point(3,4),
                                       Point(0,5)])
        expected = 2
        self.assertEqual(expected, result)
    def test_furthest_from_origin2(self):
        result = furthest_from_origin([Point(0,0),
                                       Point(1,1)])
        expected = 1
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
