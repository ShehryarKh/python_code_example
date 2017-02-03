def roman_numeral_from_string(string):
    """
    Converts the roman numeral string into an integer
    :param string: Roman numeral as a string
    :returns int: integer value of string or None if failed to convert
    """


    # WHY DOESNT IT TELL ME WHICH BUG I HAVE ONCE THE TESTS PASS
    #Notes
    '''
    Im not sure what bug its reffering too. Checking Logic. If the next value on the string is bigger than current one,
    I subtract that value, and I add if its not. So Something like 'CDM' would return -100+-500+100 = 400.
    '''
    nums = {'M':1000, 'D':5000, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

    sum = 0

    if not type(string):
      return None

    for i in range(len(string)):
      #Find the value of the letter in the string looking at the dictionary
      #we want to add to the sum its value/ but subtract its value ...
      # if the next value in the string is higher then the current value
        try:
          value = nums[string[i]]
          # I check if i+1 can be indexed in the string, and then check its value, if its grreater than
          # current value, i have to subtract it
          if i+1 < len(string) and nums[string[i+1]] > value:
            sum -= value
          else:
            # if its not I add to the sum
            sum += value

        except KeyError:
            return None

    return sum



