student = {
    "name" : "Aaditya",
    "age" : 19,
    "city" : "Gr noida"
}
print(student["name"])
print(student["city"])
print(type(student))
student["city"] = "GB Nagar"
student["fav subject"] = "Maths"
print(student)
student.pop("city")
print(student)