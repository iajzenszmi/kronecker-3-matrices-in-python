import numpy as np

def kronecker_product(A, B):
    """
    Compute the Kronecker product of two matrices A and B.
    """
    # Get the shapes of A and B
    a_rows, a_cols = A.shape
    b_rows, b_cols = B.shape
    
    # Initialize the result matrix with zeros
    result = np.zeros((a_rows * b_rows, a_cols * b_cols))
    
    # Compute the Kronecker product
    for i in range(a_rows):
        for j in range(a_cols):
            result[i * b_rows:(i + 1) * b_rows, j * b_cols:(j + 1) * b_cols] = A[i, j] * B

    return result

# Define three example matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[0, 5], [6, 7]])
matrix3 = np.array([[8, 9], [10, 11]])

# Compute the Kronecker product iteratively
kronecker_result = kronecker_product(matrix1, matrix2)
kronecker_result = kronecker_product(kronecker_result, matrix3)

print(kronecker_result)
