n, k = input().split()
value = input().split()
k = int(k)
scores = list(map(int, value))
count = 0
cutoff = scores[k-1]   
for i in range(len(scores)):
    if scores[i] >= cutoff and scores[i] > 0:
        count += 1

print(count)