cities = ["Bengaluru", "Pune", "bengaluru", "chennai", "pune"]
u_cities = {city.lower() for city in cities}
print(u_cities)
print(type(u_cities))

numbers = [2, 3, 2, 4, 3 ]
unique_squares = set()
for number in numbers:
    unique_squares.add(number * number)
print(unique_squares)

unique_squares = {number * number for number in numbers} 
print(unique_squares)
print(type(unique_squares))

numbers = [2, 3, 2, 4, 3 ]

squares_list = [number * number for number in numbers]
squares_set = [number * number for number in numbers]

print(squares_list)
print(squares_set)

#Dictonaries

numbers = [2, 3, 4, 5]
cube_by_number = {}
for number in numbers:
    cube_by_number[number] = number ** 3
print(cube_by_number)

cube_by_number = {number: number ** 3 for number in numbers}
print(cube_by_number)
print(type(cube_by_number))