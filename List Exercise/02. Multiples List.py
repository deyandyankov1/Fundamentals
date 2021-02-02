factor = int(input())
count = int(input())
result = 0
prime = []

for _ in range(count):
    result += factor
    prime.append(result)
print(prime)