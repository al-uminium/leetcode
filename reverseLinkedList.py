class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution: 
    def reverseList(self, head):
        prevNode = None
        currNode = head
        while currNode:
            nextNode = currNode.next #save next node before changing it. on last iteration, currNode.next will be None, and will break while loop
            currNode.next = prevNode #point to previous node
            prevNode = currNode #save state for next iteration
            currNode = nextNode #move to next node. will be None on last iteration, but state is saved in prevNode
        head = prevNode
        return head

            