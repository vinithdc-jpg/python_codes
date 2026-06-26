import random
import string

length = int(input("Enter the length of charecter: "))

charectar = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(charectar)for _ in range(length))

print("Generate password: ", password)