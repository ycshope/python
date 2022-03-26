# https://leetcode-cn.com/problems/design-circular-deque/
from operator import index


class MyCircularDeque:
    def __init__(self, k: int):
        self.queue = []
        self.maxsize = k
        self.size = 0
        return None

    def __str__(self):
        return str(self.queue)

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue = [value] + self.queue
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue.append(value)
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.queue.pop(0)
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.queue.pop()
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[-1]

    def isEmpty(self) -> bool:
        if self.size:
            return False
        return True

    def isFull(self) -> bool:
        if self.size == self.maxsize:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

if __name__ == "__main__":
    # obj = MyCircularDeque(3)
    # print(obj.insertLast(1))
    # print(obj)

    # print(obj.insertLast(2))
    # print(obj)

    # print(obj.insertFront(3))
    # print(obj)

    # print(obj.insertFront(4))
    # print(obj)

    # print(obj.getRear())
    # print(obj)

    # print(obj.isFull())
    # print(obj)

    # print(obj.deleteLast())
    # print(obj)

    # print(obj.insertFront(4))
    # print(obj)

    # print(obj.getFront())
    # print(obj)

    obj = MyCircularDeque(8)
    print(obj.insertFront(5))
    print(obj)

    print(obj.getFront())
    print(obj)

    print(obj.isEmpty())
    print(obj)

    print(obj.deleteFront())
    print(obj)

    print(obj.insertLast(3))
    print(obj)
    
    print(obj.getRear())
    print(obj)

    print(obj.insertLast(7))
    print(obj)

    print(obj.insertFront(7))
    print(obj)

    print(obj.deleteLast())
    print(obj)

    print(obj.insertLast(4))
    print(obj)

    print(obj.isEmpty())
    print(obj)
