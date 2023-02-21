def push(item):
    global top
    if top == N - 1:
        return  # overflow
    top += 1
    S[top] = item

def pop():
    global top
    if top == -1:
        return  # empty
    ret = S[top]
    top -= 1
    return ret

n= int(input())
for s in range(n):
    S = [0]*1000
    N = len(S)
    top = -1
    strinput = input().split()
    a=ans=0
    for i in strinput:
        if i == '.':
            break
        if top <= 0: ans = 1
            break
        elif i == '+':

            else:
                a = pop()
                S[top] = a + S[top]
        elif i == '-':
            if top <= 0:
                ans =1
                break
            else:
                a = pop()
                S[top] =  S[top] - a

        elif i == '*':
            if top <= 0:
                ans =1
                break
            else:
                a = pop()
                S[top] = a * S[top]
        elif i == '/':
            if top <= 0:
                ans =1
                break
            else:
                a = pop()
                S[top] = S[top] // a

        else:
            push(int(i))
    c = top
    if ans == 1:
        c = 'error'

    else:
        if top == 0:
            c = S[0]
        else:
            c = 'error'
    print(f'#{s + 1} {c}')