"""Begin by loading Numbers.txt into a list.This file contains 100 integers between 0 and 1000D
efine the function load_numbers(filename), where filename is a formal parameter that is a string, containing the name of the file you want to load.
You should return a list that contains the (unsorted) numbers in filename as a list."""

def load_numbers(filename):
    with open(filename) as file:
        numbers = file.readlines()
    return [int(number) for number in numbers]

def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort(load_numbers("Numbers.txt")))
