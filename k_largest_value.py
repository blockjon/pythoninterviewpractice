"""
Select Kth largest value in the array.
Given an unsorted array of size n, and a value k.
Select the kth largest value from the array.
"""

if __name__ == "__main__":
    k = 3
    numbers = [7, 25, 4, 13, 88, 55, 41, 2]
    numbers.sort()
    print numbers[k-1]
