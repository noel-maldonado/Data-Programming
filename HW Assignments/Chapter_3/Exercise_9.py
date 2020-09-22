#(Financial application: payroll) Write a program that reads the following information
#and prints a payroll statement:
#Employee’s name (e.g., Smith)
#Number of hours worked in a week (e.g., 10)
#Hourly pay rate (e.g., 9.75)
#Federal tax withholding rate (e.g., 20%)
#State tax withholding rate (e.g., 9%)
employeeName = input("Enter employee's name: ")
hoursWorkedInAWeek = eval(input('Enter number of hours worked in a week: '))
hourlyPayRate = eval(input('Enter hourly pay rate: '))
federalTaxRate = eval(input('Enter federal tax withholding rate (0.15 = 15%): '))
stateTaxRate = eval(input('Enter state tax withholding rate (0.15 = 15%): '))
grossPay = hoursWorkedInAWeek * hourlyPayRate
federalTaxWithholding = grossPay * federalTaxRate
stateTaxWithholding = grossPay * stateTaxRate
totalTaxDeduction = federalTaxWithholding + stateTaxWithholding
netPay = grossPay - totalTaxDeduction
print('Employee Name:', employeeName)
print('Hours Worked:', hoursWorkedInAWeek)
print('Pay Rate: $' + str(hourlyPayRate))
print('Gross Pay:', grossPay)
print('Deductions:')
print('  Federal Withholding (' + str(int(federalTaxRate * 100)) +'%):', federalTaxWithholding)
print('  State Withholding (' + str(int(stateTaxRate * 100)) +'%):', stateTaxWithholding)
print('  Total Deduction: $' + str(totalTaxDeduction))
print('Net Pay: $' + str(netPay))