__author__ = 'shehryar'

'''
Given an array find the largest product
using 3 numbers

This is not the optimal solution. Optimal solution below

'''

def three_product(array):
    if(len(array)>3):
        max1 = max(array)
        min1 = min(array)
        array.remove(max1)
        array.remove(min1)

        max2 = max(array)
        min2 = min(array)
        array.remove(max2)
        array.remove(min2)
        max3 = max(array)


        if min1*min2*max1 > max1*max2*max3:
            return min1*min2*max1
        else:
            return max1*max2*max3
    else:
        return array[0]*array[1]*array[2]


'''
Optimal Solution:
sort the array(quick sort)
index the positions to find the products
'''