#https://leetcode-cn.com/problems/brick-wall
class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        # 性能问题hash = [0] * 500000000
        # [[100000000,100000000],[100000000,100000000]]
        hash = {}
        length = len(wall)
        for row in wall:
            sum = 0
            #生成hash[sum]
            for i in row:
                strsum = f"{sum}"
                key = (hash.get(strsum) or 0) + 1
                hash[strsum] = key
                sum += i

        maxline = 0
        for key in hash.keys():
            if key != "0":
                maxline = max(hash[key], maxline)

        ans = length - maxline
        print(hash)
        return ans

    def leastBricks2(self, wall: list[list[int]]) -> int:
        gaps = {}
        for w in wall:  # 遍历每一层
            gap = 0
            for i in range(len(w) - 1):  # 不考虑最后一块砖，因为不能贴着边缘画线
                gap += w[i]
                if gap in gaps:
                    gaps[gap] += 1
                else:
                    gaps[gap] = 1

        #直接为空
        if gaps:  # 不为空
            # dict取出全部值
            return len(wall) - max(gaps.values())
        else:  # 为空说明每一层都只有一块砖
            return len(wall)


if __name__ == "__main__":
    wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2],
            [1, 3, 1, 1]]

    #边界条件
    # wall = [[1], [1], [1]]
    s = Solution()
    ans = s.leastBricks(wall)
    print(ans)
