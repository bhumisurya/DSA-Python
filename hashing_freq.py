arr = [1,2,1,2,3,4,3,4,3,4,5,6,5,6,5,6,3,3,2,6]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0)+1

print(freq)