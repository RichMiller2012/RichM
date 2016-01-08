﻿"""
Test for source.shape_checker
"""
from source.shape_checker import get_triangle_type
from unittest import TestCase

EQUILATERAL = 'equilateral'
ISOSCELES = 'isosceles'
SCALENE = 'scalene'
INVALID = 'invalid' 
class TestGetTriangleType(TestCase):
        
    """ integer test cases """


    """ 1 """
    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, EQUILATERAL)
    """ 2 """
    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, SCALENE)
    """ 3 """
    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(1, 1, 2)
        self.assertEqual(result, ISOSCELES)
    """ 4 """
    def test_get_triangle_equilateral_all_float(self):
        result = get_triangle_type(1.123, 1.123, 1.123)
        self.assertEqual(result, EQUILATERAL)
    """ 5 """
    def test_get_triangle_isosceles_all_float(self):
        result = get_triangle_type(1.123, 1.123, 2.345)
        self.assertEqual(result, ISOSCELES)
    """ 6 """
    def test_get_triangle_scalene_all_float(self):
        result = get_triangle_type(1.123, 2.234, 3.456)
        self.assertEqual(result, SCALENE)
    """ 7 """
    def test_get_triangle_invalid_zero(self):
        result = get_triangle_type(0, 0, 0)
        self.assertEqual(result, INVALID)
    """ 8 """
    def test_get_triangle_invalid_negative_int(self):
        result = get_triangle_type(-1, -1, -1)
        self.assertEqual(result, INVALID)
    """ 9 """
    def test_get_triangle_invalid_negative_float(self):
        result = get_triangle_type(-1.124, -1.123, -1.123)
        self.assertEqual(result, INVALID)
    

    """ tuple test cases """


    """ 10 """
    def test_get_triangle_equilateral_valid_tuple(self):
        input = (1, 1, 1)
        result = get_triangle_type(input)
        self.assertEqual(result, EQUILATERAL)
    """ 11 """
    def test_get_triangle_isosceles_valid_tuple(self):
        input = (1, 1, 2)
        result = get_triangle_type(input)
        self.assertEqual(result, ISOSCELES)
    """ 12 """
    def test_get_triangle_scalene_valid_tuple(self):
        input = (1, 2, 3)
        result = get_triangle_type(input)
        self.assertEquals(result, SCALENE)
    """ 13 """
    def test_get_triangle_equilateral_valid_tuple_float(self):
        input = (1.123, 1.123, 1.123)
        result = get_triangle_type(input)
        self.assertEquals(result, EQUILATERAL)
    """ 14 """
    def test_get_triangle_isosceles_valid_tuple_float(self):
        input = (1.123, 1.123, 2.234)
        result = get_triangle_type(input)
        self.assertEqual(result, ISOSCELES)
    """ 15 """
    def test_get_triangle_type_scalene_valid_tuple(self):
        input = (1.123, 2.234, 3.345)
        result = get_triangle_type(input)
        self.assertEquals(result, SCALENE)
    """ 16 """
    def test_get_triangle_type_invalid_zero_tuple(self):
        input = (0, 0, 0)
        result = get_triangle_type(input)
        self.assertEqual(result, INVALID)
    """ 17 """
    def test_get_triangle_type_invalid_negative_tuple(self):
        input = (-1, -1, -1)
        result = get_triangle_type(input)
        self.assertEqual(result, INVALID)


    """ list test cases """


    """ 18 """
    def test_get_triangle_equilateral_valid_int_list(self):
        input = [1, 1, 1]
        result = get_triangle_type(input)
        self.assertEqual(result, EQUILATERAL)
    """ 19 """
    def test_get_triangle_isosceles_valid_int_list(self):
        input = [1, 1, 2]
        result = get_triangle_type(input)
        self.assertEqual(result, ISOSCELES)
    """ 20 """
    def test_get_triangle_scalene_valid_int_list(self):
        input = [1, 2, 3]
        result = get_triangle_type(input)
        self.assertEquals(result, SCALENE)
    """ 21 """
    def test_get_triangle_equilateral_valid_list_float(self):
        input = [1.123, 1.123, 1.123]
        result = get_triangle_type(input)
        self.assertEquals(result, EQUILATERAL)
    """ 22 """
    def test_get_triangle_isosceles_valid_list_float(self):
        input = [1.123, 1.123, 2.234]
        result = get_triangle_type(input)
        self.assertEqual(result, ISOSCELES)
    """ 23 """
    def test_get_triangle_type_scalene_valid_list_float(self):
        input = [1.123, 2.234, 3.345]
        result = get_triangle_type(input)
        self.assertEquals(result, SCALENE)
    """ 24 """
    def test_get_triangle_type_invalid_zero_list(self):
        input = [0, 0, 0]
        result = get_triangle_type(input)
        self.assertEqual(result, INVALID)
    """ 25 """
    def test_get_triangle_type_invalid_negative_list(self):
        input = [-1, -1, -1]
        result = get_triangle_type(input)
        self.assertEqual(result, INVALID)
   
    """ Dictionary test cases """


    """ 26 """
    def test_get_triangle_equilateral_valid_int_dictionary(self):
        input = {'a':1, 'b':1, 'c':1}
        result = get_triangle_type(input)
        self.assertEqual(result, EQUILATERAL)
    """ 27 """
    def test_get_triangle_isosceles_valid_int_dictionary(self):
        input = {'a':1, 'b':1, 'c':3}
        result = get_triangle_type(input)
        self.assertEqual(result, ISOSCELES)
    """ 28 """
    def test_get_triangle_scalene_valid_int_dictionary(self):
        input = {'a':1, 'b':2, 'c':3}
        result = get_triangle_type(input)
        self.assertEquals(result, SCALENE)
    """ 29 """
    def test_get_triangle_equilateral_valid_dictionary_float(self):
        input = {'a':1.123, 'b':1.123, 'c':1.123}
        result = get_triangle_type(input)
        self.assertEquals(result, EQUILATERAL)
    """ 30 """
    def test_get_triangle_isosceles_valid_dictionary_float(self):
        input = {'a':1.123, 'b':1.123, 'c':3}
        result = get_triangle_type(input)
        self.assertEqual(result, ISOSCELES)
    """ 31 """
    def test_get_triangle_type_scalene_valid_dictionary_float(self):
        input = {'a':1.123, 'b':2.234, 'c':3.345}
        result = get_triangle_type(input)
        self.assertEquals(result, SCALENE)
    """ 32 """
    def test_get_triangle_type_invalid_zero_dictionary(self):
        input = {'a':0, 'b':0, 'c':0}
        result = get_triangle_type(input)
        self.assertEqual(result, INVALID)
    """ 33 """
    def test_get_triangle_type_invalid_negative_dictionary(self):
        input = {'a':-1, 'b':-2, 'c':-3}
        result = get_triangle_type(input)
        self.assertEqual(result, INVALID)


    """ Robust test cases """


    """ 34 """
    def test_get_triangle_type_string_values(self):
        result = get_triangle_type('one', 'two', 'three')
        self.assertEqual(result, INVALID)
    """ 35 """
    def test_get_triangle_type_string_tuple_values(self):
        input = ('one', 'two', 'three')
        result = get_triangle_type(input)
        self.assertEqual(result, INVALID)
    """ 36 """
    def test_get_triangle_type_string_list_values(self):
        input = ['one', 'two', 'three']
        result = get_triangle_type(input)
        self.assertEqual(result, INVALID)
    """ 37 """
    def test_get_triangle_type_string_dictionary_values(self):
        input = {'a':'one', 'b':'two', 'c':'three'}
        result = get_triangle_type(input)
        self.assertEqual(result, INVALID)       

