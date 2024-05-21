def pos_first_less_or_eq(i, a):
    l = 0
    r = len(a) - 1
    while l < r:
        mid = l + (r - l) // 2
        if a[mid] < i:
            r = mid
        else:
            l = mid + 1
    if l < 0:
        return 0
    if l >= len(a):
        return l + 1
    if a[l] >= i:
        return l + 1
    else:
        return l

def symmetric(a):
    counts = [0] * int(len(a) + 1)
    for i in range(1, len(a) + 1):
        counts[i] = pos_first_less_or_eq(i, a)

    for i in range(1, len(a) + 1):
        if counts[i] != a[i-1]:
            return False
    
    return True

t = int(input())
for ti in range(t):
    n = int(input())
    arr = [int(ai) for ai in input().split(' ')]
    print('YES' if symmetric(arr) else 'NO')