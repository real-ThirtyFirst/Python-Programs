# Assignment #2

inp_Num = int(input("Enter the size (factor) of mul.table: "))
charSize = len(str(inp_Num))
cS = len(str(inp_Num**2))
print(f'{"x":>{charSize}}', end="")
for row in range(1, inp_Num+1):
    print(f'|{row:>{cS}}', end="")
print()
print(f'{("-"*charSize)+"+"+(("-"*cS)+"+")*(inp_Num - 1)+('-'*cS)}')
for row in range(1, inp_Num+1):
    print(f'{row:>{charSize}}', end="")
    for column in range(1, inp_Num + 1):
        newColumn = column * row
        print(f'|{newColumn:>{cS}}', end="")
    print()
