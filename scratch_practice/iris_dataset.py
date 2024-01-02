# import requests
import os
import csv
import random

from typing import List, Dict, Tuple
from collections import defaultdict
import matplotlib.pyplot as plt

import k_nearest_neighbors_practice as knn
import machine_learning_practice as ml

Vector = List[float]
Matrix = List[Vector]

# data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

# with open(os.path.join(dir_path, 'iris.dat'), 'w') as f:
#     f.write(data.text)

def parse_iris_row(row: List[str]) -> knn.LabeledPoint:
    """
    sepal_length, sepal_width, petal_length, petal_width, class
    """
    measurements = [float(value) for value in row[:-1]]
    # class is e.g. "Iris-virginica"; we just want "virginica"
    if len(row) > 0:
        label = row[-1].split("-")[-1]
    else:
        label = None

    return knn.LabeledPoint(measurements, label)

with open(os.path.join(dir_path, 'iris.dat')) as f:
    reader = csv.reader(f)
    iris_data = [parse_iris_row(row) for row in reader]

# We'll also group just the points by species/label so we can plot them.
points_by_species: Dict[str, List[Vector]] = defaultdict(list)
for iris in iris_data:
    points_by_species[iris.label].append(iris.point)

metrics = ['sepal length', 'sepal width', 'petal length', 'petal width']
pairs = [(i, j) for i in range(4) for j in range(4) if i < j]
marks = ['+', '.', 'x']  # we have 3 classes, so 3 markers

fig, ax = plt.subplots(2, 3)

for row in range(2):
    for col in range(3):
        i, j = pairs[3 * row + col]
        ax[row][col].set_title(f"{metrics[i]} vs {metrics[j]}", fontsize=8)
        ax[row][col].set_xticks([])
        ax[row][col].set_yticks([])

        for mark, (species, points) in zip(marks, points_by_species.items()):
            xs = [point[i] for point in points]
            ys = [point[j] for point in points]
            ax[row][col].scatter(xs, ys, marker=mark, label=species)

ax[-1][-1].legend(loc='lower right', prop={'size': 6})
# plt.show()

random.seed(12)
iris_train, iris_test = ml.split_data(iris_data, 0.7)

confusion_matrix: Dict[Tuple[str, str], int] = defaultdict(int)

