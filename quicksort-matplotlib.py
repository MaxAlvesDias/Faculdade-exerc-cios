import matplotlib.pyplot as plt
import numpy as np
import time

def quicksort(v, low, high):
    if low < high:
        pi = partition(v, low, high)

        quicksort(v, low, pi - 1)
        quicksort(v, pi + 1, high)

def partition(v, low, high):
    pivot = v[high]
    i = low - 1

    for j in range(low, high):
        if v[j] < pivot:
            i += 1
            v[i], v[j] = v[j], v[i]
            plot_bar(v)
            plt.pause(0.05)

    v[i + 1], v[high] = v[high], v[i + 1]
    plot_bar(v)
    plt.pause(0.05)
    return i + 1

def plot_bar(v):
    plt.clf()
    plt.bar(range(len(v)), v, color='skyblue')
    plt.title("Quicksort")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.draw()
    plt.pause(0.01)

def main():
    v = [3,8,6,7,10, 0, 1]
    print("Original vay:", v)
    
    plt.ion()
    plt.figure()
    plot_bar(v)
    
    quicksort(v, 0, len(v) - 1)
    
    plt.ioff()
    plt.show()
    print("Sorted vay:", v)

if __name__ == "__main__":
    main()
