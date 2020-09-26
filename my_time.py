'''
时间的类型:
    1.系统时间-时间戳
    2.开发者-时间结构体
    3.可视化-字符串时间
'''
import time
import calendar
#系统时间-时间戳
print(time.time())
#开发者时间
My_time = time.localtime(time.time())
print(My_time)
print(My_time.tm_year)
print(My_time.tm_mon)
#可视化时间
print(time.asctime(My_time))
#日历
print(calendar.month(2020,11))