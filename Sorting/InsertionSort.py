import random
import time


def insertion_sort(lst):
    for i in range (1,len(lst)):
        j = i-1
        while j >= 0 and lst[j] > lst [i]:
            j += -1

        temp = lst[i]
        lst[j+2:i+1] = lst[j+1:i]
        lst[j+1] = temp

    return lst


if __name__ == '__main__':

    lst = []
    for i in range(10):
        lst.append(random.random())
    print(lst)
    starttime = time.time()
    print(insertion_sort(lst))
    print("Total time is:", time.time()-starttime)