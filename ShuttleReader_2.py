"This file is called ShuttleReader_2.py."
"It was forked from ShuttleReader.py."
"Objective of this version: a new way of storing four-digit passwords in the shuttle."
import random


def buffer_digit():
    """Prompts the user with a string of 16 random digits and a question mark, asking for the sum modulo 10 of those digits,
    and re-prompting if the answer is wrong."""
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
    """Writes a line of 16 digits whose sum modulo 10 equals argument digit. (The first 15 are random and the last one
    is compensating in order for the sum to equal the target digit.)"""
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
    """Presents a camouflage trellis for the four-tuple of digits in global variable digit. String argument title 
    is the headline of the brief intro."""
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

def is_string(param):
    "Returns a Boolean of whether argument param is a string or not."
    return (param == str(param))

def Mro_to_Western_Arabic(a_string):
    "Replaces Mro digits in a_string to their equivalent Western Arabic digits."
    a_string = a_string.replace("𖩠", "0")
    a_string = a_string.replace("𖩡", "1")
    a_string = a_string.replace("𖩢", "2")
    a_string = a_string.replace("𖩣", "3")
    a_string = a_string.replace("𖩤", "4")
    a_string = a_string.replace("𖩥", "5")
    a_string = a_string.replace("𖩦", "6")
    a_string = a_string.replace("𖩧", "7")
    a_string = a_string.replace("𖩨", "8")
    a_string = a_string.replace("𖩩", "9")
    return a_string

def string_to_16_tuple(a_string):
    """Converts a 16-tuple captured in string a_string into an actual (Pythonian) 16-tuple.
    The components have to be digits (or integers, at least)."""
    if (a_string[0] == "(") and (a_string[-1] == ")"):
        a_string = a_string[1:-1]
        a_string = a_string.replace(" ", "")
        char_LS = a_string.split(",")
        if len(char_LS) == 16:
            comp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(16):
                comp[i] = int(char_LS[i])
            return (comp[0], comp[1], comp[2], comp[3], comp[4], comp[5], comp[6], comp[7], comp[8], comp[9], comp[10], comp[11], comp[12], comp[13], comp[14], comp[15])
        else:
            print("L100. ERROR in string_to_16_tuple: The tuple in a_string should have 16 components.")
    else:
        print("L102. ERROR in string_to_16_tuple: a_string should be wrapped in parentheses.")
        DEBUG(debug_0, f"a_string = {a_string}")
        DEBUG(debug_0, f"a_string[-1] = {a_string[-1]}")
        DEBUG(debug_0, f"a_string[-2] = {a_string[-2]}")

def one_digit_unmask(a, b, c, d):
    "The inverse of one_digit_mask in, e.g., FourHundredWords2FourDigits_8.py."
    dgt_LS = [a, (a + 2) % 10, (a + 4) % 10, (a + 6) % 10, (a + 8) % 10]
    dgt_LS.remove(a)
    dgt_LS.remove(b)
    dgt_LS.remove(c)
    dgt_LS.remove(d)
    return dgt_LS[0]

def four_digit_unmask(sixteen_tuple):
    "The inverse of four_digit_mask in, e.g., FourHundredWords2FourDigits_8.py."
    a = one_digit_unmask(sixteen_tuple[0], sixteen_tuple[4], sixteen_tuple[8], sixteen_tuple[12])
    b = one_digit_unmask(sixteen_tuple[1], sixteen_tuple[5], sixteen_tuple[9], sixteen_tuple[13])
    c = one_digit_unmask(sixteen_tuple[2], sixteen_tuple[6], sixteen_tuple[10], sixteen_tuple[14])
    d = one_digit_unmask(sixteen_tuple[3], sixteen_tuple[7], sixteen_tuple[11], sixteen_tuple[15])
    return (a, b, c, d)

def string_to_four_tuple(a_string):
    "Composition of string_to_16_tuple and four_digit_unmask."
    sixteen_tuple = string_to_16_tuple(a_string)
    return four_digit_unmask(sixteen_tuple)

def four_digit_unmask_Mro(a_string):
    "Composition of Mro_to_Western_Arabic and string_to_four_tuple."
    a_string = Mro_to_Western_Arabic(a_string)
    four_tuple = string_to_four_tuple(a_string)
    return four_tuple

def DEBUG(flag, msg):
    "Showing of message in string msg conditioned on content of Boolean flag, for purpose of debugging."
    if flag:
        print(msg)
        
"BEGIN"
debug_0 = False
file = open("shuttle_2.txt", "r")
four_tuple_1 = four_digit_unmask_Mro(file.readline()[0:-1])
four_tuple_2 = four_digit_unmask_Mro(file.readline())
file.close()

digits = [-1, -1, -1, -1]

"First password."
digits = four_tuple_1

camouflage_trellis("\nCAMOUFLAGE TRELLIS FOR THE FIRST PASSWORD")

"Second password."
digits = four_tuple_2

camouflage_trellis("\nCAMOUFLAGE TRELLIS FOR THE SECOND PASSWORD")

file = open("shuttle_2.txt", "w")
file.write("XXXXXXXX\n")
file.write("ZZZZZZZZ")      # Should this line end in '\n'? Ans.: Not needed, apparently.
file.close()

print("DONE")
"END"
