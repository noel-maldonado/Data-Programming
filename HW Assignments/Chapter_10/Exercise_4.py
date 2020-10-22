# (Analyze scores) Write a program that reads an unspecified number of scores and
# determines how many scores are above or equal to the average and how many
# scores are below the average. Assume the input numbers are separated by one
# space in one line.

scores = input("Enter scores: ")
scores_list = [int(x) for x in scores.split()]
averageScore = round(sum(scores_list) / len(scores_list))
above_or_equal = 0
below = 0
for score in scores_list:
    if score >= averageScore:
        above_or_equal += 1
    else:
        below += 1
print("There are", above_or_equal, "above or equal to the average", averageScore, "and", below, "below the average")
