import random
import time

def bubble_sort(lst):
    for i in range (len(lst) -1):
        sorted = True
        for j in range (len(lst)-1-i):
            if lst[j] > lst [j+1]:
                lst[j] , lst[j+1] = lst[j+1], lst[j]
                sorted = False
        if sorted:
            return lst




if __name__ == '__main__':

    lst = []
    for i in range(1000):
        lst.append(random.random())
    print(lst)
    starttime = time.time()
    print(bubble_sort(lst))
    print("Total time is:" , time.time()-starttime)