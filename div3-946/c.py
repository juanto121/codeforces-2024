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
        pk = list(pairs[pair].keys())
        l = len(pk)
        if l > 1:
            for i in range(l):
                for j in range(i + 1, l):
                    subres += pairs[pair][pk[i]] * pairs[pair][pk[j]]
        res += subres
    print(res)
            
    



            
            
            
