__author__ = 'shehryar'



def check_balanced_string(str):
  li = []
  braces = {'(': ')', '[': ']', '{': '}'}


  for i in str:
    if i in braces.keys():
      li.append(i)

    elif i in braces.values():
      if braces[li[-1]] == i:
        li.pop()
      else:
        return False
  return not len(li)

eq = '{1+[3*5+(2+1)]}'
print(check_balanced_string(eq))