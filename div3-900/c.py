t = int(input())
for ti in range(t):
    n, k, x = [int(j) for j in input().split(" ")]
    
    max_achievable_n = n * ( n + 1) / 2
    max_achievable_mk = (n-k) * ((n-k) + 1) /2
    max_achievable = max_achievable_n - max_achievable_mk
    if x > max_achievable:
        print('NO')
        continue
    
    smallest_sum_of_k_diff_elements = k * (k + 1) / 2 
    if x < smallest_sum_of_k_diff_elements:
        print('NO')
        continue

    print('YES')


