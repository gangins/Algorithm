l = int(input())
for tc in range(l)

    N, W = map(int, input().split())
    a = 0
    arr = [list(map(int,input().split())) for i in range(N)]
    max_val = 0
    for i in range(N - W + 1):
        for j in range(N - W + 1):

            for c in range(W):
                for z in range(W):
                    a += arr[i+c][j+z]

            if a > max_val:
                max_val = a
            a = 0


    print(f'#{tc+1} {max_val}')