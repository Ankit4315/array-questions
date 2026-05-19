# Find the maximum and minimum element in an array

arr = [12, 3, 4, 5, 5, 100]

max = 0
min = float('inf')

for i in arr:
    if max < i:
        max = i
    if min > i:
        min = i

print(max)
print(min)