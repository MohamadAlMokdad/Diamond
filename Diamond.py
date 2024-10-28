num_rows = int(input("Enter the number of rows: "))
for i in range(num_rows):
    print(' ' * (num_rows - i - 1) + '*' * (2 * i + 1))


for i in range(num_rows - 1):  
    print(' ' * (i + 1) + '*' * (2 * (num_rows - i - 2) + 1))
