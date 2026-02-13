#!/usr/bin/env python3
"""
    a function def poly_derivative(poly):
    that calculates the derivative of a polynomial
"""

def poly_derivative(poly):
    """
        calculates the derivative of a polynomial
    """

    # Validate poly
    if (not isinstance(poly, list) or
        len(poly) == 0 or
        not all(isinstance(x, (int, float)) for x in poly)):
        return None

    # If polynomial is constant
    if len(poly) == 1:
        return [0]

    # Compute derivative
    derivative = [poly[i] * i for i in range(1, len(poly))]

    return derivative
