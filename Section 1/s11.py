#Dictionary data type

employee = {
    "name" : "John Doe",
    "age" : 30,
    "position" : "Software Engineer",
    "salary" : 285000
}

print("The name of the eployee is: " , employee["name"])
print ("The age of the employee is: ", employee["age"])
print ("The position of the employee is: ", employee["position"])
print("The salary of the employee is: ", employee["salary"])

employee["department"] = "IT"
print(employee)

employee["salary"] = 300000
print(employee)