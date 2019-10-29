# author: adnan
# date: 29-Oct-2019
import pytest

def reverse(s):
  ''' 
  Reverse a given string
  :param s: string to reverse
  :type s: str
  '''
  assert isinstance(s, str)

  arr = [c for c in s] #convert from str to array
  rev = ''.join(arr[::-1]) #reverse array and convert back to string

  return rev

if __name__ == '__main__':
  print(reverse('abcd'))