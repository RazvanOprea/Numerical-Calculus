import numpy as np

epsilon = 0.000001


def get_V0(A, n):
    At = np.transpose(A)

    maxx = -1
    for i in range(0, n):
        summ = 0
        for j in range(0, n):
            summ = summ + abs(A[i][j])
        if summ > maxx:
            maxx = summ
    A1 = maxx

    maxx = -1
    for i in range(0, n):
        summ = 0
        for j in range(0, n):
            summ = summ + abs(A[j][i])
        if summ > maxx:
            maxx = summ
    Ainf = maxx

    V0 = At / (A1 * Ainf)

    return V0


def generate_A(n):
    A = np.zeros((n, n))

    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                A[i][j] = 1
            if i + 1 == j:
                A[i][j] = 4

    return np.array(A)


def first_part(V, A, n):
    the_I = 2 * np.identity(n)
    subtract = np.subtract(the_I, np.dot(A, V))
    V_new = np.dot(V, subtract)
    return V_new


def second_part(V, A, n):
    the_I = 3 * np.identity(n)
    subtract = np.subtract(the_I, np.dot(A, V))
    multiply = np.dot(np.dot(A, V), subtract)
    subtract2 = np.subtract(the_I, multiply)
    V_new = np.dot(V, subtract2)
    return V_new


def third_part(V, A, n):
    the_I = 3 * np.identity(n)
    subtract1 = np.subtract(the_I, np.dot(V, A))
    subtract2 = np.subtract(np.identity(n), np.dot(V, A))
    at_pow = np.dot(subtract1, subtract1)
    multiply = np.dot(subtract2, at_pow) * 1 / 4
    adding = np.add(multiply, np.identity(n))
    V_new = np.dot(adding, V)
    return V_new


def algorithm(A, n):
    V0 = V1 = get_V0(A, n)
    k = 0
    kmax = 10000

    V1 = third_part(V0, A, n) # modify here the method (first, second, third)
    deltaV = np.subtract(V1, V0)
    deltaV = np.linalg.norm(deltaV, 1)
    k = k + 1
    V0 = V1

    while deltaV >= epsilon and k <= kmax and deltaV <= 10000000000:
        V1 = third_part(V0, A, n) # modify here the method
        deltaV = np.subtract(V1, V0)
        deltaV = np.linalg.norm(deltaV, 1)
        k = k + 1
        V0 = V1

    if deltaV <= epsilon:
        print("Numpy Inverse:", np.linalg.inv(A))
        print("My Inverse:", V1, "Nb iters:", k)
        product = np.dot(A, V1)
        subtract = np.subtract(product, np.identity(n))
        print("Norm:", np.linalg.norm(subtract, 1))
    else:
        print("divergenta")


my_N = 6

A = generate_A(my_N)

algorithm(A, my_N)
