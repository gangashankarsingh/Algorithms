import time
from math import sqrt


def checkprime(num):

    for i in range(2, int(sqrt(num)) + 1):
        if (num % i == 0):
            return False
    return True

num=3
start = int((time.time()))
while True:
    stop = int(time.time())-start
    if checkprime(num):
        if stop < 11:
            print("Prime Number is {}. Total time taken so far is {}".format(num,stop))
    num=num+1


