my_list = [
    [0.3, 0.5, 0.7],
    [0.2, 0.9, 1.0],
    [0.4, 0.5, 0.8],
    ]


sum_my_list = 0

for row in range(len(my_list)):
    for col in range(len(my_list[row])):
        sum_my_list += my_list[row][col]
    

print(sum_my_list)