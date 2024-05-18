import math

def get_divisors(n):
	divs = []
	for i in range(2, int(math.sqrt(n)) + 1):
		if n%i == 0:
			divs.append(i)
	return divs

t = int(input())

for ti in range(t):
	res = []
	l, r = [int(x) for x in input().split(" ")]
	
	if l <=2 and r<=3:
		print(-1)
	elif l == r:
		divs = get_divisors(l)
		if len(divs) == 0:
			print(-1)
		else:
			print(r - divs[0], divs[0])
	else:
		pe = r if r % 2 == 0 else r - 1
		half = int(pe/2)
		print(int(pe/2), int(pe/2))
		assert 2 * half >= l 
		assert 2 * half <= r