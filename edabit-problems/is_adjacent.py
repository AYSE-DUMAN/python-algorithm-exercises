def is_adjacent(matrix, node1, node2):
    return matrix[node1][node2] == 1

if __name__ == "__main__":
    matrix1 = [[0,1,0,0],[1,0,1,1],[0,1,0,1],[0,1,1,0]]
    matrix2 = [[0,1,0,1,1], [1,0,1,0,0],[0,1,0,1,0],[1,0,1,0,1],[1,0,0,1,0]]

    print(is_adjacent(matrix1,1,2))
    print(is_adjacent(matrix2,1,4))

