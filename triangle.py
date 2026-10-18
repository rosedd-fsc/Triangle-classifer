import math

def is_valid_triangle(a, b, c) -> bool:
    # Check if the triangle is valid using the triangle inequality theorem
    if a <= 0 or b <= 0 or c <= 0:
        return False
    shortest, middle, longest = sorted([a, b, c])
    return shortest + middle > longest

def classify_triangle(a, b, c) -> str:
    # Classify the triangle based on its sides
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    if a == b == c: 
        type = "Equilateral"

    elif a ==b or b == c or a ==c:
        type = "Isosceles"

    else:
        type = "Scalene"

    # Check for right triangle using the Pythagorean theorem
    shortest, middle, longest = sorted([a, b, c])
    if math.isclose(shortest**2 + middle**2, longest**2, rel_tol=1e-9):
        return "Right " + type
    return type


        
      

       


