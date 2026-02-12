"""
================================================================================
ROBOTICS MATRIX LIBRARY (RML)
Developed by: [Ahmed Janzouri/ahmed-janzouri]
Version: 1.0.0
Description: A lightweight, pure-Python library for matrix operations including
             Gaussian elimination, determinants, and transformations for 
             robotic kinematics.
================================================================================
"""
import math 
def create_zero_matrix(rows, cols):
    """
    Initializes a matrix filled with zeros.
    Args: rows (int), cols (int)
    Returns: List[List[float]]
    """
    return [[0 for _ in range(cols)] for _ in range(rows)]

def create_identity_matrix(n):
    """
    Creates an n x n identity matrix with 1s on the main diagonal.
    """
    mat = create_zero_matrix(n, n)
    for i in range(n):
        mat[i][i] = 1
    return mat

def is_matrix(x):
    """Validates if the input is a properly formatted list of lists."""
    return (
        isinstance(x, list) and
        len(x) > 0 and
        all(isinstance(row, list) for row in x)
    )

def is_scalar(x):
    """Checks if input is a numeric scalar."""
    return isinstance(x, (int, float))

def add_matrices(mat1, mat2):
    """Performs element-wise addition of two matrices."""
    if not (is_matrix(mat1) and is_matrix(mat2)):
        raise ValueError("Inputs must be matrices.")
    
    rows, cols = len(mat1), len(mat1[0])
    if rows != len(mat2) or cols != len(mat2[0]):
        raise ValueError("Matrices must have identical dimensions.")

    result = create_zero_matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            result[i][j] = mat1[i][j] + mat2[i][j]
    return result

def scalar_multiplication(s, mat):
    """Multiplies a matrix by a scalar value."""
    if not is_scalar(s):
        s, mat = mat, s # Handle case where scalar is the second argument
    
    rows, cols = len(mat), len(mat[0])
    result = create_zero_matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            result[i][j] = mat[i][j] * s
    return result

def matrix_multiplication(mat1, mat2):
    """
    Performs matrix multiplication (Dot Product).
    Rule: Columns of Mat1 must equal Rows of Mat2.
    """
    rows1, cols1 = len(mat1), len(mat1[0])
    rows2, cols2 = len(mat2), len(mat2[0])
    
    if cols1 != rows2:
        raise ValueError("Dimension mismatch: Cols of A must match Rows of B.")

    result = create_zero_matrix(rows1, cols2)
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

def matrix_transpose(mat):
    """Returns the transpose of the matrix (rows become columns)."""
    rows, cols = len(mat), len(mat[0])
    result = create_zero_matrix(cols, rows)
    for i in range(rows):
        for j in range(cols):
            result[j][i] = mat[i][j]
    return result

def matrix_determinant(mat):
    
    """
    Calculates the determinant using Gaussian Elimination.
    Efficient for large matrices (O(n^3)).
    """
    if not is_matrix(mat) or len(mat) != len(mat[0]):
        raise ValueError("Determinant requires a square matrix.")

    n = len(mat)
    # Create a copy to avoid modifying the original
    temp = [row[:] for row in mat]
    det = 1
    sign = 1

    for i in range(n):
        # Pivoting
        pivot_row = i
        for r in range(i + 1, n):
            if abs(temp[r][i]) > abs(temp[pivot_row][i]):
                pivot_row = r

        if temp[pivot_row][i] == 0:
            return 0

        if pivot_row != i:
            temp[i], temp[pivot_row] = temp[pivot_row], temp[i]
            sign *= -1

        # Elimination
        for r in range(i + 1, n):
            factor = temp[r][i] / temp[i][i]
            for c in range(i, n):
                temp[r][c] -= factor * temp[i][c]

    for i in range(n):
        det *= temp[i][i]

    return sign * det

def create_rotation_matrix_2d(angle_degrees):

    """
    Creates a 2x2 rotation matrix for a given angle in degrees.
    Formula: [[cos(t), -sin(t)], [sin(t), cos(t)]]
    """
    if not is_scalar(angle_degrees):
        raise ValueError("Angle must be a numeric scalar.")
    
    # Convert degrees to radians for Python's math functions
    theta = math.radians(angle_degrees)
    
    c = math.cos(theta)
    s = math.sin(theta)
    
    # Building the rotation matrix
    return [
        [c, -s],
        [s,  c]
    ]

def matrix_inverse(mat):

    """
    Computes the inverse of a square matrix using Gauss-Jordan elimination.
    Raises ValueError if the matrix is not square or not invertible.
    """
    if not is_matrix(mat) or len(mat) != len(mat[0]):
        raise ValueError("Inverse requires a square matrix.")
    
    n = len(mat)
    
    # Check if matrix is invertible
    if abs(matrix_determinant(mat)) < 1e-12:
        raise ValueError("Matrix is singular and not invertible.")
    
    # Create copies to avoid modifying the original
    A = [row[:] for row in mat]
    I = create_identity_matrix(n)
    
    # Gauss-Jordan elimination
    for i in range(n):
        # Partial pivoting
        pivot_row = i
        for r in range(i + 1, n):
            if abs(A[r][i]) > abs(A[pivot_row][i]):
                pivot_row = r
        
        if pivot_row != i:
            A[i], A[pivot_row] = A[pivot_row], A[i]
            I[i], I[pivot_row] = I[pivot_row], I[i]
        
        # Scale pivot row
        pivot = A[i][i]
        for c in range(n):
            A[i][c] = A[i][c] / pivot
            I[i][c] = I[i][c] / pivot
        
        # Eliminate column
        for r in range(n):
            if r == i:
                continue
            factor = A[r][i]
            for c in range(n):
                A[r][c] -= factor * A[i][c]
                I[r][c] -= factor * I[i][c]
    
    return I
# ================================================================================
# END OF LIBRARY
# ================================================================================