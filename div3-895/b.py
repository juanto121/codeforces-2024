import math
t = int(input())
for ti in range(t):
	n = int(input())
	reachable = []
	for ni in range(n):
		d,s = [int(x) for x in input().split(" ")]
		reachable.append(d + math.floor((s-1)/2))
	max_reach = min(reachable)
	print(max_reach)


