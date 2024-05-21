t = int(input())
for ti in range(t):
    n = int(input())
    nums = []
    a = 5
    while len(nums) < n:
        nums.append(str(a))
        b = a + 1
        c = b + 1
        while 3 * c % (a + b) == 0:
            b = b + 1
            c = c + 1
        if len(nums) < n:
            nums.append(str(b))
        if len(nums) < n:
            nums.append(str(c))
        a = c + 1
        # assert 3 * nums[-1] % (nums[-2] + nums[-3]) != 0
    print(" ".join(nums))