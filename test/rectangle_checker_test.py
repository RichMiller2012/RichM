﻿
from source.shape_checker import get_rectangle_type
from unittest import TestCase

SQUARE = 'square'
RECTANGLE = 'rectangle'
INVALID = 'invalid'

class TestGetRectangleType(TestCase):

    """ tuple tests """

    """ 1 """
    def test_get_rectangle_type_square_tuple_int(self):
        input = (1, 1, 1, 1)
        result = get_rectangle_type(input)
        self.assertEqual(result, SQUARE)

    """ 2 """
    def test_get_rectangle_type_rectangle_tuple_int(self):
        input = (1, 1, 2, 2)
        result = get_rectangle_type(input)
        self.assertEqual(result, RECTANGLE)

    """ 3 """
    def test_get_rectangle_type_square_tuple_float(self):
        input = (1.123, 1.123, 1.123, 1.123)
        result = get_rectangle_type(input)
        self.assertEqual(result, SQUARE)

    """ 4 """
    def test_get_rectangle_type_rectangle_tuple_float(self):
        input = (1.123, 1.123, 2.234, 2.234)
        result = get_rectangle_type(input)
        self.assertEquals(result, RECTANGLE)

    """ 5 """
    def test_get_rectangle_type_invalid_sides_tuple(self):
        input = (1, 2, 3, 4)
        result = get_rectangle_type(input)
        self.assertEqual(result, INVALID)

    """ 6 """
    def test_get_rectangle_type_two_invalid_sides_tuple(self):
        input = (1, 1, 2, 3)
        result = get_rectangle_type(input)
        self.assertEqual(result, INVALID)

    
    """ List Tests """


    """ 7 """
    def test_get_rectangle_type_square_list_int(self):
        input = [1, 1, 1, 1]
        result = get_rectangle_type(input)
        self.assertEqual(result, SQUARE)

    """ 8 """
    def test_get_rectangle_type_rectangle_list_int(self):
        input = [1, 1, 2, 2]
        result = get_rectangle_type(input)
        self.assertEqual(result, RECTANGLE)

    """ 9 """
    def test_get_rectangle_type_square_list_float(self):
        input = [1.123, 1.123, 1.123, 1.123]
        result = get_rectangle_type(input)
        self.assertEqual(result, SQUARE)

    """ 10 """
    def test_get_rectangle_type_rectangle_list_float(self):
        input = [1.123, 1.123, 2.234, 2.234]
        result = get_rectangle_type(input)
        self.assertEquals(result, RECTANGLE)

    """ 11 """
    def test_get_rectangle_type_invalid_sides_list(self):
        input = [1, 2, 3, 4]
        result = get_rectangle_type(input)
        self.assertEqual(result, INVALID)

    """ 12 """
    def test_get_rectangle_type_two_invalid_sides_list(self):
        input = [1, 1, 2, 3]
        result = get_rectangle_type(input)
        self.assertEqual(result, INVALID)


    """ Dictionary Test Cases """

    
    """ 13 """
    def test_get_rectangle_type_square_dictionary_int(self):
        input = {'a':1, 'b':1, 'c':1, 'd':1}
        result = get_rectangle_type(input)
        self.assertEqual(result, SQUARE)

    """ 14 """
    def test_get_rectangle_type_rectangle_dictionary_int(self):
        input = {'a':1, 'b':1, 'c':2, 'd':2}
        result = get_rectangle_type(input)
        self.assertEqual(result, RECTANGLE)

    """ 15 """
    def test_get_rectangle_type_square_dictionary_float(self):
        input = {'a':1.123, 'b':1.123, 'c':1.123, 'd':1.123}
        result = get_rectangle_type(input)
        self.assertEqual(result, SQUARE)

    """ 16 """
    def test_get_rectangle_type_rectangle_dictionary_float(self):
        input = {'a':1.123, 'b':1.123, 'c':2.234, 'd':2.234}
        result = get_rectangle_type(input)
        self.assertEquals(result, RECTANGLE)

    """ 17 """
    def test_get_rectangle_type_invalid_sides_dictionary(self):
        input = {'a':1, 'b':2, 'c':3, 'd':4}
        result = get_rectangle_type(input)
        self.assertEqual(result, INVALID)

    """ 18 """
    def test_get_rectangle_type_two_invalid_sides_dictionary(self):
        input = {'a':1, 'b':1, 'c':2, 'd':3}
        result = get_rectangle_type(input)
        self.assertEqual(result, INVALID)
    




        




