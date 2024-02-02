mlist = [
    [2, 15, 8],
    [13, 7, 14],
    [1, 16, 9],
    [44, 11, 5],
]
print()
r = int(input('Select a row: '))
c = int(input('Select a column: '))
res = mlist[r][c]
print()
print(f'The value at ({r},{c}) is {res}')
print()
r2D = int(input('Select a row to display: '))
g = mlist[r2D]
res = ','.join(f'{_}' for _ in g)
print()
print(f'Values at row 1: {res}')
newItem = input('Enter 3 new values (2-digit, comma-separated): ').split(',')
mlist.append([int(_) for _ in newItem])
print()
for row in mlist:
    res = ','.join(f'{_:>{2}}' for _ in row)
    print(f'{res}')