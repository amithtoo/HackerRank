#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    nbin = bin(n)
    nstr = nbin[2:]
    for i in range(len(nstr), -1, -1):
        temp = '1'*i
        if temp in nstr:
            seq = len(temp)
            break
    print(seq)

        
