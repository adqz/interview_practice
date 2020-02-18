# @author: adnan
# Problem 2. Add Two Numbers

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return str(self.val) +'->'+ str(self.next)

class Solution(object):
    def addTwoNumbers(self, l1, l2, carry = 0):
        value = l1.val + l2.val + carry
        carry = value // 10
        newNode = ListNode(value%10)

        if (l1.next != None or l2.next != None or carry!=0):
            if not(l1.next):
                l1.next = ListNode(0)
            if not(l2.next):
                l2.next = ListNode(0)
            newNode.next = self.addTwoNumbers(l1.next, l2.next, carry)

        return newNode


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print(l1)
print(l2)

s = Solution()
s.addTwoNumbers(l1,l2)

'''
Solution 1

def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while (l1 or l2):
            if not(l1.val): l1.val=0
            if not(l2.val): l2.val=0
            temp = (l1.val + l2.val)
            value = (temp%10) + carry
            carry = temp//10
            assert isinstance(carry, int)
            curr.next = ListNode(value)
            curr, l1, l2 = curr.next, l1.next, l2.next

        if carry>0:
            curr.next = ListNode(carry)
        print(dummy.next)
        return dummy.next
'''