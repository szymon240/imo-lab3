import utils
from steepest_alg import steepest_full
from utils import load_from_tsp

if __name__ == "__main__":
    kroa200_matrix, kroa200_coords = load_from_tsp('datasets/kroA200.tsp')
    krob200_matrix, krob200_coords = load_from_tsp('datasets/kroB200.tsp')
    kroa200_cycle1_random, kroa200_cycle2_random, _ = utils.initialize_random_cycles(kroa200_matrix)
    krob200_cycle1_random, krob200_cycle2_random, _ = utils.initialize_random_cycles(krob200_matrix)

    solution_steepest_full, length_steepest_full, time_steepest_full = steepest_full(kroa200_matrix,
                                                                                     kroa200_cycle1_random,
                                                                                     kroa200_cycle2_random)
    print("\nSteepest local search (all moves) for kroA:")
    print(f"Best solution length: {length_steepest_full}")
    print(f"Execution time: {time_steepest_full:.4f} seconds")

    solution_steepest_full, length_steepest_full, time_steepest_full = steepest_full(krob200_matrix,
                                                                                     krob200_cycle1_random,
                                                                                     krob200_cycle2_random)
    print("\nSteepest local search (all moves) for kroB:")
    print(f"Best solution length: {length_steepest_full}")
    print(f"Execution time: {time_steepest_full:.4f} seconds")