import time
import numpy as np


def loop():
    """
    Finding the sum of numbers using loops
    """

    start = time.time()
    total = 0
    for item in range(0, 1500000):
        total = total + item

    print('sum is:' + str(total))
    end = time.time()
    print(end - start)

def vectorization():
    """
    Finding the sum of numbers using vectorization
    """

    start = time.time()
    sequence = np.arange(1500000)
    sum_sequence = np.sum(sequence)
    end = time.time()
    print(end-start)