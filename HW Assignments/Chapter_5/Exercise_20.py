#(Display four patterns using loops) Use nested loops that display the following
#patterns in four separate programs:


# Pattern A
print()
print("Pattern A")
print("------------")

for i in range(1, 6 + 1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()


print()
print("Pattern B")
print("------------")

for i in range(1, 6 + 1):
    for j in range(1, 7 - i + 1):
        print(j, end = " ")
    print()

print()
print("Pattern C")
print("------------")

for i in range(1, 6 + 1):
    # Print leading space
    for j in range(6 - i, 0, -1):
        print("  ", end="")

    for j in range(i, 0, -1):
        print(j, end=" ")

    print()

print()
print("Pattern D")
print("------------")

for i in range(1, 6 + 1):
    # Print leading space
    for j in range(i, 1, -1):
        print("  ", end="")

    for j in range(1, 6 + 1 - i + 1):
        print(j, end=" ")

    print()