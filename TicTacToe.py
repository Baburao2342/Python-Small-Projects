import random

box = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

result = 2
inputs = []


print('''

    Welcome to Tic-Tac-Toe!
    You will be cooked.

''')



# Game Logic

while result == 2:

    for row in box:
        print(row, end='\n')

    coords = input("Enter the coords of your mark! (row, column) (1-3): ")
    parts = coords.split(',')
    input_row = int(parts[0]) - 1
    input_column = int(parts[1]) - 1
    inputs.append((input_row, input_column))

    if box[input_row][input_column] not in ['*', 'o']:
        box[input_row][input_column] = '*'
    
    valid = False

    while not valid:
        comp_row = random.randint(0, 2)
        comp_column = random.randint(0, 2)

        if box[comp_row][comp_column] not in ['*', 'o']:
            box[comp_row][comp_column] = 'o'
            valid = True
            break
        else:
            valid = False

    for row in box:
        if row[0] != " " and all(cell == row[0] for cell in row):
            if row[0] == '*':
                result = 1
                break
            else:
                result = 0
                break
        
    
    for column in range(3):
        column_cells = [row[column] for row in box]

        if column_cells[0] != " " and all(cell == column_cells[0] for cell in column_cells):
            if column_cells[0] == '*':
                result = 1
                break
            else:
                result = 0
                break

    for point in range(3):
        diagonal_left = [row[point] for row in box]
        diagonal_right = [row[2-point] for row in box]
    
    if diagonal_left[0] != " " and all(cell == diagonal_left[0] for cell in diagonal_left):
        if diagonal_left[0] == '*':
            result = 1
            break
        else:
            result = 0
            break

    if diagonal_right[0] != " " and all(cell == diagonal_right[0] for cell in diagonal_right):
        if diagonal_right == '*':
            result = 1
            break
        else:
            result = 0
            break

    

for row in box:
    print(row, end='\n')

if result == 1:
    print('Victory!')
elif result == 0:
    print('Loss!')
else:
    print('Draw!')
