def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0  # number of elements in first row
    return num_rows, num_cols


def get_row(A, i):
    return A[i]


def get_column(A, j):
    return [A_i[j] for A_i in A]


def make_matrix(num_rows, num_cols, entry_fn):
    """return a num_rows x num_cols mattrix
    whose (i,j)th entry is entry_fn(i,j)"""
    return [[entry_fn(i, j)
             for j in range(num_cols)]
            for i in range(num_rows)]


def is_diagonal(i, j):
    """1's on the 'diagonal', 0's everywhere else"""
    return 1 if i == j else 0


def test_identity_matrix():
    matrix = make_matrix(5, 5, is_diagonal)
    assert matrix == [[1, 0, 0, 0, 0],
                      [0, 1, 0, 0, 0],
                      [0, 0, 1, 0, 0],
                      [0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 1]]
