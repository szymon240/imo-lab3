import tsplib95
import math
import numpy as np
import random
from typing import Callable, Tuple, List, Set
import matplotlib.pyplot as plt
import json


def convert_tsp_to_array(tsp_coords: tsplib95.fields.IndexedCoordinatesField, size: int) -> np.ndarray:
    list_coords = []
    for i in range(1, size + 1):
        list_coords.append(tsp_coords[i])
    return np.array(list_coords)


def load_from_tsp(path: str) -> Tuple[np.ndarray, np.ndarray]:
    problem = tsplib95.load(path)
    coords = problem.node_coords
    n = problem.dimension
    distance_matrix = np.zeros((n, n), dtype=int)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                distance_matrix[i - 1, j - 1] = 0
            else:
                x1, y1 = coords[i]
                x2, y2 = coords[j]
                distance = math.hypot(x1 - x2, y1 - y2)
                distance_matrix[i - 1, j - 1] = round(distance)

    coords_matrix = convert_tsp_to_array(coords, n)
    return distance_matrix, coords_matrix


def initialize_random_cycles(distance_matrix: np.ndarray) -> tuple[list[int], list[int], set[int]]:
    n = len(distance_matrix)
    nodes = list(range(n))

    start_point1 = random.choice(nodes)
    start_point2 = int(np.argmax(distance_matrix[start_point1]))

    remaining_nodes = list(set(nodes) - {start_point1, start_point2})
    random.shuffle(remaining_nodes)

    first_cycle_size = (n + 1) // 2
    second_cycle_size = n // 2

    first_cycle = [start_point1] + remaining_nodes[:first_cycle_size - 1]
    second_cycle = [start_point2] + remaining_nodes[first_cycle_size - 1:]

    first_cycle.append(start_point1)
    second_cycle.append(start_point2)

    return first_cycle, second_cycle, set(nodes)


def cycle_length(cycle, matrix):
    length = 0
    for i in range(1, len(cycle)):
        length += matrix[cycle[i - 1]][cycle[i]]
    return length


def target_function(cycle1: list[int], cycle2: list[int], matrix: np.ndarray) -> int:
    return cycle_length(cycle1, matrix) + cycle_length(cycle2, matrix)