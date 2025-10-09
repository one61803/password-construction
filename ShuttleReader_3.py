"This file is called ShuttleReader_3.py."
"It was forked from ShuttleReader_2.py."
"123456789A123456789B123456789C123456789D123456789E123456789F123456789G123456789H123456789I123456789J123456789K123456789L"
"Right margin set at I3."
import random
from datetime import date

def buffer_digit():
    """Prompts the user with a string of 16 random digits and a question mark, asking for
    the sum modulo 10 of those digits, and re-prompting if the answer is wrong."""
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
        input_digit = input_integer(digit_string)
        if (input_digit == digit_sum):
            OK = True
        else:
            print("Error: incorrect buffer digit; try again.")

def input_integer(message_ST):
    """Inputs an integer. The return value is an actual integer, not a string containing
    an integer."""
    integer_ST = "ABC"
    while not is_string_an_integer(integer_ST):
        integer_ST = input(message_ST)
        if not is_string_an_integer(integer_ST):
            print("The input should be an integer. Please try again.\n")
    return int(integer_ST)

def is_string_an_integer(ST):
    "Checks whether string ST contains an integer."
    if (len(ST) == 0):
        return False
    else:
        if (ST[0] == "-"):
            ST = ST[1:]
    return ST.isdigit()

def digit_mask(digit):
    """Writes a line of 16 digits whose sum modulo 10 equals argument digit. (The first
    15 are random and the last one is compensating in order for the sum to equal the
    target digit.)"""
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

def camouflage_trellis(title_ST, digits_AR):
    "Outputs the four digits in a masked way, so that the user cannot (or should not) \
     perceive them all at once."
    print(title_ST)
    print("Add each row of digits module 10 mentally in order to obtain each digit.")
    print("Rows that end in question mark are buffers, but their sum must be input before")
    print("moving on to the next line.\n")
    print("The four digits are (add):\n")
    buffer_digit()
    for i in range(4):
        digit_mask(digits_AR[i])
        buffer_digit()

def camouflage_trellis_modulator(title_ST, how_many_NT, digits_AR):
    "Modulates camouflage trellis based on the value of the how_many_NT argument."
    out_ST = "Is this reconstruction session for newly assigning (ss) the given"
    out_ST += "\npassword (to some domain) or for accessing (cc) a password's"
    out_ST += "\n(already assigned) domain (ss/cc)? "
    if (how_many_NT == 2):
        cont = True
        while cont:
            print("Just ahead: camouflage trellis A.\n")
            camouflage_trellis(title_ST, digits_AR)
            print("Just ahead: camouflage trellis B.\n")
            camouflage_trellis(title_ST, digits_AR)
            cont = whether_to_continue()     
    elif (how_many_NT == 1):
        cont = True
        while cont:
            print("Just ahead: a single camouflage trellis.\n")
            camouflage_trellis(title_ST, digits_AR)
            cont = whether_to_continue()

def whether_to_continue():
    "Asks user whether to continue and returns a boolean based on that."
    continue_answer = input_y_or_n("Another (y/n)? ")
    if (continue_answer == "n"):
        return False
    elif (continue_answer == "y"):
        print("\n\n\n\n")
        return True

def input_y_or_n(message_ST):
    "Asks for a 'y' or 'n' input and loops until it gets a proper answer."
    ans_CH = ""
    while not (ans_CH in ["y", "n"]):
        ans_CH = input(message_ST)
        if not (ans_CH in ["y", "n"]):
            print("Error. Please answer with either 'y' or 'n'.\n")
    return ans_CH

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
            return (comp[0], comp[1], comp[2], comp[3], comp[4], comp[5], comp[6], \
                    comp[7], comp[8], comp[9], comp[10], comp[11], comp[12], comp[13], \
                    comp[14], comp[15])
        else:
            out_ST = "L102. ERROR in string_to_16_tuple: The tuple in a_string should have"
            out_ST += " 16 components."
            print(out_ST)
    else:
        out_ST = "L102. ERROR in string_to_16_tuple: a_string should be wrapped in "
        out_ST += "parentheses."
        print(out_ST)
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
    a = one_digit_unmask(sixteen_tuple[0], sixteen_tuple[4], sixteen_tuple[8], \
                         sixteen_tuple[12])
    b = one_digit_unmask(sixteen_tuple[1], sixteen_tuple[5], sixteen_tuple[9], \
                         sixteen_tuple[13])
    c = one_digit_unmask(sixteen_tuple[2], sixteen_tuple[6], sixteen_tuple[10], \
                         sixteen_tuple[14])
    d = one_digit_unmask(sixteen_tuple[3], sixteen_tuple[7], sixteen_tuple[11], \
                         sixteen_tuple[15])
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
    "Showing of message in string msg conditioned on content of Boolean flag, for "
    "purpose of debugging."
    if flag:
        print(msg)
        
"BEGIN"
debug_0 = False
is_toy_version = False
is_trial_version = True
if is_toy_version and is_trial_version:
    print("L205. ERROR: is_toy_version and is_trial_version should not")
    print("both be set to True.")
    quit()
if is_toy_version:
    what_log = "toy_password_construction_log.txt"
elif is_trial_version:
    what_log = "trial_password_construction_log.txt"
else:
    what_log = "password_construction_log.txt"
    
file = open("shuttle_3.txt", "r")
four_tuple_1 = four_digit_unmask_Mro(file.readline()[0:-1])
four_tuple_2 = four_digit_unmask_Mro(file.readline())
file.close()

digits = [-1, -1, -1, -1]

"First password."
digits = four_tuple_1

camouflage_trellis_modulator("\nCAMOUFLAGE TRELLIS FOR THE FIRST PASSWORD", 1, digits)

"Second password."
digits = four_tuple_2

camouflage_trellis_modulator("\nCAMOUFLAGE TRELLIS FOR THE SECOND PASSWORD", 2, digits)

file = open("shuttle_3.txt", "w")
file.write("XXXXXXXX\n")
file.write("ZZZZZZZZ")      # Should this line end in '\n'? Ans.: Not needed, apparently.
file.close()

"log?"
antwoord_CH = input_y_or_n("\nWould you like this shuttle session to be logged? (y/n)? ")
if (antwoord_CH == "y"):
    "append entry in log"
    with open(what_log, "a") as fil_chron:
        fil_chron.write("- - - - - - - - - - - - - - - -\n")
        todays_date = date.today()
        fil_chron.write(f"Today's date: {todays_date}\n")
        fil_chron.write(f"Shuttle session.\n")
    print(f"A record has been written in {what_log}.\n")

print("DONE")
"FINIS PROGRAMMATIS · FINIS PROGRAMMATIS · FINIS PROGRAMMATIS · FINIS PROGRAMMATIS · FINIS PRO"
