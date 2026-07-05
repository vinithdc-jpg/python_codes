import random
import string

length = int(input("Password Length: "))

chars = string.ascii_letters + string.digits + "!@#$%^&*"

password = ''.join(random.choice(chars) for _ in range(length))

print("Generated Password:", password)