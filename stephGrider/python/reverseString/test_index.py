import pytest
from index import *

class TestClass():

  def test_one(self):
    assert reverse('abcd') == 'dcba'
  def test_two(self):
    assert reverse('  abcd') == 'dcba  '
    