def isYes(compare: bool):
  return 'YES' if compare else 'NO'

t = int(input())

for index in range (0, t):
  parenthesisString = input()
  isValidParenthesisString = True
  stack = []

  for parenthesis in list(parenthesisString):
    if parenthesis == '(' :
      stack.append(parenthesis)
    elif parenthesis == ')':
      if len(stack) > 0 and stack[len(stack)-1] == '(':
        stack.pop()
      else:
        isValidParenthesisString = False
        break
  
  if len(stack) > 0:
    isValidParenthesisString = False

  print(isYes(isValidParenthesisString))