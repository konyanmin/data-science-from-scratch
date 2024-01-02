from typing import List
from collections import Counter
import linear_algebra_practice as la
import math

Vector = List[float]

def mean(xs: Vector) -> float:
    return sum(xs) / len(xs)

assert mean([1, 2, 3]) == 2

def _median_odd(xs: Vector) -> float:
    return sorted(xs)[len(xs) // 2]

def _median_even(xs: Vector) -> float:
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2

def median(v: Vector) -> float:
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2

def quantile(xs: Vector, p: int) -> float:
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]

def mode(x: Vector) -> float:
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]

def data_range(xs: Vector) -> float:
    return max(xs) - min(xs)

def de_mean(xs: Vector) -> float:
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: Vector) -> float:
    assert len(xs) >= 2, "variance requires at least two elements"

    n = len(xs)
    deviation = de_mean(xs)
    return la.sum_of_squares(deviation) / (n - 1)

def standard_deviation(xs: Vector) -> float:
    return math.sqrt(variance(xs))

def interquartile_range(xs: Vector) -> float:
    return quantile(xs, 0.75) - quantile(xs, 0.25)

def covariance(xs: Vector, ys: Vector) -> float:
    assert len(xs) == len(ys), "xs and ys must have same number of elements"
    return la.dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)

def correlation(xs: Vector, ys: Vector) -> float:
    """Meausre how much xs and ys vary in tandam about their mean"""
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        0 # if no variance corelation is zero