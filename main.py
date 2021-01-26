import selenium

percentage = 100
salary = 80000
government_tax = 13

tax_amount = (salary / percentage)*government_tax

real_salary = salary - tax_amount
print('Your real salary = ' + ' ' + str(real_salary))
