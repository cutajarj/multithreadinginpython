import multiprocessing
import time
from random import Random

from multiprocessing import Barrier

from multiprocessing.context import Process

process_count = 8
matrix_size = 200
random = Random()


def generate_random_matrix(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            matrix[row * matrix_size + col] = random.randint(-5, 5)


def work_out_row(id, matrix_a, matrix_b, result, work_start, work_complete):
    while True:
        work_start.wait()
        for row in range(id, matrix_size, process_count):
            for col in range(matrix_size):
                for i in range(matrix_size):
                    result[row * matrix_size + col] += matrix_a[row * matrix_size + i] * matrix_b[i * matrix_size + col]
        work_complete.wait()


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    work_start = Barrier(process_count + 1)
    work_complete = Barrier(process_count + 1)
    matrix_a = multiprocessing.Array('i', [0] * (matrix_size * matrix_size), lock=False)
    matrix_b = multiprocessing.Array('i', [0] * (matrix_size * matrix_size), lock=False)
    result = multiprocessing.Array('i', [0] * (matrix_size * matrix_size), lock=False)
    for p in range(process_count):
        Process(target=work_out_row, args=(p, matrix_a, matrix_b, result, work_start, work_complete)).start()
    start = time.time()
    for t in range(10):
        generate_random_matrix(matrix_a)
        generate_random_matrix(matrix_b)
        for i in range(matrix_size * matrix_size):
            result[i] = 0
        work_start.wait()
        work_complete.wait()
    end = time.time()
    print("Done, time taken", end - start)
