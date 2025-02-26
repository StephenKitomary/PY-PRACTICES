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
