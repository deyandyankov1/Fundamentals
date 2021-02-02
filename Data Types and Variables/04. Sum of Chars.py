number = int(input())

total_sum = 0
for _ in range(number):
    letter = input()
    char = ord(letter)
    total_sum += char



print(f"The sum equals: {total_sum}")