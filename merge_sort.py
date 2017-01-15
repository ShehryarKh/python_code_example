__author__ = 'shehryar'

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result += left[i:]
    result += right[j:]
    return result

def mergesort(mylist):
    if len(mylist) == 1:
        return list
    middle = len(mylist)//2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    return merge(left,right)

print(mergesort([1,4,5,123,1,54]))