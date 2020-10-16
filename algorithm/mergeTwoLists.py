'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

?

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
?

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
            buff.append(self.val)
            self = self.next
        return str(buff)
'''
    复习点:1.递归的思维,特别注意返回值
            2.__str__
            3.参数类型的声明
'''                  
class Solution: 
    #直接show
    def __str__(self:ListNode):
        buff = []
        while self != None :
            buff.append(self.val)
            self = self.next
        return str(buff)
    
    #定义:排序以l1,l2开头的链表
    def mergeTwoLists(self, l1:ListNode, l2:ListNode) ->ListNode: #声明参数类型和返回值的类型
        #如果其中一个链表为空,返回另一个链表
         if l1 == None :
            return l2
         if l2 == None :
            return l1
         #结点为比较小的那个结点   
         if l1.val < l2.val :
            l1.next = self.mergeTwoLists(l1.next, l2) #self.next不会被保存
            return l1
         else :
            l2.next = self.mergeTwoLists(l1, l2.next)#  self.next不会被保存
            return l2
    
    #解法2
    def mergeTwoLists_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val: l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
    '''
    备注： 在 Python 中，and 和 or 都有提前截至运算的功能。
            and：如果 and 前面的表达式已经为 False，那么 and 之后的表达式将被 跳过，返回左表达式结果
            or：如果 or 前面的表达式已经为 True，那么 or 之后的表达式将被跳过，直接返回左表达式的结果
            例子：[] and 7 等于 []
    '''
if __name__ == "__main__":

    l1 ,l2 = [1,2,4], [1,3,4]
    #l1 ,l2 = [],[0]
    
    #建立两个头结点
    head1 = ListNode(val=None)
    head2 = ListNode(val=None)
    head = ListNode(val=None)
    #生成两个链表
    for val in l1:
        head1.Append(val)
    
    for val in l2:
        head2.Append(val)
    '''打印链表    
    print(head1)
    print(head2)
    '''
    print("Solution:")
    s = Solution()
    head = s.mergeTwoLists(head1.next,head2.next)
    print(head) 