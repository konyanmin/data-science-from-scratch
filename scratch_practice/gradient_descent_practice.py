import random

import linear_algebra_practice as la

from typing import Callable, TypeVar, List, Iterator

T = TypeVar('T')

def difference_quotient(f: Callable[[float], float],
                        x: float,
                        h: float) -> float:
    return (f(x + h) - f(x)) / h

def square(x: float) -> float:
    return x * x

def derivative(x: float) -> float:
    return 2 * x

def partial_difference_quotient(f: Callable[[la.Vector], float],
                                v: la.Vector,
                                i: int,
                                h: float = 0.0001) -> float:
    """Returns the i-th partial difference quotient of f at v"""
    w = [v_j + (h if j==i else 0) for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h

def extimate_gradient(f: Callable[[la.Vector], float],
                      v: la.Vector,
                      h: float) -> float:
    return [partial_difference_quotient(f, v, i, h)
            for i in range(len(v))]

def gradient_step(v: la.Vector, gradient: la.Vector, step_size: float) -> la.Vector:
    """Move step_size in the gradient direction from v"""
    assert len(v) == len(gradient)
    step = la.scalar_multiply(step_size, gradient)
    return la.add(v, step)

def sum_of_squares_gradient(v: la.Vector) -> la.Vector:
    return [2 * v_i for v_i in v]

def linear_gradient(x: float, y: float, theta: la.Vector) -> la.Vector:
    slope, intercept = theta
    predicted = slope * x + intercept    # The prediction of the model.
    error = (predicted - y)              # error is (predicted - actual)
    squared_error = error ** 2           # We'll minimize squared error
    grad = [2 * error * x, 2 * error]    # using its gradient.
    return grad

def minibatches(dataset: List[T],
                batch_size: int,
                shuffle: bool=True) -> Iterator[List[T]]:
    """Generate batch sized from the dataset"""
    batch_starts = [start for start in range(0, len(dataset), batch_size)]
    if shuffle: random.shuffle(batch_starts)
    
    for start in batch_starts:
        end = start + batch_size
        yield dataset[start:end]