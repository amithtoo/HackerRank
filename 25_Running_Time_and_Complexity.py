# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt
t = int(input())
for _ in range(t):
    n = int(input())
    flag = 1
    if n in (0, 1):
        print('Not prime')
    else:
        for i in range(2, int(sqrt(n))):
            if n%i == 0:
                flag = 0
        if flag == 1:
            print('Prime')
        else:
            print('Not prime')
