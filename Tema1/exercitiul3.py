from tkinter import *
from math import ceil, log
import numpy as np


def print_matrix(matrix):
    for line in matrix:
        print("\t".join(map(str, line)))


def get_matrix(matrix):
    my_matrix = ""
    for line in matrix:
        my_matrix += "  ".join(map(str, line)) + '\n'
    return my_matrix


def add_zeros(matrix):
    next_power_of_2 = lambda n: 2 ** int(ceil(log(n, 2)))
    n = len(matrix[0])  # nr col
    m = len(matrix)  # nr linii
    if n > m:
        m_size = next_power_of_2(n)
        temp_matrix = np.zeros((m_size, m_size), dtype=int)
    else:
        m_size = next_power_of_2(m)
        temp_matrix = np.zeros((m_size, m_size), dtype=int)
    matrix = np.array(matrix)
    temp_matrix[:matrix.shape[0], :matrix.shape[1]] = matrix
    return temp_matrix


# split matrix into quarters
def split(matrix):
    matrix_size = int(len(matrix[0])/2)
    top_left = matrix[0:matrix_size, 0:matrix_size].copy()
    bottom_left = matrix[matrix_size:, 0:matrix_size].copy()
    top_right = matrix[0:matrix_size, matrix_size:].copy()
    bottom_right = matrix[matrix_size:, matrix_size:].copy()
    return top_left, top_right, bottom_left, bottom_right


def strassen(A, B, d):
    A = np.array(A)
    B = np.array(B)
    n = A.shape[0]  # verificam dimensiunea matricii
    if n <= 2**d:
        return A.dot(B)
    else:
        a11, a12, a21, a22 = split(A)
        b11, b12, b21, b22 = split(B)
        p1 = strassen(a11 + a22, b11 + b22, d)
        p2 = strassen(a21 + a22, b11, d)
        p3 = strassen(a11, b12 - b22, d)
        p4 = strassen(a22, b21 - b11, d)
        p5 = strassen(a11 + a12, b22, d)
        p6 = strassen(a21 - a11, b11 + b12, d)
        p7 = strassen(a12 - a22, b21 + b22, d)

        c11 = p1 + p4 - p5 + p7
        c12 = p3 + p5
        c21 = p2 + p4
        c22 = p1 + p3 - p2 + p6

        # group back c11, c12, c21 and c22 into C
        C = np.vstack([np.hstack([c11, c12]), np.hstack([c21, c22])])
        return C.astype(int)


if __name__ == "__main__":
    master = Tk()
    master.title('Ex3')
    master.geometry("500x500")

    matrixA = np.loadtxt("matrixA.txt", dtype='i', delimiter=',')
    matrixB = np.loadtxt("matrixB.txt", dtype='i', delimiter=',')

    nr_col_matrixA = len(matrixA[0])
    nr_lines_matrixB = len(matrixB)
    if nr_lines_matrixB == nr_col_matrixA:
        matrixA = add_zeros(matrixA)
        matrixB = add_zeros(matrixB)
        matrixC = strassen(matrixA, matrixB, 0)
        verify_result = matrixA.dot(matrixB)
        print("Verificare rezultat A * B: ")
        print_matrix(verify_result)

        Label(master, text='Matricea A (cu 0-uri):\n' + str(get_matrix(matrixA)) + '\n\n'
                           +'Matricea B (cu 0-uri):\n' + str(get_matrix(matrixB)) + '\n\n'
                           +'Rezultatul A * B:\n' + str(get_matrix(matrixC)) + '\n\n').pack()
        master.mainloop()
    else:
        Label(master, text = 'Nu se poate face inmultirea!\nPattern: A(m*n) * B (n*p)').pack()
        master.mainloop()

