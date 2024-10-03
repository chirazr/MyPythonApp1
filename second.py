# Dictionaries

student={
    "name":"chiraze",
    "age": 26,
    "grade":"A",
    "city":"tunis"
}

print (student)
print(student["name"])


student["grade"] = "B"
print(student)


print(student.keys())
print(student.values())
print(student.items())

print(student.get("ggg"))