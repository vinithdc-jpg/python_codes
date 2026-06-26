text = input("Enter text: ")
shift = int(input("Enter shift value: "))

encrypted = ""

for char in text:
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        encrypted += chr((ord(char) - base + shift) % 26 + base)
    else:
        encrypted += char

print("Encrypted:", encrypted)