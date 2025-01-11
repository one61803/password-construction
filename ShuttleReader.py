"This file is called ShuttleReader.py."
import random


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
        else:
            print("Error: incorrect buffer digit; try again.")

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

def camouflage_trellis(title):
    print(title)
    print("Add each row of digits modulo 10 mentally in order to obtain each digit.")
    print("Rows that end in question mark are buffers, but their sum must be input before")
    print("moving on to the next line.\n")
    cont = True    # default
    while cont:
        print("The four digits are (add):\n")
        buffer_digit()
        for i in range(4):
            digit_mask(digits[i])
            buffer_digit()
        contanswer = ""        # continue answer = answer about continuation
        while not (contanswer in ['y', 'n']):
            contanswer = input("Another (y/n)? ")
        if contanswer == "n":
            cont = False
        else:
            print("\n\n\n\n")    

def digit_Kannada_to_Western_Arabic(digit_CH):
    decuplet_LS = ['೦', '೧', '೨', '೩', '೪', '೫', '೬', '೭', '೮', '೯']
    index_NT = 0
    found_TF = False
    while not found_TF:
        if (digit_CH == decuplet_LS[index_NT]):
            found_TF = True
        else:
            index_NT += 1
        if index_NT > 10:
            print("L71. ERROR in digit_Kannada_to_Western_Arabic: The given parameter is not a Kannada character.")
    return str(index_NT)

def is_string(param):
    return (param == str(param))

def decode_from_Kannada(a_string):
    new_string = ""
    if is_string(a_string):
        if (len(a_string) == 4):
            for i in range(4):
                a_char = a_string[i]
                new_string += digit_Kannada_to_Western_Arabic(a_char)
            return new_string
        else:
            print("L86. ERROR in decode_from_Kannada: The parameter should have four characters.")
    else:
        print("L88. ERROR in decode_from_Kannada: The parameter should be a string.")
        
"BEGIN"
file = open("shuttle.txt", "r")
line_1 = decode_from_Kannada(file.readline()[0:4])
line_2 = decode_from_Kannada(file.readline())
file.close()

digits = [-1, -1, -1, -1]

"First password."
digits[0] = int(line_1[0])
digits[1] = int(line_1[1])
digits[2] = int(line_1[2])
digits[3] = int(line_1[3])

camouflage_trellis("\nCAMOUFLAGE TRELLIS FOR THE FIRST PASSWORD")

"Second password."
digits[0] = int(line_2[0])
digits[1] = int(line_2[1])
digits[2] = int(line_2[2])
digits[3] = int(line_2[3])

camouflage_trellis("\nCAMOUFLAGE TRELLIS FOR THE SECOND PASSWORD")

file = open("shuttle.txt", "w")
file.write("XXXXXXXX\n")
file.write("ZZZZZZZZ")      # Should this line end in '\n'? Ans.: Not needed, apparently.
file.close()

print("DONE")
"END"
