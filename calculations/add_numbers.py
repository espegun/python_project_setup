import numpy as np


def add_numbers(x1: int, x2: int) -> int:
    """
    Add the two numbers and return the result.
    Use the amazing capabilities of numpy!
    """

    n1 = np.array([x1])
    n2 = np.array([x2])
    n = n1 + n2
    x = int(n[0])

    return x
