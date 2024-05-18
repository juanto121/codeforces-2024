t = int(input())

for ti in range(t):
	n = int(input())
	chips = [int(i) for i in input().split(" ")]
	countz = 0
	seen = False
	i = 0
	gencount = 0


	while chips[i] == 0 and i < len(chips):
		i += 1

	while i < len(chips):
		countz = 0
		while  i < len(chips) and chips[i] == 1:
			i+=1
		while  i < len(chips) and chips[i] == 0:
			countz +=1
			i+=1
		if i < len(chips):
			#print(i, chips[i], countz)
			gencount += countz

	print(gencount)
