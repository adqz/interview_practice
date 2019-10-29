import pytest
import sys
from index import *

class TestClass():

  def test_one(self):
    assert len(fizzBuzz.__doc__)
  
  def test_two(self, capsys): #The capsys and capfd fixtures allow to access stdout/stderr output created during test execution
    fizzBuzz(15)
    out, _ = capsys.readouterr()
    lines = out.split('\n')
    assert lines[0] == 'fizz'
    assert lines[2] == 'fizz'
    assert lines[3] == 'fizz'
    assert lines[5] == 'fizz'
    assert lines[1] == 'buzz'
    assert lines[4] == 'buzz'
    assert lines[6] == 'fizzbuzz'
    
  # def test_three(self):
    
  # def test_four(self):
    
  # def test_five(self):
    
  # def test_six(self):
    
  # def test_seven(self):
    