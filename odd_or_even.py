arr = [11, 22, 33, 44, 55, 66]

even = 0
odd = 0

for num in arr:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)