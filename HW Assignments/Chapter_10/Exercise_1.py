# (Assign grades) Write a program that reads a list of scores and then assigns grades
# based on the following scheme:
# The grade is A if score is >= best – 10.
# The grade is B if score is >= best – 20.
# The grade is C if score is >= best – 30.
# The grade is D if score is >= best – 40.
# The grade is F otherwise.


scores = input("Enter scores: ")
scoresList = [int(s) for s in scores.split()]
bestScore = max(scoresList)
for i in range(len(scoresList)):
    if scoresList[i] >= bestScore - 10:
        print('Student', i, 'score is', scoresList[i], 'and grade is A')
    elif scoresList[i] >= bestScore - 20:
        print('Student', i, 'score is', scoresList[i], 'and grade is B')
    elif scoresList[i] >= bestScore - 30:
        print('Student', i, 'score is', scoresList[i], 'and grade is C')
    elif scoresList[i] >= bestScore - 40:
        print('Student', i, 'score is', scoresList[i], 'and grade is D')
    else:
        print('Student', i, 'score is', scoresList[i], 'and grade is F')
