#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    sum=0
    for i in range(len(bill)):
        sum+=bill[i]
    amt=int((sum-bill[k])/2)

    c=b-amt
    if(b==amt):
        print('Bon Appetit')
    else:
        print(c)
if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
