__author__ = 'shehryar'

def square_each(array):
    s = [x**2 for x in array]
    return s


def two_list_one_dictionary(array1, array2):
    #zip Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables
    return dict(zip(array1,array2))

