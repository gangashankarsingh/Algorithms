import time
import random


def merge_sort(arr):

    if len(arr) > 1:
        middle = len(arr)//2
        sortedleft = (arr[:middle])
        sortedright = (arr[middle:])
        sortedleft=merge_sort(sortedleft)
        sortedright= merge_sort(sortedright)
        s_arr=[]
        x = y = 0
        while x < len(sortedleft) and y < len(sortedright):
            if sortedleft[x]<sortedright[y]:
                s_arr.append(sortedleft[x])
                x += 1
            else:
                s_arr.append(sortedright[y])
                y += 1

        while x < len(sortedleft):
            s_arr.append(sortedleft[x])
            x += 1

        while y < len(sortedright):
            s_arr.append(sortedright[y])
            y += 1

        return s_arr
    else:
        return arr


if __name__ == '__main__':
    lst = []
    for i in range(1000):
        lst.append(random.random())
    print(lst)
    starttime = time.time()
    print(merge_sort(lst))
    print("Total time is:", time.time()-starttime)




