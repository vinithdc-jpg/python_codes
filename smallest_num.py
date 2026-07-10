arr = [12, 45, 7, 89, 23]

smallest = arr[0]

for num in arr:
    if num < smallest:
        smallest = num

print("Smallest element:", smallest)