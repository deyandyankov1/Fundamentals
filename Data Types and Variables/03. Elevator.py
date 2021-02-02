import math
persons = int(input())
elevator_capacity = int(input())

courses = math.ceil(persons / elevator_capacity)

print(math.ceil(courses))