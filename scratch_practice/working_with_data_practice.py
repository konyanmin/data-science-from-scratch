from typing import List, Dict, Tuple
from collections import Counter
import math
import tqdm
import matplotlib.pyplot as plt

import statistics_practice as st
import linear_algebra_practice as la
import gradient_descent_practice as gd

Vector = List[float]
Matrix = List[Vector]

def bucketize(point: float, bucket_size: float) -> float:
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points: Vector, bucket_size: float) -> Dict[float, int]:
    return Counter(bucketize(point, bucket_size) for point in points)

def plot_histogram(points: Vector, bucket_size: float, title: str = ""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()

def correlation_matrix(data: Vector) -> Matrix:
    """
    Returns the len(data) x len(data) matrix whose (i, j)-th entry
    is the correlation between data[i] and data[j]
    """
    def correlation_ij(i: int, j: int) -> float:
        return st.correlation(data[i], data[j])
    
    return la.make_matrix(len(data), len(data), correlation_ij)

def scale(data: Matrix) -> Tuple[Vector, Vector]:
    """returns the mean and standard deviation for each position"""
    dim = len(data[0])

    means = la.vector_mean(data)
    stdevs = [st.standard_deviation([vector[i] for vector in data])
              for i in range(dim)]
    return means, stdevs

vectors = [[-3, -1, 1], [-1, 0, 1], [1, 1, 1]]
means, stdevs = scale(vectors)
assert means == [-1, 0, 1]
assert stdevs == [2, 1, 0]

def rescale(data: Matrix) -> Matrix:
    """
    Rescales the input data so that each position has
    mean 0 and standard deviation 1. (Leaves a position
    as is if its standard deviation is 0.)
    """
    dim = len(data[0])
    means, stdevs = scale(data)

    # make a copy of each vector
    rescaled = [v[:] for v in data]

    for v in rescaled:
        for i in range(dim):
            if stdevs[i] > 0:
                v[i] = (v[i] - means[i]) / stdevs[i]

    return rescaled

means, stdevs = scale(rescale(vectors))
assert means == [0, 0, 1]
assert stdevs == [1, 1, 0]

def de_mean(data: Matrix) -> Matrix:
    """Reenters the data to have mean 0 in every dimension"""
    mean = la.vector_mean(data)
    return [la.subtract(vector, mean) for vector in data]

def direction(w: Vector) -> Vector:
    mang = la.magnitude(w)
    return [w_i / mag for w_i in w]

def directional_variance(data: Matrix, w: Vector) -> float:
    """Returns the variance of x in the direction of w"""
    w_dir = direction(w)
    return sum(dot(v, w_dir)**2 for v in data)

def directional_variance_gradient(data: Matrix, w: Vector) -> Vector:
    """The gradient of directional variance with respect to w"""
    w_dir = direction(w)
    return [sum(2 * dot(v, w_dir)) for v in data for i in range(len(w))]

def first_principal_component(data: Matrix, n: int=100, step_size: float=0.1) -> Vector:
    guess = [1.0 for _ in data[0]]

    with tqdm.trange(n) as t:
        for _ in t:
            dv = directional_variance(data, guess)
            gradient = directional_variance_gradient(data, guess)
            guess = gd.gradient_step(guess, gradient, step_size)
            t.set_description(f"dv: {dv:.3f}")
    
    return direction(guess)

def project(v: Vector, w: Vector) -> Vector:
    """return the projection of v onto the direction w"""
    projection_length = dot(v, w)
    return la.scalar_multiply(projection_length, w)

def remove_projection_from_vector(v: Vector, w: Vector) -> Vector:
    """projects v onto w and subtracts the result from v"""
    return subtract(v, project(v, w))

def pca(data: Matrix, num_components: int) -> Matrix:
    components: Matrix = []
    for _ in range(num_components):
        component = first_principal_component(data)
        components.append(component)
        data = remove_projection(data, component)

    return components

def transform_vector(v: Vector, components: Matrix) -> Vector:
    return [dot(v, w) for w in componets]

def transform(data: Matrix, components: Matrix) -> Matrix:
    return [transform_vector(v, components) for v in data]
