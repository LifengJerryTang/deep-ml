import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    top_deri = derivative_of_poly(g_coeffs, x)
    bottom_deri = derivative_of_poly(h_coeffs, x)
    top_eval = deriative_eval(g_coeffs, x)
    bottom_eval = deriative_eval(h_coeffs, x)

    if bottom_eval == 0:
        return -1

    return (-top_eval * bottom_deri + bottom_eval * top_deri) / (pow(bottom_eval, 2))


def deriative_eval(coeffs, x):
    res = 0
    n = len(coeffs)
    j = n - 1

    for i in range(n):
        res += coeffs[i] * pow(x, j)
        j -= 1

    return res

def derivative_of_poly(coeffs: list, x: float):
    res = 0
    n = len(coeffs)
    j = n - 1

    for i in range(n):
        res += pow_rule(coeffs[i], j, x)
        j -= 1

    return res


def pow_rule(c, n, x):
    if n == 0:
        return 0

    return n * c * pow(x, n - 1)