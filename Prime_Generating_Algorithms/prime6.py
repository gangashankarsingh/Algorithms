import time
from math import sqrt







def checkprime(num):

    if num>6 and (num%6 in [0,2,3,4]):
        return False

    if num==2:
        return True
    if num%2 == 0:
        return False
    for i in range(3, int(sqrt(num)) + 1,2):
        if (num % i == 0):
            return False
    return True

num=2
start = int((time.time()))
while True:
    stop = int(time.time())-start
    if checkprime(num):
        if stop < 11:
            print("Prime Number is {}. Total time taken so far is {}".format(num,stop))
    num=num+1

