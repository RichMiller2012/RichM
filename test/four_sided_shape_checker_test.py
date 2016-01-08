
from source.shape_checker import get_four_sided_shape_type
from unittest import TestCase

DISCONNECTED = 'disconnected'
RHOMBUS = 'rhombus'
SQUARE = 'square'
RECTANGLE = 'rectangle'
SQUARE = 'square'
INVALID = 'invalid'

class GetFourSidedShapeTypeTest(TestCase):


    """ Tuple and Tuple with integer values test cases """


    """ 1 """
    def test_get_four_sided_shape_type_square_tuple_int(self):
        sides = (1, 1, 1, 1)
        angles = (90, 90, 90, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, SQUARE)

    """ 2 """
    def test_get_four_sided_shape_type_rectangle_int(self):
        sides = (1, 1, 2, 2)
        angles = (90, 90, 90, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, RECTANGLE)

    """ 3 """
    def test_get_four_sided_shape_type_rhombus_int(self):
        sides = (1, 1, 1, 1)
        angles = (50, 50, 130, 130)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, RHOMBUS)

    """ 4 """
    def test_get_four_side_shape_type_disconnected_int(self):
        sides = (1, 1, 1, 1)
        angles = (70, 80, 90, 100)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, DISCONNECTED)

    """ 5 """
    def test_get_four_sided_shape_type_invalid_square_int(self):
        sides = (1, 1, 1, 3)
        angles = (90, 90, 90, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, INVALID)

    """ 6 """
    def test_get_four_sided_shape_type_invalid_rhombus_sides_int(self):
        sides = (1, 1, 2, 3)
        angles = (50, 50, 130, 130)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, INVALID)

    """ 7 """
    def test_get_four_sided_shape_type_invalid_rhombus_angles_int(self):
        sides = (1, 1, 2, 2)
        angles = (100, 90, 80, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, INVALID)

    """ Tuple and Tuple with float values test cases """


    """ 8 """
    def test_get_four_sided_shape_type_square_tuple_float(self):
        sides = (1.123, 1.123, 1.123, 1.123)
        angles = (90, 90, 90, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, SQUARE)

    """ 9 """
    def test_get_four_sided_shape_type_rectangle_float(self):
        sides = (1.123, 1.123, 2.234, 2.234)
        angles = (90, 90, 90, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, RECTANGLE)

    """ 10 """
    def test_get_four_sided_shape_type_rhombus_float(self):
        sides = (1.123, 1.123, 1.123, 1.123)
        angles = (50, 50, 130, 130)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, RHOMBUS)

    """ 11 """
    def test_get_four_side_shape_type_disconnected_float(self):
        sides = (1.123, 1.123, 1.123, 1.123)
        angles = (70, 80, 90, 100)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, DISCONNECTED)

    """ 12 """
    def test_get_four_sided_shape_type_invalid_square_float(self):
        sides = (1.123, 1.123, 1.123, 3.345)
        angles = (90, 90, 90, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, INVALID)

    """ 13 """
    def test_get_four_sided_shape_type_invalid_rhombus_sides_float(self):
        sides = (1.123, 1.123, 2.234, 3.345)
        angles = (50, 50, 130, 130)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, INVALID)

    """ 14 """
    def test_get_four_sided_shape_type_invalid_rhombus_angles_float(self):
        sides = (1.123, 1.123, 2234, 2.234)
        angles = (100, 90, 80, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, INVALID)


    """ List and List with integer values """


    """ 15 """
    def test_get_four_sided_shape_type_square_list_int(self):
        sides = [1, 1, 1, 1]
        angles = (90, 90, 90, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, SQUARE)

    """ 16 """
    def test_get_four_sided_shape_type_rectangle_list_int(self):
        sides = [1, 1, 2, 2]
        angles = (90, 90, 90, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, RECTANGLE)

    """ 17 """
    def test_get_four_sided_shape_type_rhombus_list_int(self):
        sides = [1, 1, 1, 1]
        angles = (50, 50, 130, 130)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, RHOMBUS)

    """ 18 """
    def test_get_four_side_shape_type_disconnected_list_int(self):
        sides = [1, 1, 1, 1]
        angles = (70, 80, 90, 100)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, DISCONNECTED)

    """ 19 """
    def test_get_four_sided_shape_type_invalid_square_list_int(self):
        sides = [1, 1, 1, 3]
        angles = (90, 90, 90, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, INVALID)

    """ 20 """
    def test_get_four_sided_shape_type_invalid_rhombus_sides_list_int(self):
        sides = [1, 1, 2, 3]
        angles = (50, 50, 130, 130)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, INVALID)

    """ 21 """
    def test_get_four_sided_shape_type_invalid_rhombus_angles_list_int(self):
        sides = [1, 1, 2, 2]
        angles = (100, 90, 80, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, INVALID)


    """ List and List with float values test cases """


    """ 22 """
    def test_get_four_sided_shape_type_square_list_float(self):
        sides = [1.123, 1.123, 1.123, 1.123]
        angles = (90, 90, 90, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, SQUARE)

    """ 23 """
    def test_get_four_sided_shape_type_rectangle_list_float(self):
        sides = [1.123, 1.123, 2.234, 2.234]
        angles = (90, 90, 90, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, RECTANGLE)

    """ 24 """
    def test_get_four_sided_shape_type_rhombus_list_float(self):
        sides = [1.123, 1.123, 1.123, 1.123]
        angles = (50, 50, 130, 130)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, RHOMBUS)

    """ 25 """
    def test_get_four_side_shape_type_disconnected_list_float(self):
        sides = [1.123, 1.123, 1.123, 1.123]
        angles = (70, 80, 90, 100)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, DISCONNECTED)

    """ 26 """
    def test_get_four_sided_shape_type_invalid_square_list_float(self):
        sides = [1.123, 1.123, 1.123, 3.345]
        angles = (90, 90, 90, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, INVALID)

    """ 27 """
    def test_get_four_sided_shape_type_invalid_rhombus_sides_list_float(self):
        sides = [1.123, 1.123, 2.234, 3.345]
        angles = (50, 50, 130, 130)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, INVALID)

    """ 28 """
    def test_get_four_sided_shape_type_invalid_rhombus_angles_list_float(self):
        sides = [1.123, 1.123, 2234, 2.234]
        angles = (100, 90, 80, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, INVALID)


    """ Dictionary and Dictionary with integer values """


    """ 29 """
    def test_get_four_sided_shape_type_square_list_int(self):
        sides = {'a':1, 'b':1, 'c':1, 'd':1}
        angles = (90, 90, 90, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, SQUARE)

    """ 30 """
    def test_get_four_sided_shape_type_rectangle_list_int(self):
        sides = {'a':1, 'b':1, 'c':2, 'd':2}
        angles = (90, 90, 90, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, RECTANGLE)

    """ 31 """
    def test_get_four_sided_shape_type_rhombus_list_int(self):
        sides = {'a':1, 'b':1, 'c':1, 'd':1}
        angles = (50, 50, 130, 130)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, RHOMBUS)

    """ 32 """
    def test_get_four_side_shape_type_disconnected_list_int(self):
        sides = {'a':1, 'b':1, 'c':1, 'd':1}
        angles = (70, 80, 90, 100)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, DISCONNECTED)

    """ 33 """
    def test_get_four_sided_shape_type_invalid_square_list_int(self):
        sides = {'a':1, 'b':1, 'c':1, 'd':3}
        angles = (90, 90, 90, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, INVALID)

    """ 34 """
    def test_get_four_sided_shape_type_invalid_rhombus_sides_list_int(self):
        sides = {'a':1, 'b':1, 'c':2, 'd':3}
        angles = (50, 50, 130, 130)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, INVALID)

    """ 35 """
    def test_get_four_sided_shape_type_invalid_rhombus_angles_list_int(self):
        sides = {'a':1, 'b':1, 'c':2, 'd':2}
        angles = (100, 90, 80, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, INVALID)


    """ Dictionary and Dictionary with float values test cases """


    """ 36 """
    def test_get_four_sided_shape_type_square_list_float(self):
        sides = {'a':1.123, 'b':1.123, 'c':1.123, 'd':1.123}
        angles = (90, 90, 90, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, SQUARE)

    """ 37 """
    def test_get_four_sided_shape_type_rectangle_list_float(self):
        sides = {'a':1.123, 'b':1.123, 'c':2.234, 'd':2.234}
        angles = (90, 90, 90, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, RECTANGLE)

    """ 38 """
    def test_get_four_sided_shape_type_rhombus_list_float(self):
       sides = {'a':1.123, 'b':1.123, 'c':1.123, 'd':1.123}
       angles = (50, 50, 130, 130)
       result = get_four_sided_shape_type(sides, angles)
       self.assertEquals(result, RHOMBUS)

    """ 39 """
    def test_get_four_side_shape_type_disconnected_list_float(self):
        sides = {'a':1.123, 'b':1.123, 'c':1.123, 'd':1.123}
        angles = (70, 80, 90, 100)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, DISCONNECTED)

    """ 40 """
    def test_get_four_sided_shape_type_invalid_square_list_float(self):
        sides = {'a':1.123, 'b':1.123, 'c':1.123, 'd':3.345}
        angles = (90, 90, 90, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, INVALID)

    """ 41 """
    def test_get_four_sided_shape_type_invalid_rhombus_sides_list_float(self):
        sides = {'a':1.123, 'b':1.123, 'c':2.234, 'd':3.345}
        angles = (50, 50, 130, 130)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, INVALID)

    """ 42 """
    def test_get_four_sided_shape_type_invalid_rhombus_angles_list_float(self):
        sides = {'a':1.123, 'b':1.123, 'c':2.234, 'd':2.234}
        angles = (100, 90, 80, 90)
        result = get_four_sided_shape_type(sides, angles)
        self.assertEquals(result, INVALID)