import math
t = int(input())
for ti in range(t):
	a, b, c = [int(x) for x in input().split(" ")]
	half = (a + b)/2
	missing = max(a,b) - half
	
	if a == b:
		print(0)
	elif c >= missing:
		print(1)
	else:
		print(math.ceil(missing/c))


