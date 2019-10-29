# author: adnan
# date: 29-Oct-2019
def fizzBuzz(n):
  '''
  Classis fizzBuzz problem
  :param n: number
  :type n: int
  '''
  for i in range(1,n+1):
    if (i%3==0 and i%5==0):
      print('fizzbuzz')
    elif (i%3==0):
      print('fizz')
    elif (i%5==0):
      print('buzz')

if __name__ == '__main__':
  fizzBuzz(15)