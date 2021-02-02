divisor = int(input())
bound = int(input())
n=bound
while divisor <= bound:
    if n % divisor == 0 and n <= bound:
        print(n)
        break
    n -= 1


# for num in range (divisor, bound+1):
#     num = + 1
#     if num == bound:
#         print(num)

