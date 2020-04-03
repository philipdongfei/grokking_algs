#!/bin/python3
from functools import reduce


if __name__ == '__main__':
    arr1 = [1,2,3,4,5]
    arr2 = map(lambda x: 2 * x, arr1)
    print(arr1)
    for i in arr2:
        print(i,end=' ')
    print()
    value = reduce(lambda x,y: x+y, arr1)
    print(value)

