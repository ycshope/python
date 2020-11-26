'''
    思路:
    1.对于__init__应该可以直接输出
    2.对于updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int)
        吧从row到int的直接边遍历边覆盖即可
'''


class SubrectangleQueries:
    def __init__(self, rectangle):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int):
        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                self.rectangle[row][col] = newValue

    def getValue(self, row: int, col: int):
        return self.rectangle[row][col]


'''
优化解法:
解题思路
1.题目中需要满足更新与获取值得操作
2.更新过程：
如果数据比较少可以直接在原始数据之上通过循环修改
如果数据量比较大会很耗时，性能低下
很容易想到用空间换时间的想法，通过将操作的过程维护在一个数组里面记录成日志
3.获取过程，通过逆序比对更新操作，看是否在范围内，
如果全部都不在，那么直接返回原始结果值
如果在，直接返回当前的更新值break

'''


class SubrectangleQueries_plus:

    def __init__(self, rectangle: List[List[int]]):
        self.data = rectangle
        self.update = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.update.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        res = None
        for i in range(len(self.update)-1, -1, -1):
            row1, col1, row2, col2, val = self.update[i]
            if row1 <= row <= row2 and col1 <= col <= col2:
                res = val
                break

        return res if res else self.data[row][col]


if __name__ == "__main__":
    tmp = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
    print(tmp.getValue(row=0, col=2))
    tmp.updateSubrectangle(row1=0, col1=0, row2=3, col2=2, newValue=5)
    print(tmp.getValue(row=0, col=2))
    print(tmp.getValue(row=3, col=1))
    tmp.updateSubrectangle(row1=3, col1=0, row2=3, col2=2, newValue=10)
    print(tmp.rectangle)
    print(tmp.getValue(row=3, col=1))
    print(tmp.getValue(row=0, col=2))
