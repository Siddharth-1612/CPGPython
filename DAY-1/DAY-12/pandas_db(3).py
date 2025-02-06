import pandas as pd
import csv

num_employees = int(input("Enter number of employees: "))


with open("employee_details.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Age", "Department", "Salary"])  
    
    for i in range(num_employees):
        emp_id = input(f"Enter Employee {i+1} ID: ")
        name = input(f"Enter Employee {i+1} Name: ")
        age = input(f"Enter Employee {i+1} Age: ")
        dept = input(f"Enter Employee {i+1} Department: ")
        salary = input(f"Enter Employee {i+1} Salary: ")
        
        writer.writerow([emp_id, name, age, dept, salary])  

print("\nEmployee details saved to CSV successfully!\n")

df = pd.read_csv("employee_details.csv")
print("Employee Data from CSV:\n")
print(df)
