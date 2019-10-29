# author: adnan
# date: 29-Oct-2019

def reverseInt(number):
  '''
  Given an integer, return an integer that is the reverse
  ordering of numbers.
  :param n: integer to reverse
  :type n: int

  Examples
  >>> reverseInt(15) === 51
  >>> reverseInt(981) === 189
  >>> reverseInt(500) === 5
  >>> reverseInt(-15) === -51
  >>> reverseInt(-90) === -9
  '''
  assert isinstance(number ,int)
  sign = 1 if number>0 else -1
  arr = [n for n in str(abs(number))] #remove sign convert to string
  rev = sign * int(''.join(arr[::-1])) #reverse the str, join it, convert to int, and then multiply with sign
  return rev

if __name__ == '__main__':
  print(reverseInt(-377))