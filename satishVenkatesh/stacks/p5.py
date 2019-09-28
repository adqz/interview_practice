# @author: adnan
import re

class Stack():
  '''
  This class implements the classic stack data structure using python lists.
  Stacks operate on a LIFO basis (Last In First Out)
  '''
  def __init__(self, maxLimit = 100):
    self.stackArray = []
    self.maxLimit = maxLimit
    self.top = 0

  def __str__(self):
    return str(self.stackArray)

  def push(self, data):
    if self.top >= self.maxLimit:
      raise IndexError('Max limit reached')
    self.stackArray.append(data)
    self.top += 1

  def pop(self):
    if self.top == 0:
      raise IndexError('No elements to pop')
    self.top -= 1
    return self.stackArray.pop()

  def size(self):
    return len(self.stackArray)

  def peek(self):
    if self.size() != 0:
      return self.stackArray[self.size() - 1]
    return None


class Convert():
  '''
  Convert infix expressions to postfix
  '''
  def __init__(self):
    # Operator precedence dictionary
    self.precedence = {
    '^': 4,
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '(': 1,
    }

  def infixToPostfix(self, expression):
    assert isinstance(expression, str) and len(expression) > 0
    postfix = []
    operatorStack = Stack(maxLimit = len(expression))
    tokens = expression.split(' ')

    for token in tokens:
      if bool(re.match('[A-Z]', token)) or bool(re.match('\d', token)):
        postfix.append(token)
      
      elif token == '(':
        operatorStack.push(token)
      
      elif token == ')':
        while operatorStack.peek() != '(':
          postfix.append(operatorStack.pop())
        operatorStack.pop() # remove the opening round brace

      elif bool(re.match('\+|-|\*|/|\^', token)):
        if operatorStack.peek():
          precOfToken, precOfLastStackElement = self.precedence[token], self.precedence[operatorStack.peek()]
          while (precOfLastStackElement >= precOfToken): #adding operators to postfix who have higher precedence than current tokens'
            postfix.append(operatorStack.pop())
            if operatorStack.size() == 0:
              break
            precOfLastStackElement = self.precedence[operatorStack.peek()] #updating precedence of last element
        operatorStack.push(token) #adding current token to stack after removing operators of higher precedence
      else:
        raise TypeError('Unknown character')
    # All tokens have been processed now. Now if any operators are left, we pop them and append them to postfix 
    while operatorStack.peek():
      postfix.append(operatorStack.pop())

    return ' '.join(postfix)

  def postfixToInfix(self, expression):
    assert isinstance(expression, str) and len(expression) > 0

    tokens = expression.split(' ')
    operandStack = Stack(maxLimit = len(expression))

    for token in tokens:
      if bool(re.match('[A-Z]', token)) or bool(re.match('\d', token)):
        operandStack.push(token)

      elif bool(re.match('\+|-|\*|/|\^', token)):
        el1 = operandStack.pop()
        el2 = operandStack.pop()
        newOperand = ' '.join(['(', el2, token, el1, ')'])
        operandStack.push(newOperand)

    return ' '.join(operandStack.stackArray)


if __name__ == '__main__':
  c = Convert()
  expression = 'A + B * ( C + ( H - G ) D )'
  print('expression = ', expression)
  postfix = c.infixToPostfix(expression)
  print('postfix = ', postfix)
  infix = c.postfixToInfix(postfix)
  print('infix = ', infix)

  # Double checking if this infix produces the same postfix as before
  print('\n -------Double checking-------')
  print('postfix = ', c.infixToPostfix(infix))