'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    #往self后面添加一个节点x
    def Append(self, x):
        #如果是最后一个元素,那么新建节点,
        if self.next == None :
            self.next = ListNode(val=x)
        else: #否则去下一个节点添加元素x
            self.next.Append(x)
    
    def __str__(self):
        buff = []
        while self != None :
            if self.val != None:
                buff.append(self.val)
            self = self.next
        return str(buff)
                  
class Solution:
    head = ListNode(val=None)
    #合并两个链表并返回
    def mergeTwoLists(self, l1, l2):
        #如果其中一个链表为空,返回另一个链表
         if l1 == None :
            return l2
         if l2 == None :
            return l1
            
         if l1.val < l2.val :
            self.next = self.mergeTwoLists(l1.next, l2)
            return l1
         else :
            self.next = self.mergeTwoLists(l1, l2.next)
            return l2
    
    def __init__(self, l1 ,l2):
        
        
                       
if __name__ == "__main__":

    l1 ,l2 = [1,2,4], [1,3,4]
    
    head1 = ListNode(val=None)
    head2 = ListNode(val=None)
    
    for val in l1:
        head1.Append(val)
    
    for val in l2:
        head2.Append(val)
        
    print(head1)
    print(head2)
    
    print("Solution:")
    

        
        