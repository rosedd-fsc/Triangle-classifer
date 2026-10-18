from triangle import classify_triangle


def test_stained_glass_acceptance():
    # AC1: when the customer enters sides (3, 3, 6), 
    # where two shorter sides sum exactly to the longest, 
    # classify_triangle returns exactly "Invalid" and does not raise an error.

    result = classify_triangle(3, 3, 6)
    assert result == "Invalid", f"AC1 failed: (3, 3, 6) should be 'Invalid' but got '{result}'"

   # AC2: when the customer enters sides (3, 4, 5), 
   # which form a right angle,
   # classify_triangle returns exactly "Right Scalene" so the piece is flagged.
   
    result2 = classify_triangle(3, 4, 5)
    assert result2 == "Right Scalene", f"AC2 failed: (3, 4, 5) should be 'Right Scalene' but got '{result2}'"
   