import sys

# 1 2
# 3 4
# 0 0
for i in sys.stdin:

    j = i.split()
    sum = int(j[0]) + int(j[1])
    if sum == 0:
        break
    else:
        print(sum)
