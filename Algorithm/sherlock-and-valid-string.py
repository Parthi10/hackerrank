from collections import Counter
s = input().strip()
freq =Counter(s)
# print(freq)
discrepancyCount = len(set(freq.values()))
# print(discrepancyCount)
if discrepancyCount <= 2:
    if discrepancyCount == 1:
        print("YES")
    else:
        maxCount = list(freq.values()).count(max(freq.values()))
        minCount = list(freq.values()).count(min(freq.values()))
        if minCount <=1 or maxCount <=1:
            print("YES")
        else:
            print("NO")
else:
    print("NO")

# print(freq.most_common(len(s)))
# print(Counter(freq.values()))
# most_common_freq = Counter(freq.values()).most_common(len(s))
# print(freq.values())
# print("most_common_freq", most_common_freq)
# most_common_freq = Counter(freq.values()).most_common(len(s))
# print(most_common_freq)
# discrepancyCount = len(most_common_freq)
# print("total num of discrepancyCount", discrepancyCount)

# discrepancyCount = 0
# for i in freq.values():
