# https://www.nowcoder.com/question/next?pid=27976983&qid=545004&tid=54425494
if __name__ == "__main__":
    import sys
    for i in sys.stdin:
        sum = 0
        for j in i.split():
            sum = sum + int(j)
        print(sum)
