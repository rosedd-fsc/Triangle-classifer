# Triangle Classifier

Classifies three side lengths as Invalid, Equilateral, Isosceles, or Scalene,
and prefixes "Right " when the sides satisfy the Pythagorean theorem.

# How to run the tests

```
python -m venv venv
venv\Scripts\activate        
pytest -v
```
# Why an equilateral triangle can never be right
An equilateral triangle can never be a right triangle because all sides have to equal 60 degrees while a right triangle must have one angle  = 90 degrees. Due to the sum of any triangle needing to be 180 degrees it is not possible for an equilateral triangle to become a right angle. 

# Equivalence classes and boundaries
Class: |   Example: |  Expected:

All sides equal |  (5, 5, 5) |  Equilateral

Exactly two sides equal | (5, 5, 8) | Isosceles 

All sides different | (4, 5, 6) | Scalene |

A side is zero or negative | (0, 5, 5), (-1, 2, 2) | Invalid 

Triangle inequality fails | (1, 2, 10) | Invalid 

Right triangle, integer sides | (3, 4, 5) | Right Scalene 

Right triangle, decimal sides | (5, 5, 5·√2) | Right Isosceles 


Boundaries:
- Side exactly 0 is "invalid" versus a small positive side is "valid".
- Sum of two sides exactly equal to the third, example: (4, 5, 9), which is
  "Invalid". Just inside, (4, 5, 8), is "Scalene".
- Pythagorean equality, which needs a tolerance (`math.isclose`) for decimals.

# Copilot Review Log

Test: | Copilot-suggested?: | Kept / edited / rejected?: | Why?

test_equilateral | Yes | Kept | Co-pilot kept the assert statement and followed my expectations

test_isosceles | Yes | Kept | Co-pilot kept the assert statement and followed my expectations

test_scalene | Yes | Kept | Co-pilot kept the assert statement and followed my expectations

test_invalid_zero_side  | Yes | Kept | Co-pilot kept the assert statement and followed my expectations

test_degenerate_boundary | Yes | Kept | Co-pilot kept the assert statement and followed my expectations

test_right_triangle_non_integer | Yes | Edited | Co-pilot forgot to assert with math.isclose() method


# Acceptance Critera 

Customer requirements: stained-glass studio, three sides in, shape and
buildability out, show a message instead of crashing on invalid input, flag
right angles, must be correct every time.

- AC1: when the customer enters sides (3, 3, 6),  where two shorter sides sum exactly to the longest, classify_triangle returns exactly "Invalid" and does not raise an error.
- AC2: when the customer enters sides (3, 4, 5), which form a right angle, classify_triangle returns exactly "Right Scalene" so the piece is flagged.
   
# AI-use disclosure

Tools used:
- Copilot was used for drafts of the unit test cases for the test_triangle.py file. 
 I also reviewed the suggestions made by Copilot in my logs.
- Claude for assitance.

What I used Claude for: 
- To explain the logic of the assginement and a rough draft idea of the triangle.py file
- Explaining how to turn the customer requiremnts into acceptable criteria and review the ones I made myself
- Explain what math.isclose() is used for

What I verified myself: 
- Ran the pytest and verified if they passed correctly or not
- Checked each expected value in my tests against the spec table rather than against what my code returned.
- Confirmed my understanding of the acceptance critera.
- Ran the classifier by hand on sample inputs such as (3, 4, 5) and (4, 5, 9).







