import math

def is_valid_triangle(a, b, c) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
shortest, middle, longest = sorted([a, b, c])
return shortest + middle > longest

def classify_triangle(a, b, c) -> str:
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    if a == b == c: 
        type = "Equilateral"

    elif a ==b or b == c or a ==c:
        type = "Isosceles"

    else:
        type = "Scalene"

    shortest, middle longest = sorted([a, b, c])
    if math.isclose(sho)


        
    

       


