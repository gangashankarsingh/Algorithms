import random
import time


def selection_sort(lst):
    for i in range (len(lst)-1):
        max_location = 0
        for j in range (1, len(lst)-i):
            if lst[j] > lst [max_location]:
                max_location = j
        if max_location == len(lst)-1-i:
            pass
        else:
            lst[max_location], lst[len(lst)-i-1] = lst[len(lst)-i-1], lst[max_location]
    return lst




if __name__ == '__main__':

    lst = []
    for i in range(1000):
        lst.append(random.random())
    print(lst)
    starttime = time.time()
    print(selection_sort(lst))
    print("Total time is:" , time.time()-starttime)