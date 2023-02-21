def pop():
    global top
    if top == -1:
        return  # empty
    ret = S[top]
    top -= 1
    return ret

def push(item):
    global top
    if top == N - 1:
        return  # overflow
    top += 1
    S[top] = item
tc = int(input())
for j in range(tc):
    S =[0] *100
    top = -1
    strinput = input()
    N=len(S)
    ans = 1
    for i in strinput:
        if top == -1:
            push(i)

        elif i == S[top]:
            pop()



        else:
            push(i)
    print(f'#{j+1} {top+1}')


