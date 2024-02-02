inputted = lowerCase = upperCase = vowels = consonants = numerics = nonLetters = 0
while True:
    inp_String = input('Input a string (or ENTER to exit): ')
    if inp_String == '':
        break
    for _ in inp_String: 
        inputted += 1
        if _ in 'abcdefghijklmnopqrstuvwxyz':
            lowerCase += 1 
            if _ in 'aeiou': 
                vowels += 1 
            else: 
                consonants += 1
        elif _ in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            upperCase += 1 
            if _ in 'AEIOU':
                vowels += 1 
            else: 
                consonants += 1
        elif _ in '1234567890':
            numerics += 1
            nonLetters += 1
        else:
            nonLetters += 1
print()
print('Summary of Total Characters:')
print(f'Inputted = {inputted}')
print(f'Lowercase = {lowerCase}')
print(f'Uppercase = {upperCase}')
print(f'Vowels = {vowels}')
print(f'Consonants = {consonants}')
print(f'Numerics = {numerics}')
print(f'Non-letters = {nonLetters}')

