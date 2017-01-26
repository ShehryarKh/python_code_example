__author__ = 'shehryar'

def square_each(array):
    s = [x**2 for x in array]
    return s


def two_list_one_dictionary(array1, array2):
    #zip Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables
    return dict(zip(array1,array2))

new_list=[]
def nested_list_to_one_list(array):

    for i in array:
        if type(i) == list:
            nested_list_to_one_list(i)
        else:
            new_list.append(i)



nested_list_to_one_list([1,[2,2,[2]],4])
print(new_list)
