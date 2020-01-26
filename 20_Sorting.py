#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numSwaps = 0
for i in range(0, len(a)):
    swaps = 0
    for j in range(0, len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numSwaps += 1
            swaps += 1
    if swaps == 0:
        break
print('Array is sorted in', numSwaps, 'swaps.')
print('First Element:', a[0])
print('Last Element:', a[n-1])

