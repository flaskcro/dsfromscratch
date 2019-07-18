from typing import List
from typing import Callable
from typing import Tuple
import math

Matrix = List[List[float]]
Vector = List[float]

def subtract(v:Vector, w:Vector) -> Vector:
    assert len(v) == len(w), 'two vectors must have same length'
    return [v_i - w_i for v_i, w_i in zip(v,w)]

def vector_sum(vectors: List[Vector]) -> Vector:
    num_elements = len(vectors[0])
    assert all(num_elements == len(v) for v in vectors), 'All vectors must have same length'
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

def scalar_multiply(s : float, v : Vector) -> Vector:
    return [s * vi for vi in v]

def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def vector_dot(v: Vector, w:Vector):
    assert len(v) == len(w), 'Two vectors must have same size'
    return sum(vi * wi for vi, wi in zip(v, w))

def sum_of_squares(v: Vector) -> float:
    return vector_dot(v,v)

def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))

def squared_distance(v: Vector, w: Vector) -> float:
    return sum_of_squares(subtract(v,w))

def distance(v: Vector, w: Vector) -> float:
    return math.sqrt(sum_of_squares(subtract(v,w)))

def shape(A: Matrix) -> Tuple[int, int]:
    num_of_rows = len(A)
    num_of_cols = len(A[0])
    return num_of_rows, num_of_cols

def get_row(A: Matrix, i : int) -> Vector:
    assert len(A) > i, 'index cannot be bigger than matrix row size'
    return A[i]

def get_column(A: Matrix, i : int) -> Vector:
    assert len(A[0]) > i, 'index cannot be bigger than matrix column size'
    return [Ai[i] for Ai in A]

def make_matrix(num_rows : int, num_cols : int, entry : Callable[[int, int], float]) -> Matrix:
    return [[entry(row, col) for col in range(num_cols)] for row in range(num_rows)]

from typing import Callable

def make_matrix(num_rows : int, num_cols : int, entry : Callable[[int, int], float]) -> Matrix:
    return [[entry(row, col) for col in range(num_cols)] for row in range(num_rows)]