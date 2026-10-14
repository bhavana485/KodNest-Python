#sorted() result will be in  new list

marks = [60,73,48,50]
new_marks = sorted(marks, reverse = True)
print(new_marks)
print(marks)

#sort result will be sorted in original list 

age = [2, 30, 1, 18]
age.sort(reverse = True)
print(age)

res = sorted(age)
print(res)

names = ["apple", "mango", "banana"]
names.sort()
print(names)

names = {"apple", "mango", "banana"}
print(sorted(names))

#cannot be used 
names = {"apple", "mango", "banana"}
names.sort()
print(names)