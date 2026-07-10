arr = [10, 20, 20, 30, 40, 40, 50]

unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print("Array without duplicates:", unique)