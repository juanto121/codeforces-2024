t = int(input())
for ti in range(t):
    n, k = [int(ai) for ai in input().split()]
    a = [int(ai) for ai in input().split()]
    if k in a:
        print('YES')
    else:
        print('NO')