
# Read text file lines as a list
with open("Puzzle.txt") as file:
    list_of_box_sizes = file.readlines()

#  Format of item in list
# '20x3x11\n'

#wrapping_paper_needed = 0
dimension_array = list()

# Part 1
# for dimension in list_of_box_sizes:
    
#     # Clean Data
#     dimension.removesuffix('\n')
#     dimension_array = list()
#     for x in dimension.split('x'):
#         dimension_array.append(int(x))
    
#     # Finding Surface Area
#     wrapping_paper_needed += 2 * dimension_array[0] * dimension_array[1] + 2 * dimension_array[1] * dimension_array[2] + 2 * dimension_array[0] * dimension_array[2]

#     # Finding Slack 
#     for i in range(len(dimension_array)):
#         for j in range(i+1, len(dimension_array)):
#             if (dimension_array[i] > dimension_array[j]):
#                 temp = dimension_array[j]
#                 dimension_array[j] = dimension_array[i]
#                 dimension_array[i] = temp

#     wrapping_paper_needed += dimension_array[0]* dimension_array[1]

# print(wrapping_paper_needed)

ribbon = 0

# Part 2

for dimension in list_of_box_sizes:

    #Clean Data
    dimension.removesuffix('\n')
    dimension_array = list()
    for x in dimension.split('x'):
        dimension_array.append(int(x))

    #Bow is
    ribbon += dimension_array[0] * dimension_array[1] * dimension_array[2]

    #Smallest perimeter area
    for i in range(len(dimension_array)):
        for j in range(i+1, len(dimension_array)):
            if (dimension_array[i] > dimension_array[j]):
                temp = dimension_array[j]
                dimension_array[j] = dimension_array[i]
                dimension_array[i] = temp

    ribbon += 2 * dimension_array[0] + 2 * dimension_array[1]

print(ribbon)
