# Assignment #1

max_Num = min_Num = int(input("Enter a number (or 0 to stop): ")) # initial: Sets all variables into what number you pressed first then proceed to 6th line
ans = int(input("Enter a number (or 0 to stop): "))
while ans != 0: # While statement decides whether you input is 0 or not, if not, proceed to the 7th line, if true proceed to 13th line
    if ans != 0: # if statement to distinguish if you input 0 or not, if not, then proceed to 13th line.
        if max_Num < ans:  # if statement if your input number is bigger than the current max number, if false then proceed to 11th line, if true, proceed to 10th line
            max_Num = ans # Sets the new biggest maximum number for max variable, then loop back to the 7th line
        elif min_Num > ans: # elif statement if the first condition is false and if your input number is smaller than the current min number. Then proceed to 12th line
            min_Num = ans # Sets the new smallest minimum number for min variable, then loop back to the 7th line
    ans = int(input("Enter a number (or 0 to stop): ")) # loopable input: Waits for your answer to proceed to 8th line
print(f"You've input 0, the program stopped! Max: {max_Num} and Min: {min_Num}") # Prints when you enter an input 0
