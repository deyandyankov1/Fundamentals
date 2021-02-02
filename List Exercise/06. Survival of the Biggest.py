list_of_strings = input().split(" ")
number_to_remove = int(input())
index_count = 0
list_of_numbers = []

for n in range(len(list_of_strings)):
    n = int(list_of_strings[index_count])
    list_of_numbers.append(n)
    index_count += 1
    list_of_numbers.sort()

index_count = 0
for number in range(number_to_remove):
    list_of_strings.remove
    index_count += 1
print(list_of_numbers)