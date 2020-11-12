class Solution():
    def romanToInt(self, s: str):
        romanint_dit = {"I": 1, "V": 5, "X": 10,
                        "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        # 特殊处理
        prenum = 1001
        for i, ch in enumerate(s):
            curnum = romanint_dit.get(ch)
            # 如果ch得出来的值大于prenum,那么sum + = curnum-preint*2
            # 如果其他情况:sum + = curnum
            sum += curnum if curnum <= prenum else curnum - (prenum << 1)
            prenum = curnum
        return sum


if __name__ == "__main__":

    Q = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
    s = Solution()
    for q in Q:
        print(s.romanToInt(q))
