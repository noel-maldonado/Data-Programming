# (Count single digits) Write a program that generates 1,000 random integers
# between 0 and 9 and displays the count for each number. (Hint: Use a list of ten
# integers, say counts, to store the counts for the number of 0s, 1s, ..., 9s.)

import random

random_list = []
for i in range(1000):
    random_list.append(random.randint(0, 9))

number_counts = []

# uses the index to count how many occurrences of that number there are in the list
for i in range(10):
    number_counts.append(random_list.count(random_list[i]))

for i in range(10):
    print(i, ":", number_counts[i], "times")

# print(len(random_list))

