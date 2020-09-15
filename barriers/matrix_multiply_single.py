import time
from random import Random

matrix_size = 200
# matrix_a = [[3, 1, -4],
#            [2, -3, 1],
#            [5, -2, 0]]
# matrix_b = [[1, -2, -1],
#            [0, 5, 4],
#            [-1, -2, 3]]
matrix_a = [[0] * matrix_size for a in range(matrix_size)]
matrix_b = [[0] * matrix_size for b in range(matrix_size)]
result = [[0] * matrix_size for r in range(matrix_size)]
random = Random()


def generate_random_matrix(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            matrix[row][col] = random.randint(-5, 5)


start = time.time()
for t in range(10):
    generate_random_matrix(matrix_a)
    generate_random_matrix(matrix_b)
    result = [[0] * matrix_size for r in range(matrix_size)]
    for row in range(matrix_size):
        for col in range(matrix_size):
            for i in range(matrix_size):
                result[row][col] += + matrix_a[row][i] * matrix_b[i][col]
#     for row in range(matrix_size):
#         print(matrix_a[row], matrix_b[row], result[row])
#     print()
end = time.time()
print("Done, time taken", end - start)
