import numpy as np
from matplotlib import pyplot as plt


def collatz_conjecture(n):
    sequence = [n]

    while n != 1:
        if n % 2:
            n = (3 * n) + 1
        else:
            n = n // 2
        sequence.append(n)

    return sequence


def main():
    n = int(input("Input value to plot graph: "))
    sequence = collatz_conjecture(n)
    x = np.arange(len(sequence))

    fig = plt.figure('Collatz Conjecture')
    plt.plot(x, sequence, 'k*-')
    plt.xlabel('Step')
    plt.ylabel('Value')
    plt.title(f'Collatz Conjecture for {n}')
    plt.grid(True)
    plt.show()
    pass


if __name__ == '__main__':
    main()
