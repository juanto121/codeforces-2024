t = int(input())
for tc in range(t):
    n = int(input())
    arr = [int(ai) for ai in input().split(" ")]
    pairs = {}
    for j in range(len(arr) - 2):
        [a,b,c] = arr[j:j+3]
        tuples = [
            (b,c,0), #ignoring 0
            (a,c,1), #ignoring 1
            (a,b,2), #ignoring 2
        ]
        ignore_list = [a, b, c]
        for id, ti in enumerate(tuples):
            if ti not in pairs:
                pairs[ti] = {}
            ignores = ignore_list[id]
            if ignores not in pairs[ti]:
                pairs[ti][ignores] = 0
            pairs[ti][ignores] += 1
    
    res = 0
    for pair in pairs.keys():
        subres = 0
        pk = list(pairs[pair].keys()) # keys of a pair {a: 1, b: 2, c: 3} -> [a, b, c]
        l = len(pk)
        if l > 1:
            keystosum = [pairs[pair][i] for i in pk]
            # print(keystosum)
            totalsumkeys = sum(keystosum)
            for key in pairs[pair]:
                subres += pairs[pair][key] * (totalsumkeys - pairs[pair][key])
            subres /= 2
        res += int(subres)
    print(res)
