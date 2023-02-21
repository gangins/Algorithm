l= int(input())
di = [-1, 1 ,0 ,0,]
dj = [0, 0 ,-1 ,1]
#
for k in range(l):
    lst = [list(map(int,input().split())) for i in range(100)]

for i in range(100):
    for j in range(100):
        if [i][j] == 2:
            for j in range(y):
                for W in range(4):
                    ni = i + di[W]
                    nj = j + dj[W]
                    if 0 <= ni <= x - 1 and 0 <= nj <= y - 1:
                        if lst[i][j] > lst[ni][nj]:
                            cnt += 1
