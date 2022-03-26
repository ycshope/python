# https://leetcode-cn.com/problems/my-calendar-i/solution/wo-de-ri-cheng-an-pai-biao-i-by-leetcode/
#NOTE:解法2.平衡树
class MyCalendar:
    def __init__(self):
        self.booked_list = []

    def book(self, start: int, end: int) -> bool:
        #仅有两种情况没有交集:
        #s1:表示原来的集合,s2:表示现在的集合
        for booked in self.booked_list:
            s1, e1 = booked[0], booked[1]
            # e2<=s1 s2>=e1
            if not end <= s1 and not start >= e1:
                # print(f"交集为:{booked}")
                return False
        # e2<s1 s2>e1
        # 1.判断是否有交集
        # 2.添加新的集合
        self.booked_list.append([start, end])
        # print(f"new set={self.booked_list}")
        return True

#NOTE:与其思考复杂的交集情况不如思考一下对立情况,无交集的情况比较简单

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
if __name__ == "__main__":
    myCalendar = MyCalendar()
    myCalendar.book(10, 20)
    # return True
    myCalendar.book(15, 25)
    # return False ，这个日程安排不能添加到日历中，因为时间 15 已经被另一个日程安排预订了。
    myCalendar.book(20, 30)
    # return True ，这个日程安排可以添加到日历中，因为第一个日程安排预订的每个时间都小于 20 ，且不包含时间 20 。
