#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # get each row
    # from each row square the values
    # store row in map
    # from map return new matrix
    
    new_matrix = {}

    for idx, row in enumerate(matrix):        
        new_matrix[idx] =[]
        for col in row:
            new_matrix[idx].append(col*col)

    return [new_matrix[i] for i in range(0,idx)]