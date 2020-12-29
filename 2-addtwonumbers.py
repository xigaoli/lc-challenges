# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #
        rsltlistHead = ListNode(0,None)
        rsltlist = rsltlistHead
        CF = 0
        while True:
            addnum=0
            if(l1 is None and l2 is None):
                #all depleted,end
                if(CF == 1):
                    rsltlist.next = ListNode(1,None)
                break
            if(l1 is None):
                digit1=0
            else:
                digit1=l1.val
            if(l2 is None):
                #add end, depleted nums, set to 0
                digit2=0
            else:
                digit2=l2.val
            addnum = digit1+digit2+CF
            CF=addnum//10    #cf
            rsltlist.next = ListNode(addnum%10,None)
            if(l1 is not None):
                l1 = l1.next
            if(l2 is not None):
                l2 = l2.next
            rsltlist = rsltlist.next
            
        return rsltlistHead.next
                
            
            
        