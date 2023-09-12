def topKFrequent(num, k):
    count= {}
    freq = [[] for i in range(len(num)+ 1)]
    for n in num:
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        freq[c].append(n) #for the location of the count, append the exact number
    
    res = []
    for i in range(len(freq) -1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

    
nums = [5, 6, 6, 1, 2, 5,]
k = 3
print(topKFrequent(nums, k))

