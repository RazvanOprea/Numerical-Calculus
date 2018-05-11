import numpy as np


def read_file(filename):
    f = open(filename, "r")
    n = int(f.readline())  # value of n
    vector_b = []
    f.readline()  # empty line
    for i in range(0, n):
        line = float(f.readline())
        vector_b += [line]
    f.readline()  # empty line
    lines = f.readlines()  # matrix
    matrix = []
    for line in lines:
        data = line.split(',')
        matrix.append((float(data[0]), int(data[1]), int(data[2])))
    f.close()
    return n, vector_b, matrix


def diagonal_element(vector, line):
    found = False
    index = 0
    for index in range(len(vector[line])):
        if vector[line][index][1] == line:
            found = True
            break
    if found:
        n = len(vector[line]) - 1
        temp_val = vector[line][n][0]
        temp_col = vector[line][n][1]
        vector[line][n][0] = vector[line][index][0]
        vector[line][n][1] = vector[line][index][1]
        vector[line][index][0] = temp_val
        vector[line][index][1] = temp_col


def sparse_matrix(n, matrix):
    new_matrix = dict()
    for element in matrix:
        el = element[0]
        i = element[1]
        j = element[2]
        row_elements = new_matrix.get(i)
        if row_elements != None:
            same_col = False
            for row_element in row_elements:
                if row_element[1] == j:
                    row_element[0] += el
                    same_col = True
                    break
            if not same_col:
                row_elements.append([el, j])
                new_matrix[i] = row_elements
                #diagonal_element(new_matrix[i], i)
        else:
            temp_list = list()
            temp_list.append([el, j])
            new_matrix[i] = temp_list
    my_vector = [[] for _ in range(n)]
    for index in range(0, n):
        elem = new_matrix.get(index)
        if elem != None:
            temp = list()
            for (val, col) in elem:
                temp.append([val, col])
            my_vector[index].extend(temp)
        else:
            my_vector[index].append(0)
    return my_vector


def sparse_matrix2(n, matrix):
    new_matrix = dict()
    for element in matrix:
        el = element[0]
        j = element[1]
        i = element[2]
        row_elements = new_matrix.get(i)
        if row_elements != None:
            same_col = False
            for row_element in row_elements:
                if row_element[1] == j:
                    row_element[0] += el
                    same_col = True
                    break
            if not same_col:
                row_elements.append([el, j])
                new_matrix[i] = row_elements
        else:
            temp_list = list()
            temp_list.append([el, j])
            new_matrix[i] = temp_list
    my_vector = [[] for _ in range(n)]
    for index in range(0, n):
        elem = new_matrix.get(index)
        if elem != None:
            temp = list()
            for (val, col) in elem:
                temp.append([val, col])
            my_vector[index].extend(temp)
        else:
            my_vector[index].append(0)
    return my_vector


def equal_matrices(m1, m2, epsilon):
    if len(m1) != len(m2):
        return False
    for i in range(0, len(m1)):
        if len(m1[i]) != len(m2[i]):
            #print(str(len(m1[i])) + ' '+ str(len(m2[i])) + '<------' +str(i))
            return False
        m1_ord_line = sorted(m1[i], key=lambda el: (el[1], el[0]))
        m2_ord_line = sorted(m2[i], key=lambda el: (el[1], el[0]))
        for j in range(0, len(m1[i])):
            if m1_ord_line[j][1] != m2_ord_line[j][1] or abs(m1_ord_line[j][0] - m2_ord_line[j][0]) > epsilon:
                return False
    return True


def equal_vectors(v1, v2):
    epsilon = 0.1
    if len(v1) != len(v2):
        return False
    for i in range(0, len(v1)):
        if abs(v1[i] - v2[i]) > epsilon:
            return False
    return True


def add_matrices(m1, m2):
    if len(m1) != len(m2):
        print("Error matrices addition")
        return -1
    m = [[] for _ in range(len(m1))]
    for i in range(0, len(m1)):
        for j in range(0, len(m1[i])):
            m[i].append([m1[i][j][0], m1[i][j][1]])
    for i in range(0, len(m2)):
        for j in range(0, len(m2[i])):
            found = False
            for k in range(0, len(m[i])):
                if m2[i][j][1] == m[i][k][1]:
                    m[i][k][0] += m2[i][j][0]
                    found = True
                    break
            if not found:
                m[i].append([m2[i][j][0], m2[i][j][1]])
    return m


def column_element(m, line, col):
    for i in range(0, len(m[line])):
        if m[line][i][1] == col:
            return m[line][i][0]
    return 0


def multiply_matrices(m1, m2):
    if len(m1) != len(m2):
        print("Error multiply matrices")
        return -1
    m = [[] for _ in range(len(m1))]
    for i in range(0, len(m1)):
        for col in range(0, len(m1)):
            element_sum = 0
            for j in range(0, len(m1[i])):
                element_sum += m1[i][j][0] * column_element(m2, m1[i][j][1], col)
            if element_sum:
                m[i].append([element_sum, col])
    return m


def multiply_matrices2(m1, m2):
    # 0 x 0
    m = [[] for _ in range(len(m1))]
    for i in range(0, len(m1)):
        for j in range(0,len(m1)):
            a = m1[i]
            b = m2[j]
            v = np.zeros((len(m1),), dtype=float)
            sum = 0
            for x in a:
                v[x[1]] = x[0]
            for x in b:
                if v[x[1]] != 0:
                    sum += v[x[1]] * x[0]
            if sum != 0:
                m[i].append([sum, j])
    return m


def multiply_vector(m):
    #m = matrix, b = vector
    x = [i for i in range(1, len(m) + 1)]
    x.sort(reverse=True)
    my_vector = list()
    for i in range(0, len(m)):
        temp_sum = 0
        for j in range(0, len(m[i])):
            temp_sum += m[i][j][0] * x[m[i][j][1]]
        my_vector.append(temp_sum)
    return my_vector


def print_matrix(m, filename):
    f = open(filename, 'w')
    for i in range(0, len(m)):
        f.write(str(i) + ': ')
        m_sorted = sorted(m[i], key=lambda el: (el[1], el[0]))
        for j in m_sorted:
            f.write(str(j) + ', ')
        f.write('\n')
    f.close()


if __name__ == "__main__":
    n1, b1, A = read_file("a.txt")
    n2, b2, B = read_file("b.txt")
    n3, b3, AplusB = read_file("aplusb.txt")
    n4, b4, AoriB = read_file("aorib.txt")

    A_sparse = sparse_matrix(n1, A)
    B_sparse = sparse_matrix(n2, B)
    AplusB_sparse = sparse_matrix(n3, AplusB)
    AoriB_sparse = sparse_matrix(n4, AoriB)
    B_sparse_reverse = sparse_matrix2(n2, B)    # swap rows with columns

    matrices_sum = add_matrices(A_sparse, B_sparse)                             # A + B
    m_vector = multiply_vector(A_sparse)                                        # A * x
    m2_vector = multiply_vector(B_sparse)                                       # B * x
    matrices_multiplication = multiply_matrices2(A_sparse, B_sparse_reverse)    # A * B

    print("A + B = AplusB --> " + str(equal_matrices(AplusB_sparse, matrices_sum, 0.1)))
    print("A * x = b --> " + str(equal_vectors(m_vector, b1)))
    print("B * x = b --> " + str(equal_vectors(m2_vector, b2)))
    print("A * B = AoriB --> " + str(equal_matrices(AoriB_sparse, matrices_multiplication, 0.1)))

    print_matrix(AplusB_sparse, "aplusb_fisier.txt")
    print_matrix(matrices_sum, "aplusb_calculat.txt")
    print_matrix(AoriB_sparse, "aorib_fisier.txt")
    print_matrix(matrices_multiplication, "aorib_calculat.txt")

    print("------------------------------")
    print("A * x [first 10]: " + str(m_vector[:10]))
    print("b a.txt [first 10]: " + str(b1[:10]))
    print("B * x [first 10]: " + str(m2_vector[:10]))
    print("b b.txt [first 10]: " + str(b2[:10]))






