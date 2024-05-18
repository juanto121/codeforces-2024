t = int(input())

for ti in range(t):
	n = int(input())
	
	b = [int(x) for x in input().split(" ")]
	res = [b[0]]
	for ai in range(1,n):
		if b[ai] < b[ai-1]:
			res.append(b[ai])
		res.append(b[ai])


	print(len(res))
	print(' '.join([str(r) for r in res]))
	