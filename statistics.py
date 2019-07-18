import random
import math
from collections import Counter
from typing import List
from linear_algebra import sum_of_squares
from linear_algebra import vector_dot

def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)

def median(xs : List[float]) ->float:
    sorted_xs = sorted(xs)
    n = len(xs)
    if n % 2 == 1:
        return sorted_xs[n//2]
    else:
        return (sorted_xs[n//2-1] + sorted_xs[n//2]) / 2
    
def quantile(xs : List[float], p :float) -> float:
    sorted_xs = sorted(xs)
    return sorted_xs[int(len(sorted_xs) * p)]

def iqr(xs : List[float]) -> float:
    return quantile(xs, 0.75) - quantile(xs, 0.25)

def mode(xs: List[float]) -> List[float]:
    counter = Counter(xs)
    max_count = max(counter.values())
    return [xi for xi, count in counter.items() if count == max_count]

def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)

def de_mean(xs: List[float]) -> List[float]:
    xbar = mean(xs)
    return [x - xbar for x in xs]

def variance(xs: List[float]) -> float:
    return sum_of_squares(de_mean(xs)) / ( len(xs) - 1)

def standard_deviation(xs: List[float]) -> float:
    return math.sqrt(variance(xs))

def interquartile_range(xs: List[float]) ->float:
    return quantile(xs, .75) - quantile(xs, 0.25)

def covariance(xs: List[float], ys:List[float]) -> float:
    return vector_dot(de_mean(xs), de_mean(ys)) / ( len(xs) - 1 )

def correlation(xs: List[float], ys:List[float]) -> float:
    return covariance(xs, ys) / (standard_deviation(xs) * standard_deviation(ys))

def outlier_bound(xs: List[float]) -> List[float]:
    return [ quantile(xs, 0.25) - (iqr(xs)* 1.5), quantile(xs, 0.75) + (iqr(xs)* 1.5)] 

