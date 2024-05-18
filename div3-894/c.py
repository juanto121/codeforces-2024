def count_larger_than(i, a):
    l = 0
    r = len(a) - 1
    while l < r:
        mid = l + (r - l) // 2
        # print('->', mid, a[mid])
        if a[mid] > i:
            l = mid + 1
        else:
            r = mid - 1
        # print(' ', l, r)
        if mid == l and mid == r:
            break
    return l

print(count_larger_than(0, [5,4,3,2,1]))
print(count_larger_than(1, [5,4,3,2,1]))
print(count_larger_than(2, [5,4,3,2,1]))
print(count_larger_than(3, [5,4,3,2,1]))
print(count_larger_than(4, [5,4,3,2,1]))
print(count_larger_than(5, [5,4,3,2,1]))
print(count_larger_than(30, [5,4,3,2,1]))

# def symmetric(a):
#     counts = [0] * int(max(a))
#     for i in range(len(a)):
#         counts[i] = count_larger_than(i, a)
    
#     for i, ai in enumerate(a):
#         # print(i, counts[i], ai)
#         if counts[i] != ai:
#             return False
    
#     return True

# t = int(input())
# for ti in range(t):
#     n = int(input())
#     arr = [int(ai) for ai in input().split(' ')]
#     print('YES' if symmetric(arr) else 'NO')