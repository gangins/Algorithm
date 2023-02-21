
l= int(input())
di = [-1, 1 ,0 ,0,1,1,-1,-1]
dj = [0, 0 ,-1 ,1,1,-1,-1,1]
#
for k in range(l):
    x,y = map(int,input().split())
    lst = [list(map(int,input().split())) for i in range(x)]
    z = [[0]*y for i in range(x)]
    sub = 0
    for i in range(x):
        for j in range(y):
            cnt = 0
            for W in range(8):
                ni = i + di[W]
                nj = j + dj[W]
                if 0 <= ni <= x-1 and 0 <= nj <= y-1:
                    if lst[i][j] > lst[ni][nj]:
                        cnt += 1
            if cnt >= 4:
                sub+=1

    print(f'#{k+1} {sub}')








