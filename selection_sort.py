__author__ = 'shehryar'

def selection_sort(li):
    for i in range(0,len(li)):
        least = i
        for j in range(i+1, len(li)):
            if li[j] < li[least]:
                least = j
        if least != i:
            li[i],li[least] = li[least],li[i]

    print(li)

selection_sort([3,5,132,2,134,6])