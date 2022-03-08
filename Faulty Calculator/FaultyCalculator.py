# Exercise - Faulty Calculator: exer_FaultyCalculator.py
# Objective: Design a calculator that takes inputs from the user and return correct result except following,
# 45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4

title = "Exercise 3 - Faulty Calculator"
subtitle = "[Note: Returns false values for few predefined calculations]"
underline = int(len(subtitle)) * "-"
print("\n{}\n{}\n{}\n".format(title, underline, subtitle))

operation = input(
    "Available calculator functions:\nType A for Addition\n     S for Subtraction\n     M for Multiplication\n     D for Divide\n\nWhich type of operation do you want to perform? ")
operands = ["A", "a", "S", "s", "M", "m", "D", "d"]
mismatch = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ",", "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", "|", "\\", "/", ":", ";", "'", '"', "<", ">", "?"]

if operation in operands:
    num1 = float(input("\nEnter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == "A" or operation == "a":
        if (num1 == 56 or num2 == 56) and (num1 == 9 or num2 == 9):
            print("\n", num1, "+", num2, "=", float(77))
        else:
            print("\n", num1, "+", num2, "=", num1 + num2)

    elif operation == "S" or operation == "s":
        print("\n", num1, "-", num2, "=", num1 - num2)

    elif operation == "M" or operation == "m":
        if (num1 == 45 or num2 == 45) and (num1 == 3 or num2 == 3):
            print("\n", num1, "*", num2, "=", float(555))
        else:
            print("\n", num1, "*", num2, "=", num1 * num2)

    else:
        if num1 == 56 and num2 == 6:
            print("\n", num1, "/", num2, "=", float(4))
        else:
            print("\n", num1, "/", num2, "=", num1 / num2)

    """
    FEATURES TO BE UPDATED,
     + Input error handling should be added
     * Two numbers right alignment in vertical order and display answer below
     
    if float(num1):
        if float(num2):
            print(float(num1) + float(num2))
        else:
            print("ABORTED, You entered a non-numeric value in second number!\nPlease try again with a numeric one.")
    else:
        print("ABORTED, You entered a non-numeric value in first number!\nPlease try again with a numeric one.")
    """

else:
    print("\nABORTED, You entered wrong option which is out of our program!\nPlease, try one more time with one from available functions.")
