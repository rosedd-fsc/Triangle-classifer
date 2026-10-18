import math
from triangle import classify_triangle, is_valid_triangle

def test_equilateral():
    # sides 5, 5, 5: all sides are equal, this must be 
    # Equilateral triangle
     assert classify_triangle(5, 5, 5) == "Equilateral"

def test_isosceles():
 # sides 5, 5, 8: exactly two sides are equal,
 # this must be Isoceles triangle
    assert classify_triangle(5, 5, 8) == "Isosceles"

def test_scalene():
    # sides 4, 5, 6: all sides are different,
    # this must be Scalene triangle
     assert classify_triangle(4, 5, 6) == "Scalene"

def test_invalid_zero_side():
    # sides 0, 5, 5: one side is less than or equal to  zero, 
    # so the triangle is invalid
     assert classify_triangle(0, 5, 5) == "Invalid" 

def test_degenerate_boundary():
    # sides 4, 5, 9: 4 + 5 = 9,
    # so the triangle is invalid
    assert classify_triangle(4, 5, 9) == "Invalid"

def test_right_triangle_non_integer():
    # sides 5, 5, 5*sqrt(2): 5^2 + 5^2 = (5*sqrt(2))^2,
    # so the triangle is a right triangle
    c = 5 * math.sqrt(2)
    # Double check if these sides form a right triangle using the Pythagorean theorem
    assert math.isclose(5**2 + 5**2, c**2)
    # Finally check the classifer output
    assert classify_triangle(5, 5, c) == "Right Isosceles"