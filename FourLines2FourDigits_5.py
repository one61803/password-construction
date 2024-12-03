"Called FourLines2FourDigits_5.py"
import random

def string_hash_9(st):
    x = 31
    Z = 999999937
    for i in range(len(st)):
        if (i == 0):
            accumulator = ord(st[0])
        else:
            accumulator = ((x * accumulator) + ord(st[i])) % Z
    return accumulator

"http://primenumberslist.com"

def string_hash_6(st):
    x = 31
    Z = 999983
    for i in range(len(st)):
        if (i == 0):
            accumulator = ord(st[0])
        else:
            accumulator = ((x * accumulator) + ord(st[i])) % Z
    return accumulator

def digit_mask(digit):
    digit_string = ""
    digit_sum = 0
    for i in range(15):
        new_digit = random.randrange(0, 10)
        digit_string += str(new_digit)
        digit_sum += new_digit
        digit_sum %= 10
        digit_string += "  "
    gap = digit - digit_sum
    while gap < 0:
        gap = gap + 10
    while gap >= 10:
        gap = gap - 10
    digit_string += str(gap)
    print(digit_string)

def buffer_digit():
    OK = False
    while not OK:
        digit_string = ""
        digit_sum = 0
        for i in range(16):
            new_digit = random.randrange(0, 10)
            digit_string += str(new_digit)
            digit_sum += new_digit
            digit_sum %= 10
            digit_string += "  "
        digit_string += "? "
        #print("53. DEBUG: digit_sum = ", digit_sum)
        input_digit = input(digit_string)
        input_digit = int(input_digit)
        if (input_digit == digit_sum):
            OK = True
    
"BEGIN"
numbers = [0, 0, 0, 0]
answer = ""
errorFlag = False
while not (answer in ['y', 'n']):
    answer = input("Load (y/n)? ")
if answer == "y":
    filename = input("Enter filename: ")
    if not (filename[-3:] == ".4D"):
        print("Wrong file extension.")
        errorFlag = True
    with open(filename) as thefile:
        i = -5
        for fileline in thefile:
            fileline = fileline.rstrip('\n')
            if i <= -1:
                print(fileline)
            elif i <= 3:
                numbers[i] = int(fileline[14:])
            else:
                print(fileline)
                if fileline == "Program: FourLines2FourDigits_5.py":
                    print("Python program and file match.\n")
                else:
                    print("Python program and file DO NOT match.\n")
                    errorFlag = True
            i += 1

lines = ["", "", "", ""]
digits = [-1, -1, -1, -1]

for i in range(4):
    j = i + 1
    input_string = input("Enter line " + str(j) + ": ")
    lines[i] = input_string
    thehash = string_hash_9(lines[i])
    print("line " + str(j) + ": " + str(thehash))
    if answer == "n":
        numbers[i] = thehash
    elif answer == "y":
        if thehash == numbers[i]:
            print("Line " + str(j) + " has the expected hash.")
        else:
            print("Line " + str(j) + " has the wrong hash.")
            errorFlag = True
            break
    digits[i] = string_hash_6(lines[i]) % 10

"Check the digits for redundancies."
if digits[0] == digits[1]:
    print("ERROR: Digits 0 and 1 are the same.")
    errorFlag = True

if digits[0] == digits[2]:
    print("ERROR: Digits 0 and 2 are the same.")
    errorFlag = True

if digits[0] == digits[3]:
    print("ERROR: Digits 0 and 3 are the same.")
    errorFlag = True

if digits[1] == digits[2]:
    print("ERROR: Digits 1 and 2 are the same.")
    errorFlag = True

if digits[1] == digits[3]:
    print("ERROR: Digits 1 and 3 are the same.")
    errorFlag = True

if digits[2] == digits[3]:
    print("ERROR: Digits 2 and 3 are the same.")
    errorFlag = True

if not errorFlag:
    print("The digits are OK (i.e. all different from each other).")

if (not errorFlag) and (answer == "y"):
    print("Add each row of digits modulo 10 mentally in order to obtain each digit.\n")
    print("Rows that end in question mark are buffers, but their sum must be input before\n")
    print("moving on to the next line.\n")
    cont = True
    while cont:
        print("The four digits are (add):\n")
        buffer_digit()
        for i in range(4):
            digit_mask(digits[i])
            buffer_digit()
        contanswer = ""
        while not (contanswer in ['y', 'n']):
            contanswer = input("Again (y/n)? ")
        if contanswer == "n":
            cont = False
        else:
            print("\n\n\n\n")

if (answer == "n") and (not errorFlag):
    saveanswer = ""
    while not (saveanswer in ["y", "n"]):
        saveanswer = input("Save (y/n)?")
    if saveanswer == "y":
        newfilename = input("Enter new filename: ")
        with open(newfilename, "w") as newfile:
            bookname = input("Enter book's name: ")
            newfile.write("Book: " + bookname + "\n")
            author = input("Who is its author? ")
            newfile.write("Author: " + author + "\n")
            publisher = input("Who is its publisher? ")
            newfile.write("Publisher: " + publisher + "\n")
            library = input("What library is the book housed in? ")
            newfile.write("Library: " +  library + "\n")
            pagenumber = input("Enter page number: ")
            newfile.write("Page: "+ str(pagenumber) + "\n")
            ii = 1
            for anumber in numbers:
                newfile.write("Line " + str(ii) + " hash9: " + str(anumber) + "\n")
                ii += 1
            newfile.write("Program: FourLines2FourDigits_5.py")
        print("New file has been written. Reconstruct the password in order to confirm it.")
        print("Do not assign the password until it has been confirmed.")
        print("\nMETADATA")
        print("Filename: " + newfilename)
        print("Executor: FourLines2FourDigits_5.py")
        print("Book's name: " + bookname)
        print("Book's author: " + author)
        print("Books' publisher: " + publisher)
        print("Book's location: " + library)
else:
    print("Close this window down when ending the session.\n")
    print("Also play some mind-clearing game.")
