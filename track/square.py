#square
square = []
for i in range(1,6):
    square.append(i*i)
print(square)

square = [i * i for i in range(1, 6)]
print(square)

number = [i for i in range(1, 11) if i % 2 == 0]
print(number)

number = [10, 3, 12, 5, 43, 7]
new_list = [i for i in number if i >= 10]
print(new_list)

names = ["ravi", "abhi" , "sita", "geetha", "mona"]
new_list = [name.upper() for name in names]
print(new_list)

