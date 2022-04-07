# 1 2 3 4 5
# 2 3 1
if __name__ == "__main__":
    import sys
    for i in sys.stdin:
        sum = 0
        for j in i.split():
            sum = sum + int(j)
        print(sum)
