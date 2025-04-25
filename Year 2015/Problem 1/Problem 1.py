
with open("Year 2015/Problem 1/Puzzle.txt") as file:
    puzzle = file.read()

floor_level = 0

for x in puzzle:
    if x == "(":
        floor_level += 1
    else :
        floor_level -= 1

print(floor_level)