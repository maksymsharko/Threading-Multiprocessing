# Task 4
"""
Divide the work between 2 methods: print_cube that returns the cube of number
and print_square that returns the square of number. These two methods
should be executed by using 2 different processes.
"""
from concurrent.futures import ProcessPoolExecutor
import time
import os
import random
from multiprocessing import Process


def print_cube(num1):
    id_name = os.getpid()
    start = time.time()
    print(f'Process: {id_name}')
    return print(f"The {num1} is elevated to the cube is equal to {num1} = {num1 ** 3} and this process continued "
                 f"{time.time() - start}")


def print_square(num2):
    id_name2 = os.getpid()
    start = time.time()
    print(f"Process: {id_name2}")
    return print(f"The {num2} is elevated to square is equal to {num2} = {num2 ** 2} and this process continued "
                 f"{time.time() - start}")


if __name__ == "__main__":
    start = time.time()

    with ProcessPoolExecutor(max_workers=2) as pool:
        pool.submit(print_cube)
        pool.submit(print_square)

        p1 = Process(target=print_cube, args=(random.randint(1, 9), ))
        p2 = Process(target=print_square, args=(random.randint(1, 9), ))
        p1.start()
        p2.start()


    print(f"Total time: {time.time() - start} ")
