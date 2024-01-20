# -*- coding: utf-8 -*-
"""bot assistant.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/114k-q8ZHkC7vAe1zE89XjTN0sMi9_n9u
"""

import numpy as np

def reader(file_path):
    arr_list = []
    with open(file_path, 'r') as file:
        n, m = map(int, file.readline().split())
        for i in range(m*n):
            matrix_row = np.array(list(map(int, file.readline().split())))
            arr_list.append(matrix_row)
        new_arr = np.array(arr_list)
        matrices = new_arr.reshape(n,m,m)
    return matrices

file = input('input the name of file: ')

def caldet(matrix):
    return np.linalg.det(matrix)

def dot_producter(matrix_array):
    result_list = []
    indices_list = []

    for i in range(len(matrix_array)):
        for j in range(i + 1, len(matrix_array)):
            result_list.append(np.dot(matrix_array[i], matrix_array[j]))
            indices_list.append((i, j))

    return result_list, indices_list

arr = np.array(reader(file))
matrice_list, indices_list = dot_producter(arr)
determinants = [caldet(matrix) for matrix in matrice_list]
max_determinant_index = np.argmax(determinants)
indices_of_max_determinant = indices_list[max_determinant_index]
matrix1_index, matrix2_index = indices_of_max_determinant
matrix1 = arr[matrix1_index]
matrix2 = arr[matrix2_index]
determinant_matrix1 = caldet(matrix1)
determinant_matrix2 = caldet(matrix2)

if determinant_matrix1 > determinant_matrix2:
    result_matrix = np.dot(matrix1, matrix2)
else:
    result_matrix = np.dot(matrix2, matrix1)

inverse_result_matrix = np.linalg.inv(result_matrix)
rounded = np.round(inverse_result_matrix, 3)

for r in rounded:
    print(" ".join(map(str, r)))