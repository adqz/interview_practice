# @author: adnan
class Node():
	'''
	This class implements the Node data structure with two attributes:

	1. data - this stores the data in the node
	2. next - this stores the address to the next node it is linked to

	'''
	def __init__(self, data):
		self.data = data
		self.next = None

	def __str__(self):
		return str(self.data)

class Stack():
	def __init__(self):
		self.root = None

	def __str__(self):
		if self.isempty():
			return 'Stack: ' + str([])
		stackString = ''
		nodeToPrint = self.root
		while nodeToPrint != None:
			stackString += ' >- ' + str(nodeToPrint.data)
			nodeToPrint = nodeToPrint.next
		return 'Stack: ' + stackString[::-1][0:-4] #[::-1] reverses the string and [0:-4] removes the last arrow

	def isempty(self):
		return True if self.root == None else False

	def push(self, data):
		newNode = Node(data)
		newNode.next = self.root
		self.root = newNode

	def pop(self):
		if self.isempty():
			return ('Empty stack. Cant pop')

		nodeToPop = self.root
		self.root = self.root.next
		return nodeToPop.data

	def size(self):
		stackSize = 0
		if self.isempty():
			return stackSize
		
		node = self.root
		while node != None:
			stackSize += 1
			node = node.next

		return stackSize

if __name__ == '__main__':
  s = Stack()
  s.push(4)
  s.push(7)
  s.push(9)
  print(s)
  print('size = ', s.size())
  print(s.pop())
  print(s.pop())
  print(s.pop())
  print(s.pop())
  print(s)
  print('size = ', s.size())