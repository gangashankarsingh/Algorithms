import time
from math import sqrt

prime_list = [2]

def checkprime(num):

    for i in prime_list:
        if (num % i == 0):
            return False
    prime_list.append(num)
    return True

num=3
start = int((time.time()))
while True:
    stop = int(time.time())-start
    if checkprime(num):
        if stop < 11:
            print("Prime Number is {}. Total time taken so far is {}".format(num,stop))
    num=num+1
