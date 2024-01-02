from typing import List

Vector = List[float]

def add(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vector must be the same length"

    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

def subtract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vector must be the same length"

    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]

def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, "no vectors provided!"

    # check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

assert vector_sum([[1, 2], [2, 3], [3, 4]]) == [6, 9]

def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplies every elements by c"""
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2]) == [2, 4]

def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]

def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w), "vectors must be the same size"

    return sum([v_i * w_i for v_i, w_i in zip(v, w)])

assert dot([1, 2], [1, 2]) == 5

def sum_of_squares(v: Vector) -> float:
    return dot(v, v)

assert sum_of_squares([1, 2]) == 5

import math

def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))

assert magnitude([3, 4]) == 5

def distance(v: Vector, w:Vector) -> float:
    return magnitude(subtract(v, w))

from typing import Tuple

Matrix = List[Vector]

def shape(A: Matrix) -> Tuple[int, int]:
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)

def get_row(A: Matrix, i: int) -> Vector:
    return A[i]

def get_column(A: Matrix, j: int) -> Vector:
    return [A_i[j] for A_i in A]

from typing import Callable

def make_matrix(num_rows: int, num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Returns a num_rows x num_cols matrix
    """
    return [[entry_fn(i, j)
            for j in range(num_cols)]
            for i in range(num_rows)]

def identity_matrix(n: int) -> Matrix:
    """Returns the n x n identity matrix"""

    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

assert identity_matrix(3) == [[1, 0, 0],
                              [0, 1, 0],
                              [0, 0, 1]]