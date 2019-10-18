import random
import time

def quicksort(lst):
    if len(lst) > 1:
        pivotindex = len(lst)-1
        leftpointer = 0

        while not (pivotindex == leftpointer):
            if lst[leftpointer] > lst[pivotindex]:
                value = lst[leftpointer]
                lst[leftpointer], lst[pivotindex-1]=lst[pivotindex-1],lst[leftpointer]
                lst[pivotindex - 1], lst[pivotindex]=lst[pivotindex],lst[pivotindex-1]
                pivotindex = pivotindex-1
            else:
                leftpointer = leftpointer+1

        lst[:pivotindex] = quicksort(lst[:pivotindex])
        lst[pivotindex+1:] = quicksort(lst[pivotindex+1:])
    else:
        return lst
    return lst



if __name__ == '__main__':
    lst = []
    for i in range(1000):
        lst.append(random.random())
    print(lst)
    starttime = time.time()
    print(quicksort(lst))
    print("Total time is:", time.time()-starttime)