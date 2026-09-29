s1 = "hello"
print(id(s1), s1)

s1 = (s1 + "World")
print(s1)
print(id(s1))

s1 = "hello"
s2 = s1 + "world"
print(id(s1),s1)
print(id(s2),(s2))

s1 = "python"
s2 = "python"
print(id(s1),s1)
print(id(s2),s2)
print(s2 == s2)
print(s1 is s2)

s1 = "python"
print(s1)
print(s1[2])
print s1[5]
print s1[1:4]
print s1[ 0:5]
print s1[: ]
print s1[ : 4]
print s1[2:]
print s1[1: ]
print s1[0::1]
print s1[0::2]
print s1[1:5:2]
print s1[::3]
print s1[2:3]
print s1[2:5:2]

