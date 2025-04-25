with open("Puzzle.txt") as file:
    puzzle = file.read()

# Part 1
# floor_level = 0

# for x in puzzle:
#     if x == "(":
#         floor_level += 1
#     else :
#         floor_level -= 1

# print(floor_level)

# Part 2
# floor_level = 0
# index = 0

# for x in puzzle:
#     if x == "(":
#         floor_level += 1
#     else :
#         floor_level -= 1
    
#     index += 1
#     if floor_level == -1:
#         print(index)
#         break

# Part 2 Another Way
floor_level = 0

for index in range(len(puzzle)):
    if puzzle[index] == "(":
        floor_level += 1
    else:
        floor_level -= 1
    
    if floor_level == -1:
        print(index + 1)
        break