'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        nodelist = []
        while self is not None:
            nodelist.append(self.val)
            self = self.next
        return str(nodelist)

def create_listnode(raw_list, i=0):
    if i >= len(raw_list):
        return None
    node = ListNode(val = raw_list[i])
    node.next = create_listnode(raw_list, i+1)
    return node
'''    
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
    #方法1.
        1.把l1,l2转换成数字int1,int2
        2.sum = int1+int2
        3.把sum反向转换为ListNode
        时间复杂度:len(l1)+len(l2)+len(sum)
    #方法2.
        直接相加两个list,主要须考虑进位问题
'''
#方法1
class Solution:
     #类型转换
    def to_int(self, l:ListNode):
        sum = 0
        i = 0 #定义位数
       # for i,node in enumerate(l):    非标准类型无法用enumerate?
        while l is not None:
            sum += l.val*10**i
            #print(f"sum={sum}")
            l = l.next
            i += 1
        return sum
        
    def to_reverse_ListNode(self, num:int):
        head = ListNode(val=None)
        tail = head
        #边界值num=0会直接返回空头
        if num == 0:
            head.next = ListNode()
        #tail每次指向尾结点
        #case1.空结点时,head=tail,
        #case2.非空结点时,tail.next=newnode;tail=newnode
        #综合而言,引入head节点,head.val=None,tail=head
        #无论对于case1,case2都是tail.next=newnode;tail=newnode
        while num != 0:
            val = num%10
            num //= 10
            node = ListNode(val)
            tail.next = node
            tail = node
        return head.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        int1 = self.to_int(l1)
        int2 = self.to_int(l2)
        #print(f"int1={int1},int2={int2}")
        sum = int1 + int2
        #print(f"sum={sum}")
        #print(f"reverse_listnode={self.to_reverse_ListNode(sum)}")
        return self.to_reverse_ListNode(sum)
        
    
if __name__ == "__main__":
    l1 ,l2 = [2,4,3], [5,6,4]
    head1 = create_listnode(l1)
    head2 = create_listnode(l2)
    print(f"head1={head1}")
    print(f"head2={head2}")
    s = Solution()
    print(s.addTwoNumbers(l1=head1 , l2=head2))