students = {
    "name":"Asha",
    "subjects":["Python","SQL","Java"]
}
print(students)


students = [
    {
        "name": "Asha",
        "branch": "CSE"
    },
    {
        "name":"Ravi",
        "branch":"ECE"
    }
]
print(students)

students = [
    {
        "name": "Asha",
        "marks": [78,85,91]
    },
    {
        "name":"Ravi",
        "marks": [72,88,80]
    }
]

student = {
    "name": "Asha",
    "marks": {
        "Python":88,
        "SQL":82
    }
}

#accessing a list inside a dictionaries

student = {
    "name": "Asha",
    "skills": ["Python", "Java"]

}

#to acces complete skill
print(student["skills"])

#to access the second skill
print(student["skills"][1])


