#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    modified = []
    for ch in s:
        if not modified:
            modified.append(ch)
        else:
            c = modified[-1]
            if ch != c:
                modified.append(ch)
    return len(s) - len(modified)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()