t = int(input())

for ti in range(t):
	monsters, bullets = [int(i) for i in input().split(" ")]
	lifes = [int(i) for i in input().split(" ")]
	positions = ([abs(int(i)) for i in input().split(" ")])
	monster_lifes = [0] * (monsters + 1)
	for i in range(monsters):
		monster_lifes[positions[i]] += lifes[i]
	extra_bullets = 0
	possible = True
	for i in range(1, monsters + 1):
		extra_bullets = bullets + extra_bullets
		extra_bullets -= monster_lifes[i]
		if extra_bullets < 0:
			possible = False
			break

	print('YES' if possible else 'NO')
