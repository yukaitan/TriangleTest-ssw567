"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
@author: Yukai Tan
"""

    # require that the input values be >= 0 and <= 200
def classify_triangle(a_side, b_side, c_side):
    """require that the input values be >= 0 and <= 200"""
    if a_side > 200 or b_side > 200 or c_side > 200:
        return 'InvalidInput'

    if a_side <= 0 or b_side <= 0 or c_side <= 0:
        return 'InvalidInput'

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a_side, int) and isinstance(b_side, int) and isinstance(c_side, int)):
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a_side + b_side <= c_side) or (a_side + c_side <= b_side) or (b_side + c_side <= a_side):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    ans = ''
    if a_side == b_side and b_side == c_side:
        ans = 'Equilateral'
    elif ((a_side ** 2) + (b_side ** 2)) == (c_side ** 2) or \
        ((a_side ** 2) + (c_side ** 2)) == (b_side ** 2) or \
            ((b_side ** 2) + (c_side ** 2)) == (a_side ** 2):
        ans = 'Right'
    elif (a_side != b_side) and (b_side != c_side) and (a_side != c_side):
        ans = 'Scalene'
    else:
        ans = 'Isoceles'

    return ans
