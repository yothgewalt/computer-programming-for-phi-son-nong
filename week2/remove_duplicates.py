nums = [1, 2, 3, 4, 5, 1, 2, 3]
unique = []

for n in nums:
    if n not in unique:
        unique.append(n)
        
print(unique)
