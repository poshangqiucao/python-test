

employee_file = open("employees.txt","r")

# print(employee_file.readable())
# print(employee_file.readline())
# print(employee_file.readline())
# print(employee_file.readline())
# print(employee_file.readlines()[3])
for employee in employee_file.readlines():
    print(employee)


employee_file.close()