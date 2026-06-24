import time

sentence = "Python is a powerful programming language."

print(sentence)

start = time.time()

typed = input("\nType above sentence:\n")

end = time.time()

if typed == sentence:
    print("Time Taken:", round(end - start, 2), "seconds")
else:
    print("Text doesn't match.")