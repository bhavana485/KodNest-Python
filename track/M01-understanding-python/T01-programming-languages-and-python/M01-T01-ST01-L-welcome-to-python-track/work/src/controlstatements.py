#Selection statements
#if statement
#write a python program to check whether a person is eligible to vote.if the age is 18 or above , print "Eligible to vote".
age = int(input("enter the age"))
if age >= 18:
    print("eligible for vote") 
print("Thank you")

#if-else statement 
age = int(input("enter the age"))
if age >= 18:
    print("eligible for vote") 
else:
    print("not eligible to vote")


#write a python program to accept marks and print the grade using the following conditions: 90+ -> B, 50+ -> C, 35+ -> D,otherwise -> Fail
marks = int(input("enter marks:"))
if marks > 90:
    print("Grade A")
elif marks > 70 :
    print("Grade B")
elif marks > 50:
    print("Grade C")
elif marks > 35:
    print("Grade D")
else:
    print("Fail")
#Nested if statement
#write a python program to check whether you are free tonight. if you are free, check whether your friends are available.
#print "Go out for party" if both are true;otherwise print the appropriate message .
free_tonight = true
friends_available = true
if(free_tonight):
    if(friends_available):
        print("Go out for party")
    else:
        print("seat and watch the movie")
else:
    print("not available for party")
#match - case statement 
#write a python program that accepts a number from 1 to 7 and uses match-case to print the corresponding day of the week 
match day:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("Invalid")
#match-case with multiple cases
#write a python program that accepts a month number and uses match-case to print the season: 3,4,5 -> summer, 6,7,8 ->rainy, 9,10,11,12 -> winter, and 1,2 -> autum
month = int(input("enter month number(1-)"))
match month:
    case 3|4|5 :
        print("Summer")
    case 6|7|8:
        print("Rainy")
    case 9|10|11|12:
        print("Winter")
    case 1|2:
        print("Autum")
    case _:
        print("Invalid")


#looping statements 
#for loop with range
#Write a python program to print numbers from 1 to 5 using a for loop
for i in range(1,6):
    print(i)

#for loop - first 5 numbers 
#write a python program to print the first five numbers starting from 0 using a for loop
for i in range(5):
    print(i)

#for loop with if condition
# write a python program to print all even numbers from 1 to 10 using a for loop
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

#while loop
#write a python program to print numbers from 0 to 4 using a while loop
i = 0 
while i <= 4:
    print(i)
    i += 1 # i = i + 1 

#jumping statements
#break statements 
#write a python program to print numbers from 1 to 5 , but stop 
for i in range(1,6):
    if i == 4:
        break
    print(i)

continue statement
#write a python program to print numbers from 1 to 5, but skip 
for i in range(1,6):
    if i == 4:
        continue
    print(i)

#pass statement
#write a python program using a for loop from 1 to 9 and use pass
#pass in function 
for i in range(1, 10):
    pass
#write a python program to create a function called add()without
def add():
    pass

#return statement
#write a python function called square(n) that accepts a number 
 def square(n):
    return n*n
print(square(3))
