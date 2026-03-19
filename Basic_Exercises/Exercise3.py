string = input(":: ")

print(f"The original string is {string}")

for i in range(len(string)):
    if i % 2 == 0:
        print(string[i])