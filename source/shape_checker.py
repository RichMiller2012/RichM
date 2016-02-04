"""
:mod:`source.source1` -- Example source code
============================================

The following example code determines if a set of 3 sides of a triangle is equilateral, scalene or iscoceles
"""

def get_triangle_type(a=0, b=0, c=0):
    print "entering get_triangle type"
    """
    Determine if the given triangle is equilateral, scalene or Isosceles

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :return: "equilateral", "isosceles", "scalene" or "invalid"
    :rtype: str
    """
    if isinstance(a, (tuple, list)) and len(a) == 3:
        c = a[2]
        b = a[1]
        a = a[0]

    if isinstance(a, dict) and len(a.keys()) == 3:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"

    if a == b and b == c:
        return "equilateral"

    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"

def get_rectangle_type(sides):
    
    print "entering get_rectangle_type"

    if isinstance(sides, (tuple, list)) and len(sides) == 4:
        d = sides[3]
        c = sides[2]
        b = sides[1]
        a = sides[0]

    elif isinstance(sides, dict) and len(sides.keys()) == 4:
        values = []
        for value in sides.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]
        d = values[3]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and isinstance(d, (int, float))):
        return 'invalid'
    
    if a == b and b == c and c == d:
        return 'square'

    elif (a == b and c == d) or (a == c and b == d) or (a == d and b == c):
        return 'rectangle'

    else:
        return 'invalid'

def get_four_sided_shape_type(sides, angles):

    if isinstance(sides, (tuple, list)) and len(sides) == 4:
        side4 = sides[3]
        side3 = sides[2]
        side2 = sides[1]
        side1 = sides[0]

    elif isinstance(sides, dict) and len(sides.keys()) == 4:
        values = []
        for value in sides.values():
            values.append(value)
        side4 = values[3]
        side3 = values[2]
        side2 = values[1]
        side1 = values[0]

    if isinstance(angles, (tuple, list)) and len(angles) == 4:
        angle4 = angles[3]
        angle3 = angles[2]
        angle2 = angles[1]
        angle1 = angles[0]

    elif isinstance(angles, dict) and len(angles.keys()) == 4:
        values = []
        for value in angles.values():
            values.append(value)
        angle4 = values[3]
        angle3 = values[2]
        angle2 = values[1]
        angle1 = values[0]

    if angle1 + angle2 + angle3 + angle4 != 360:
        return 'disconnected'

    elif angle1 == angle2 == angle3 == angle4 == 90:
        if side1 == side2 and side2 == side3 and side3 == side4:
            return 'square'

        elif (side1 == side2 and side3 == side4) or (side1 == side3 and side2 == side4) or (side1 == side4 and side2 == side3):
            return 'rectangle'

        else:
            return 'invalid'

    elif (angle1 == angle2 and angle3 == angle4) or (angle1 == angle3 and angle2 == angle4) or (angle1 == angle4 and agle2 == angle3):
        if((side1 == side2 and side3 == side4) or (side1 == side3 and side2 == side4) or (side1 == side4 and side2 == side3)):
            return 'rhombus'
        else:
            return 'invalid'

    else:
        return 'invalid'
