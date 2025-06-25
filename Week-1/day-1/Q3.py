base = float(input("Base salary: "))
hra = float(input("HRA: "))
epf = float(input("EPF deduction: "))
ppf = float(input("PPF deduction: "))
salary = base + hra - epf - ppf
print("Gross Salary:", salary)
tax_rate = float(input("Tax rate (%): ")) / 100
tax_amount = salary * tax_rate
print("Tax Amount:", tax_amount)
in_hand_salary = salary - tax_amount
print("In-Hand Salary:", in_hand_salary)