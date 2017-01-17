__author__ = 'shehryar'

def bubble_sort(li):
    for i in range(len(li)):
        for j in range(len(li)-1 -i):
            if li[j] > li[j+1]:
                temp = li[j]
                li[j] = li[j+1]
                li[j+1] = temp
    print(li)


bubble_sort([2,5,1,5,00,435])