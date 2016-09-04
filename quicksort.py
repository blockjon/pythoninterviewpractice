"""
Implement quick sort

Input:
[2, 1, 5, 3]

Output:
[1, 2, 3, 5]
"""


def quicksort(input):
    if len(input) < 2:
        return input
    pivot = 0
    leftmark = 1
    rightmark = len(input) - 1
    continue_scanning = True
    while continue_scanning:
        while input[leftmark] < input[pivot] and leftmark+1 != len(input):
            leftmark += 1
        while input[rightmark] > input[pivot]:
            rightmark -= 1
        if rightmark <= leftmark:
            # Swap pivot and right most value.
            input[pivot], input[rightmark] = (input[rightmark], input[pivot])
            pivot = rightmark
            continue_scanning = False
        else:
            # Exchange values
            input[leftmark], input[rightmark] = (input[rightmark], input[leftmark])
    return quicksort(input[:pivot]) + [input[pivot]] + quicksort(input[pivot+1:])

if __name__ == "__main__":
    print quicksort([2, 1, 5, 3])
