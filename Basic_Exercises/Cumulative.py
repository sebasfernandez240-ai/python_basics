rank = 10
previous_number = 0
print(f"Print the sum of the current and previous number in a range {rank}")
for c_number in range(rank):
    total = c_number + previous_number
    print(f"Current number {c_number} Previous number {previous_number} sum: {total}")
    previous_number = c_number