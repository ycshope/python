# https://leetcode-cn.com/problems/search-a-2d-matrix/


class Solution:
    #思路:直接拼接在一起然后二分查找  时间复杂度:O(logmn )
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        tlist = []
        for row in matrix:
            tlist += row

        def binary_search(tlist: list, low: int, high: int, target: int):

            if low > high:
                return False
            mid = (low + high) // 2
            if tlist[mid] == target:
                return True
            elif tlist[mid] > target:
                return binary_search(tlist, low, mid - 1, target)
            else:
                return binary_search(tlist, mid + 1, high, target)

        if (length := len(tlist)) == 0:
            return False

        return binary_search(tlist=tlist,
                             low=0,
                             high=length - 1,
                             target=target)

    #思路:二维坐标转换为一位坐标后二分
    def searchMatrix_ref(self, matrix: list[list[int]], target: int) -> bool:
        #0.计算出k
        if (rows := len(matrix)) == 0:
            return False

        try:
            cols = len(matrix[0])
        except Exception as e:
            return False

        if (length := rows * cols) == 0:
            return False

        def binary_search(matrix: list[list[int]], low: int, high: int,
                          target: int, length: int) -> bool:
            if low > high:
                return False

            #1.计算出二分查找的坐标mid
            mid = (low + high) // 2
            #2.将mid转换为x,y
            #2.1 x=k//length
            #2.2 y=k%length
            #3.二分比较
            x = mid // length
            y = mid % length
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                return binary_search(matrix, low, mid - 1, target, length)
            else:
                return binary_search(matrix, mid + 1, high, target, length)

        return binary_search(matrix=matrix,
                             low=0,
                             high=length - 1,
                             target=target,
                             length=cols)


if __name__ == "__main__":
    # matrix, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3
    # matrix, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13
    # matrix, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 1
    # matrix, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60
    # matrix, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 0
    # matrix, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 61
    # matrix, target = [[], [], []], 1
    matrix, target = [], 1
    ans = Solution()
    print(ans.searchMatrix_ref(matrix=matrix, target=target))
