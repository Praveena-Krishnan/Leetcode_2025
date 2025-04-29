"""
Compares two triplets of integers and determines the scores for each based on the comparison.

The function takes two lists of integers, `a` and `b`, each containing three elements. 
For each corresponding element in the lists:
- If the element in `a` is greater than the element in `b`, `a` earns 1 point.
- If the element in `b` is greater than the element in `a`, `b` earns 1 point.
- If the elements are equal, no points are awarded.

The function returns a list containing two integers:
- The first integer is the total score for `a`.
- The second integer is the total score for `b`.

This problem is based on the "Compare the Triplets" challenge from HackerRank.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    bob_c=0
    alice_c=0
    for i in range (len(a)):
            if a[i]<b[i]:
                bob_c+=1
            elif a[i]>b[i]:
                alice_c+=1
    return alice_c,bob_c
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
