__author__ = 'shehryar'



def balanced(str):
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
  return True

eq = '{{]]}'
print(balanced(eq))