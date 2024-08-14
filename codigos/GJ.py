
import numpy as np


def gauss_jordan_inverse(matrix):
    n = len(matrix)
    identity = np.identity(n)
    augmented_matrix = np.hstack((matrix, identity))

    for col in range(n):
        pivot_row = None
        for row in range(col, n):
            if augmented_matrix[row, col] != 0:
                pivot_row = row
                break

        if pivot_row is None:
            raise ValueError("Matrix is singular, inverse does not exist.")

        augmented_matrix[[col, pivot_row]] = augmented_matrix[[pivot_row, col]]
        pivot_element = augmented_matrix[col, col]

        augmented_matrix[col] /= pivot_element

        for row in range(n):
            if row == col:
                continue
            multiplier = augmented_matrix[row, col]
            augmented_matrix[row] -= multiplier * augmented_matrix[col]

    inverse = augmented_matrix[:, n:]
    return inverse


# Example usage
matrix = np.array([[2, 1, 1], [1, 2, 1], [3, 2, 3]])
inverse_matrix = gauss_jordan_inverse(matrix)
print("Inverse matrix:\n", inverse_matrix)