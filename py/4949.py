# 4949번: 균형잡힌 세상
def isYes(compare: bool):
  return 'yes' if compare else 'no'

while True:
  sentence = input()
  stack = []
  openParenthesis = True

  if sentence == '.':
    break

  for character in list(sentence):
    if character == '(' or character == '[':
      stack.append(character)
    elif character == ')':
      if len(stack) > 0 and stack[len(stack)-1] == '(':
        stack.pop()
      else:
        openParenthesis = False
        break
    elif character == ']':
      if len(stack) > 0 and stack[len(stack)-1] == '[':
        stack.pop()
      else:
        openParenthesis = False
        break
  
  print(isYes(len(stack) == 0 and openParenthesis))