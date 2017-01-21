__author__ = 'shehryar'


'''
This function takes in a list and
flips it based on its largest index/value once found.
It returns a list that has been flipped.
'''

def psort(li):
    # ISSUE HERE WAS HAD TO WORK BACKWORD
    # STARTING FROM 0 WILL ALWAYS RETURN
    # AN OUT OF INDEX ERROR
    for i in reversed(range(len(li))):
        idx = find_largest_index(li ,i)
        li = flip(li, idx)
        li = flip(li, i)

    return li

'''
This takes in the index
and finds the largest value based of
the position of the index. It compares
what index it has and searched up until the index
to determine if larger value is found if so return it
'''
def find_largest_index(li , idx):
    largest = li[idx]
    largest_index = idx
    for i in range(idx):
        if li[i] > largest:
            largest = li[i]
            largest_index = i
    return largest_index

'''
The flip method takes a list
and its index and flips it based on the position
of the index. It gets the elements of everything
after a position and then reverses it.
'''

def flip(li, idx):
    # ISSUE HERE WAS PREVIOUSLY I WAS OVERRIDING LI
    x = li[:(idx + 1)]
    x.reverse()
    x += li[(idx+1):]
    return x

li = [0,5,2,6,7,3,7,8,2]



print(psort(li))