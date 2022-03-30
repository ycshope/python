'''
5 7
1 2 3 4 5
Q 1 5
5

U 3 6
1 2 6 4 5

Q 3 4
6

Q 4 5
5

U 4 5
1 2 6 5 5

U 2 9
1 9 6 5 5

Q 1 5
9
'''
if __name__ == "__main__":
    while True:
        try:
            N, M = (input().split())
            N = int(N)
            M = int(M)
            #注意这种输入
            score_list = [int(N) for N in input().split()]
            # print(f"N={N},M={M}")
            while M:
                method, A, B = (input().split())
                A = int(A)
                B = int(B)
                #Q查询
                if method == 'Q':
                    # Q 1 5
                    #从下标A-1到B
                    # 异常输入:A大于B
                    if A > B:
                        A, B = B, A
                    print(max(score_list[A - 1:B]))
                #U更新
                else:
                    # U 3 6
                    #更新下标A-1的值为B
                    score_list[A - 1] = B
                    # print(f"update... score_list={score_list}")
                M = M - 1
        except:
            break
