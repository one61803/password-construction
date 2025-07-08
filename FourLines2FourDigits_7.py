"This file is called FourLines2FourDigits_7.py."
"It was forked from FourLines2FourDigits_6.py."
"Objective of this version: changing how passwords are stored in the password shuttle."
import random
from datetime import date

"The output of shuttle output mode of this program can be read with ShuttleReader_2.py."

"""SUMMARY OF PROGRAM'S ATTRIBUTES
Name: FourLines2FourDigits_7.py
Extension of password-constructing file: .4L4D
Input work level: 4 lines
Output password entropy: 13.2 bits
Output information entropy: 12.3 shannons"""

def string_hash_9(st):
    x = 31
    Z = 999999937
    for i in range(len(st)):
        if (i == 0):
            accumulator = ord(st[0])
        else:
            accumulator = ((x * accumulator) + ord(st[i])) % Z
    return accumulator

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
    while (gap < 0):
        gap = gap + 10
    while (gap >= 10):
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
        input_digit = input(digit_string)
        input_digit = int(input_digit)
        if (input_digit == digit_sum):
            OK = True

def is_string(param):
    return (param == str(param))

"Functions for writing in the password shuttle."
def four_digit_shuffle(a, b, c, d):
    "Shuffles a quadruplet of four digits (or any four values passed as parameters, actually)."
    for i in range(6):
        if (random.randint(0, 1) == 1):
            b = a + b
            a = b - a
            b = b - a
        if (random.randint(0, 1) == 1):
            c = a + c
            a = c - a
            c = c - a
        if (random.randint(0, 1) == 1):
            d = a + d
            a = d - a
            d = d - a
        if (random.randint(0, 1) == 1):
            c = b + c
            b = c - b
            c = c - b
        if (random.randint(0, 1) == 1):
            d = b + d
            b = d - b
            d = d - b
        if (random.randint(0, 1) == 1):
            d = c + d
            c = d - c
            d = d - c
    return (a, b, c, d)

def one_digit_mask(dgt):
    """Given digit dgt, this function returns a quadruplet of four digits that somewhat covertly imply that digit.
    Here is how it works: There are five even digits and five odd digits. To mask an even digit, present the remaining
    four even digits in shuffled order. To mask an odd digit, present the remaining four odd digits in shuffled order."""
    a = (dgt + 2) % 10
    b = (dgt + 4) % 10
    c = (dgt + 6) % 10
    d = (dgt + 8) % 10
    return four_digit_shuffle(a, b, c, d)

def four_digit_mask(a, b, c, d):
    """Given a quadruplet of digits, returns a 16-tuple of digits that imply those four digits; but in a way that might not be immediately obvious:
    that is, in a way that might prevent their instantaneous, all-at-once apperception. How it works: The one_digit_mask of each digit is interleaved with the
    one_digit_mask's of the other three digits."""
    a_m = one_digit_mask(a)
    b_m = one_digit_mask(b)
    c_m = one_digit_mask(c)
    d_m = one_digit_mask(d)
    return (a_m[0], b_m[0], c_m[0], d_m[0], a_m[1], b_m[1], c_m[1], d_m[1], a_m[2], b_m[2], c_m[2], d_m[2], a_m[3], b_m[3], c_m[3], d_m[3])

def four_digit_mask_ST(a, b, c, d):
    "Wraps four_digit_mask in a string."
    a_string = str(four_digit_mask(a, b, c, d))
    return a_string

def Western_Arabic_to_Mro(a_string):
    "Replaces Western Arabic digits in a_string with their Mro digit equivalents."
    a_string = a_string.replace("0", "𖩠")
    a_string = a_string.replace("1", "𖩡")
    a_string = a_string.replace("2", "𖩢")
    a_string = a_string.replace("3", "𖩣")
    a_string = a_string.replace("4", "𖩤")
    a_string = a_string.replace("5", "𖩥")
    a_string = a_string.replace("6", "𖩦")
    a_string = a_string.replace("7", "𖩧")
    a_string = a_string.replace("8", "𖩨")
    a_string = a_string.replace("9", "𖩩")
    return a_string

def four_digit_mask_Mro_ST(a, b, c, d):
    "Encodes four (Western Arabic) digits into a string containing a 16-tuple of Mro digits."
    a_string = four_digit_mask_ST(a, b, c, d)
    a_string = Western_Arabic_to_Mro(a_string)
    return a_string

def DEBUG(flag_BL, msg_ST):
    "Prints msg_ST only if flag_BL is True."
    if flag_BL:
        print(msg_ST)

    
"BEGIN"
numbers = [0, 0, 0, 0]
answer = ""
errorFlag = False
errorType = 0
debug_0 = False
while not (answer in ['y', 'n']):
    answer = input("Load (y/n)? ")
if (answer == "y"):
    filename_OK = False
    while not filename_OK:
        filename = input("Enter filename: ")        
        if (len(filename) < 6) or not (filename[-5:] == ".4L4D"):
            print("Error: The filename's extension should be .4L4D.")
        else:
            filename_OK = True
    with open(filename) as thefile:
        i = -5
        for fileline in thefile:
            fileline = fileline.rstrip('\n')
            if (i <= -1):
                print(fileline)
            elif (i <= 3):
                numbers[i] = int(fileline[14:])
            else:
                print(fileline)
                if (fileline == "Program: FourLines2FourDigits_7.py"):
                    print("Python program and file match.\n")
                else:
                    print("Error: Python program and file DO NOT match.\n")
                    errorFlag = True
                    quit()
            i += 1

lines = ["", "", "", ""]
digits = [-1, -1, -1, -1]

for i in range(4):
    j = i + 1
    input_string = input("Enter line " + str(j) + ": ")
    lines[i] = input_string
    thehash = string_hash_9(lines[i])
    print("line " + str(j) + ": " + str(thehash))
    if (answer == "n"):
        numbers[i] = thehash
    elif (answer == "y"):
        if (thehash == numbers[i]):
            print("Line " + str(j) + " has the expected hash.")
        else:
            print("Line " + str(j) + " has the wrong hash.")
            errorFlag = True
            errorType = 1
            break
    digits[i] = string_hash_6(lines[i]) % 10

"Check the digits for redundancies."
if (digits[0] == digits[1]):
    print("ERROR: Digits 0 and 1 are the same.")
    errorFlag = True
    errorType = 2
    DEBUG(debug_0, f"L211. digits[0] = {digits[0]}; digits[1] = {digits[1]}")

if (digits[0] == digits[2]):
    print("ERROR: Digits 0 and 2 are the same.")
    errorFlag = True
    errorType = 2
    DEBUG(debug_0, f"L216. digits[0] = {digits[0]}; digits[2] = {digits[2]}")

if (digits[0] == digits[3]):
    print("ERROR: Digits 0 and 3 are the same.")
    errorFlag = True
    errorType = 2
    DEBUG(debug_0, f"L221. digits[0] = {digits[0]}; digits[3] = {digits[3]}")

if (digits[1] == digits[2]):
    print("ERROR: Digits 1 and 2 are the same.")
    errorFlag = True
    errorType = 2
    DEBUG(debug_0, f"L226. digits[1] = {digits[1]}; digits[2] = {digits[2]}")

if (digits[1] == digits[3]):
    print("ERROR: Digits 1 and 3 are the same.")
    errorFlag = True
    errorType = 2
    DEBUG(debug_0, f"L231. digits[1] = {digits[1]}; digits[3] = {digits[3]}")

if (digits[2] == digits[3]):
    print("ERROR: Digits 2 and 3 are the same.")
    errorFlag = True
    errorType = 2
    DEBUG(debug_0, f"L236. digits[2] = {digits[2]}; digits[3] = {digits[3]}")

if not errorFlag:
    print("The digits are OK (i.e., all different from each other).")
elif (errorType == 2):
    print("Error: The digits are not OK. (At least two digits are equal to each other.)")
    quit()
elif (errorType == 1):
    print("Error: Some line was not entered correctly.")
    quit()


if (not errorFlag) and (answer == "y"):
    output_mode = ""
    while not (output_mode in ['t', 's']):
        output_mode = input("Camouflage trellis (t) or password shuttle (s)? ")

if (not errorFlag) and (answer == "y") and (output_mode == "t"):
    print("\nCAMOUFLAGE TRELLIS")
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
        if (contanswer == "n"):
            cont = False
        else:
            print("\n\n\n\n")

if (not errorFlag) and (answer == "y") and (output_mode == "s"):
    shuttle_position = 0
    while not (shuttle_position in ['1', '2']):
        shuttle_position = input("What position: 1 or 2? ")
    if (shuttle_position == "1"):
        file_1 = open("shuttle_2.txt", "w")
        file_1.write(four_digit_mask_Mro_ST(digits[0], digits[1], digits[2], digits[3]) + "\n")
        file_1.close()
        print("The password has been written into the shuttle's first position.")
    elif (shuttle_position == "2"):
        file_1 = open("shuttle.txt", "a")
        file_1.write(four_digit_mask_Mro_ST(digits[0], digits[1], digits[2], digits[3]))
        file_1.close()
        print("The password has been written into the shuttle's second position.")
        
if (answer == "n") and (not errorFlag):
    saveanswer = ""
    while not (saveanswer in ["y", "n"]):
        saveanswer = input("Save (y/n)?")
    if (saveanswer == "y"):
        newfilename_OK = False
        while not newfilename_OK:
            newfilename = input("Enter filename: ")
            if (len(newfilename) < 6) or not (newfilename[-5:] == ".4L4D"):
                print("Error: The filename should have extension .4L4D.")
            else:
                newfilename_OK = True
        "save data in file"
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
            newfile.write("Program: FourLines2FourDigits_7.py")
        print("New file has been written. Reconstruct the password in order to confirm it.")
        print("Do not assign the password until it has been confirmed.")
        print("\nMETADATA")
        print("Filename: " + newfilename)
        print("Executor: FourLines2FourDigits_7.py")
        print("Book's name: " + bookname)
        print("Book's author: " + author)
        print("Books' publisher: " + publisher)
        print("Book's location: " + library)
        print("Password's page number: " + pagenumber + "\n")
elif (not errorFlag) and (answer == "y") and (output_mode == "t"):
    print("Close this window down when ending the session.\n")
    print("Also play some mind-clearing game.")

if (not errorFlag) and (answer == "y"):
    "log"
    antwoord_CH = ""
    while not (antwoord_CH in ["y", "n"]):
        antwoord_CH = input("\nWould you like this reconstruction episode to be logged (y/n)? ")
    if (antwoord_CH == "y"):
        "append entry in password_construction_log.txt"
        with open("password_construction_log.txt", "a") as fil_chron:
            fil_chron.write("- - - - - - - - - - - - - - - -\n")
            todays_date = date.today()
            fil_chron.write(f"Today's date: {todays_date}\n")
            fil_chron.write(f"Reconstructed: {newfilename}\n")
            if (output_mode == "t"):
                fil_chron.write("Output mode: trellis\n")
            elif (output_mode == "s"):
                fil_chron.write(f"Output mode: shuttle, #{shuttle_position}\n")
        print("A brief mention has been written in password_construction_log.txt.")      
elif (not errorFlag) and (answer == "n") and (saveanswer == "y"):
    "log"
    antwoord_CH = ""
    while not (antwoord_CH in ["y", "n"]):
        antwoord_CH = input("\nWould you like this 'creating new' session to be logged (y/n)? ")
    if (antwoord_CH == "y"):
        "append entry in password_construction_log.txt"
        with open("password_construction_log.txt", "a") as fil_chron:
            fil_chron.write("- - - - - - - - - - - - - - - -\n")
            todays_date = date.today()
            fil_chron.write(f"Today's date: {todays_date}\n")
            fil_chron.write(f"Created new: {newfilename}\n")             
        print("A brief mention has been written in password_construction_log.txt.")
"FINIS PROGRAMMAE"
