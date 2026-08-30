# Payroll system using resuable functions to calculate an employee's gross salary,deductions and net salary

def calculate_overtime(hours, rate):
    return hours * rate

def calculate_gross_salary(basic_salary, overtime_pay):
    return basic_salary + overtime_pay

def calculate_tax(gross_salary):
    if gross_salary <= 20000:
        return 0
    elif gross_salary <= 40000:
        return gross_salary * 0.10
    else:
        return gross_salary * 0.20
    
def calculate_net_salary(gross_salary, tax):
    return gross_salary - tax

def display_payroll(name, basic_salary, overtime_pay, gross_salary, tax, net_salary):
    print("\n-------------PAYROLL-------------")
    print("Employee Name: " ,name)
    print("Basic Salary: ", basic_salary)
    print("Overtime Pay: ", overtime_pay)
    print("Gross Salary: ", gross_salary)
    print("Tax Deduction: ", tax)
    print("Net Salary: ", net_salary)
    
    
def main():
    name = input("Enter employee name: ")
    basic_salary = float(input("Enter basic salary: "))
    overtime_hours = float(input("Enter overtime hours: "))
    overtime_rate = float(input("Enter overtime rate: "))
    
    overtime_pay = calculate_overtime(overtime_hours, overtime_rate)
    gross_salary = calculate_gross_salary(basic_salary, overtime_pay)
    tax = calculate_tax(gross_salary)
    net_salary = calculate_net_salary(gross_salary, tax)
    
    display_payroll(
        name,
        basic_salary,
        overtime_pay,
        gross_salary,
        tax,
        net_salary
    )
    
if __name__ == "__main__":
    main()