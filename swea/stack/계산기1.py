import sys;


sys.stdin = open('input (15).txt', 'r', encoding='utf-8')
icp = {'(' : 3, '*' : 2, '/' : 2, '+' : 1, '-':1}
isp = {'(' : 0, '*' : 2, '/' : 2, '+' : 1, '-':1}


for s in range(1):
    n = int(input())
    stack= []
    infix = input()
    postfix = ''
    # 중위 표기법 ->후위표기법법
    for t in infix:
        if '0' <= t <= '9':
            postfix += t
        else:
            if len(stack) == 0 or isp[stack[-1]] < icp[t]: #스택이 비어있거나(비교할 연산자 없거나)
                stack.append(t)
                # t의 우선순위가 높으면 연산자 push
            elif isp[stack[-1]] >= icp[t]:              #스택 맨위 연산자읜 순위가 같거나 높으면
                while len(stack) > 0 and isp[stack[-1]] >= icp[t]:        #t보다 우선 순위가 낮은 연산자가 나올때 까지 pop
                    postfix += stack.pop()
                stack.append(t)


    while stack:                           #스택에 연산자가 남아있으면
        postfix += stack.pop()
    # 후위식 계산식
    stack = [0] * n

    for t in postfix:
        if t in ['+','-','*','/']:
            op2 = stack.pop()
            op1 = stack.pop()
            ans = 0
            if t == '+':
                ans = op1 + op2
                stack.append(ans)
            elif t == '*':
                ans = op1 * op2
                stack.append(ans)
            elif t == '-':
                ans = op1 - op2
                stack.append(ans)
            elif t == '/':
                ans = op1 // op2
                stack.append(ans)
        else:
            stack.append(int(t))

    print(f'#{s+1}', stack.pop())


