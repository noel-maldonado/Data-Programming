#(Financial application: calculate future investment value) Write a program that
#reads in an investment amount, the annual interest rate, and the number of years,
#and displays the future investment value using the following formula:
#
#futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate)^numberOfMonths
#
#For example, if you enter the amount 1000, an annual interest rate of 4.25%,
#and the number of years as 1, the future investment value is 1043.33. Here is a
#sample run:

amount  = eval(input("Enter investment amount (1000 for $1000): "))
interestRate = eval(input("Enter annual interest rate (4.25 = 4.25%): "))
years = eval(input("Enter number of years: "))
loanTotalValue = amount * (1 + ((interestRate / 100) / 12)) ** (years * 12.0)
formatedTotalValue = int(loanTotalValue * 100) / 100
print("Accumulated value is ", formatedTotalValue)