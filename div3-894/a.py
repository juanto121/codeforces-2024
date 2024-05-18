t = int(input())

for ti in range(t):
	carpet = []
	n,m = [int(i) for i in input().split(" ")]
	for ni in range(n):
		row = input()
		carpet.append([c for c in row])
	seen = ['v','i','k','a']
	seenidx = 0
	for c in range(m):
		for r in range(n):
			car = carpet[r][c]
			if car == seen[seenidx]:
				seenidx +=1
				break
		if seenidx > 3:
			break

	if seenidx == 4:
		print('YES')
	else:
		print('NO')
