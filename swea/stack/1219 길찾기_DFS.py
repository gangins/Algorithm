
for tc in range(1,11):

    tc_num, E= map(int,input().split())
    arr = list(map(int, input().split()))

    G =[[] for _ in range(100)] #정점번화 0~99
    #간선정보를 읽자

    for i  in range(0,E*2,2):
        u,v = arr[i], arr[i+1] # u-->v
        G[u].append(v) #유향그래프

    visited = [0]*100
    S = [0] # 출발점추가
    visited[0] = 1
    v  =0
    while S: # 빈스택이 아닐동안
        # v의 방문하지 않은 인접정점 w를 하나 선택한다.
        for w in G[v]:
            if not visited[w]:
                visited[w]= 1
                S.append(v)
                v = w
                break
        else:
            v = S.pop()

    print(visited[99])


######## 재귀
for tc in range(1,11):

    tc_num, E= map(int,input().split())
    arr = list(map(int, input().split()))

    G =[[] for _ in range(100)] #정점번화 0~99
    #간선정보를 읽자

    for i  in range(0,E*2,2):
        u,v = arr[i], arr[i+1] # u-->v
        G[u].append(v) #유향그래프

    visited = [0]*100
    S = [0] # 출발점추가
    visited[0] = 1
    v  =0
    while S: # 빈스택이 아닐동안
        # v의 방문하지 않은 인접정점 w를 하나 선택한다.
        for w in G[v]:
            if not visited[w]:
               
    print(visited[99])