def create_zero_matrix(rows, cols) :
    """Creates a matrix of zeros with the given number of rows and columns."""
    mat=[] 
    for i in range(rows) :
        row = []
        for j in range(cols) :
            row.append(0)
        mat.append(row)
    return mat

def add_matrices(mat1, mat2) :
    if not(is_matrix(mat1) and is_matrix(mat2)):
        raise ValueError("Invalid format: need two matrices")
    """addition of two matrices of the same size."""
    rows1 = len(mat1)
    rows2 = len(mat2)
    cols1 = len(mat1[0])
    cols2 = len(mat2[0])

    if not(rows1==rows2 and cols1==cols2):
        raise ValueError("Matrices must be the same size")
    else:
        addmat=create_zero_matrix(rows1,cols1)
        for i in range (rows1):
            for j in range (cols1):
                addmat[i][j]=mat1[i][j]+mat2[i][j]
        return addmat
    
def is_scalar(x):
    return isinstance(x, (int, float))


def is_matrix(x):
    return (
        isinstance(x, list) and
        len(x) > 0 and
        all(isinstance(row, list) for row in x)
    )


def scalar_multiplication(s, mat) :
    if is_scalar(s) and is_matrix(mat):
        x = s
        A = mat
    elif is_scalar(mat) and is_matrix(s):
        x = mat
        A = s
    else:
        raise ValueError("Invalid format: need one scalar and one matrix")
     
    rows = len(A)
    cols = len(A[0])

    scalmat=create_zero_matrix(rows,cols)
    for i in range (rows):
        for j in range (cols):
            scalmat[i][j]=A[i][j]*x
    return scalmat

def matrix_multiplication(mat1,mat2):
    if not(is_matrix(mat1) and is_matrix(mat2)):
        raise ValueError("Invalid format: need two matrices")
    rows1 = len(mat1)
    rows2 = len(mat2)
    cols1 = len(mat1[0])
    cols2 = len(mat2[0])
    if not(cols1==rows2):
        raise ValueError("respect matrices size")
    else:
        new_mat=create_zero_matrix(rows1, cols2)
        for i in range (rows1):
            for j in range (cols2):
                for k in range(cols1):
                    new_mat[i][j]+=mat1[i][k]*mat2[k][j]
        return new_mat

    

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

C = [
    [1, 2, 3],
    [4, 5, 6]
]

D = [
    [7, 8],
    [9, 10],
    [11, 12]
]
print(matrix_multiplication(A,B))