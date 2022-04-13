#https://leetcode-cn.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #思路:归并排序
        #边界情况1:nums2为空
        if len(nums2) == 0:
            return None

        i = 0
        j = 0
        midarr = []
        while i < m and j < n:
            #较小的作为元素
            if nums1[i] < nums2[j]:
                midarr.append(nums1[i])
                i += 1
            else:
                midarr.append(nums2[j])
                j += 1

        #如果nums1先遍历完,nums2后面的添加进去;否则
        if i == m:
            midarr += nums2[j:]
        else:
            midarr += nums1[i:m]

        #注意nums1=midarr函数结束后由于midarr被释放,结果依旧不变
        nums1[:] = midarr


if __name__ == "__main__":
    # nums1, m, nums2, n = [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3
    # nums1, m, nums2, n = [1], 1, [], 0
    nums1, m, nums2, n = [0], 0, [1], 1
    s = Solution()
    s.merge(nums1, m, nums2, n)
    print(nums1)
