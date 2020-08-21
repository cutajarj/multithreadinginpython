import time
from random import Random

matrix_size = 60
# matrixA = [[3, 1, -4],
#            [2, -3, 1],
#            [5, -2, 0]]
# matrixB = [[1, -2, -1],
#            [0, 5, 4],
#            [-1, -2, 3]]
matrixA = [[0] * matrix_size for a in range(matrix_size)]
matrixB = [[0] * matrix_size for b in range(matrix_size)]
result = [[0] * matrix_size for r in range(matrix_size)]
random = Random()


def generate_random_matrix(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            matrix[row][col] = random.randint(-5, 5)


start = time.time()
for t in range(100):
    generate_random_matrix(matrixA)
    generate_random_matrix(matrixB)
    for row in range(matrix_size):
        for col in range(matrix_size):
            for i in range(matrix_size):
                result[row][col] = result[row][col] + matrixA[row][i] * matrixB[i][col]
    # for row in range(matrix_size):
    #     print(matrixA[row], matrixB[row], result[row])
    # print()
end = time.time()
print("Done, time taken", end - start)