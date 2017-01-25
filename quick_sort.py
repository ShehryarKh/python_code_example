__author__ = 'shehryar'

def qsort(li):
    quick_sort(li,0,len(li)-1)


def quick_sort(li,least,high):
    if least < high:
        pivot = partition(li, least,high)
        quick_sort(li,least,pivot-1)
        quick_sort(li,pivot+1,high)


def get_pivot(li,least,high):
    mid = (least+high)//2
    pivot = high
    if li[least]< li[mid]:
        if li[mid] < li[high]:
            pivot = mid
    elif li[least] < li[high]:
        pivot = least
    return pivot

def partition(li, least, high):
    pivot = li[least]
    left = least+1
    right = high
    done = False

    while not done:
        while left <= right and li[least]<= pivot:
            left = left +1
        while li[right] >= pivot and right >= left:
            right = right -1

        if right < left:
            done = True

        else:
            temp = li[least]
            li[least] = li[right]
            li[right] = temp

        temp = li[least]
        li[least] = li[right]
        li[right] = temp

        return right