import stack

def revstring(string):
  rev_stack = stack.Stack()
  rev_string = ''
  for char in string:
    rev_stack.push(char)
  while not rev_stack.isEmpty():
    rev_string = rev_string + rev_stack.pop()
  return rev_string
