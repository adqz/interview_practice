import pytest
from index import *

class TestClass():

  def test_one(self):
    assert len(reverseInt.__doc__)
  def test_two(self):
    assert reverseInt(0) == 0
  def test_three(self):
    assert reverseInt(5) == 5
  def test_four(self):
    assert reverseInt(15) == 51
  def test_five(self):
    assert reverseInt(90) == 9
  def test_six(self):
    assert reverseInt(2359) == 9532
  def test_seven(self):
    assert reverseInt(-5) == -5
  def test_eight(self):
    assert reverseInt(-90) == -9
  def test_nine(self):
    assert reverseInt(-15) == -51
  def test_ten(self):
    assert reverseInt(-2539) == -9352
    
    