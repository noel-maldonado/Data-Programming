#   (Find the highest score) Write a program that prompts the user to enter the number
#   of students and each student’s score, and displays the highest score. Assume that
#   the input is stored in a file named score.txt, and the program obtains the input from
#   the file.


#Does not specify that I have to collect the students names only the scores.

numberOfStudents = eval(input('Enter the number of students: '))
i = 1
maxScore = 0
while i <= numberOfStudents:
    tempScore = eval(input("Enter score for student " + str(i)+ ": "))
    if tempScore > maxScore:
        maxScore = tempScore
    i += 1
print("Max Score: " + str(maxScore))