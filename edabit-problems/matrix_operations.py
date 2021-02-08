def add_matrix(a,b):
    result = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    # iterate through rows
    for i in range(len(a)):
        # iterate through columns
        for j in range(len(a[0])):
            result[i][j] = a[i][j] + b[i][j]
    
    for k in result:
        print(k)


# second solution for matrix addition
def add_matrix2(a,b):
    result = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    for r in result:
        print(r)


# matrix multiplication
def mult_matrix(a,b):
    result = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    # iterate through row of a
    for r in range(len(a)):
        # iterate through column of b
        for j in range(len(b[0])):
            # iterate through by rows of b
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    
    for r in result:
        print(r)


# second solution for matrix multiplication
def mult_matrix2(a,b):
    result = np.dot(a, b)
    for r in result:
        print(r)

if __name__ == "__main__":
    x = [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    y = [[4,4,4,4],[5,5,5,5],[6,6,6,6]]
    add_matrix(x, y)
    print("---------")
    add_matrix2(x,y)


