
t = int(input())
for ti in range(t):
	n, q = [int(x) for x in input().split(" ")]
	c = [int(x) for x in input().split(" ")]
	prefix = [0] * n
	prefix[0] = c[0]
	one_count = [0] * n
	one_count[0] = 1 if c[0] == 1 else 0
	for i in range(1, n):
		prefix[i] = prefix[i-1] + c[i]
		one_count[i] = one_count[i-1] + (1 if c[i] == 1 else 0)
	for qi in range(q):
		l, r = [int(x) for x in input().split(" ")]
		if r == l:
			print("NO")
			continue
		range_sum = prefix[r-1] - prefix[l-1] + 1
		ones = one_count[r-1] - one_count[l-1] + 1
		diff_1s = r - l + 1 - ones
		#print(c[l-1:r])
		#print("onec", one_count)
		#print(l, r)
		#print(prefix)
		#print(one_count, r, l)
		#print(ones, diff_1s, range_sum)
		if 2 * ones + diff_1s <= range_sum:
			print("YES")
		else:
			print("NO")