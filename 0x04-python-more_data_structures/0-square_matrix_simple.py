#!/usr/bin/python3
def square_matrix_simple(matrix=[]) 
    
    new_matrix = {}
    n = len(matrix)

    for idx, row in enumerate(matrix):
        new_matrix[idx] =[]
        for col in row:
            new_matrix[idx].append(col*col)

    return [new_matrix[i] for i in range(0,n)]
