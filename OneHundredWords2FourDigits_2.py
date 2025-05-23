"This file is called OneHundredWords2FourDigits_2.py."
"It was forked from OneHundredWords2FourDigits.py."
import random
import time

"A filename (of a file processed by the program) should have extension .1H4D."
"The output password has entropy 4*lg(10) = 13.2."

"""SUMMARY OF PROGRAM'S ATTRIBUTES
Name: OneHundredWords2FourDigits_2.py
Extension of password constructing file: .1H4D
Input work level: 100 words
Output password entropy: 13.2 bits
Output information entropy: 12.3 shannons"""

def neo_code(ch):
    "0=0, 1=1, ..., 9=9, A=10, B=11, ..., Y=34, Z=35, a=36, b=37, ..., y=60, z=61"
    if ((ord(ch) >= 48) and (ord(ch) <= 57)):
        return ord(ch) - 48
    elif ((ord(ch) >= 65) and (ord(ch) <= 90)):
        return ord(ch) - 55
    elif ((ord(ch) >= 97) and (ord(ch) <= 122)):
        return ord(ch) - 61
    else:
        print("L25. ERROR in neo_code")

def transnumeration(word_st):
    "Convert an 8-string of capital letters to an 8-list numbers (each one from 1 to 26)." 
    lst = []
    for i in range(len(word_st)):
        ch = word_st[i]
        lst.append(neo_code(ch))
    if len(lst) == 8:
        return lst
    else:
        print("L36. ERROR in transnumeration.")

def left_rotate(num_ls):
    new_ls = []
    for i in [1, 2, 3, 4, 5, 6, 7]:
        new_ls.append(num_ls[i])
    new_ls.append(num_ls[0])
    return new_ls

def right_rotate(num_ls):
    new_ls = []
    new_ls.append(num_ls[7])
    for i in [0, 1, 2, 3, 4, 5, 6]:
        new_ls.append(num_ls[i])
    return new_ls

def neo_mod(num):
    "Returns a number between 0 and 61 (inclusive) that is equivalent (mod 62) to num."
    new_num = num
    if num >= 0:
        while new_num > 61:
            new_num = new_num - 62
        return new_num
    elif num < 0:
        print("L60. ERROR in neo_mod: argument num < 0")
    else:
        print("L62. ERROR in neo_mod: argument is not a number.")

def vector_sum(word1_LS, word2_LS):
    "Adds two 8-lists of natural numbers component-wise modulo 62."
    new_word_LS = []
    for i in range(len(word1_LS)):
        num1 = word1_LS[i]
        num2 = word2_LS[i]
        new_word_LS.append(neo_mod(num1 + num2))
    return new_word_LS

def to_char(num):
    if ((num >= 0) and (num <= 9)):
        return chr(48 + num)
    elif ((num >= 10) and (num <= 35)):
        return chr(55 + num)
    elif ((num >= 36) and (num <= 61)):
        return chr(61 + num)
    else:
        print("L81. ERROR in to_char")

def transcharacterization(vector_LS):
    "Convert an 8-list of natural numbers into an 8-string of alphanumerics. This is the inverse of transnumeration."
    word_ST = ""
    for i in range(len(vector_LS)):
        ch = to_char(vector_LS[i])
        word_ST = word_ST + ch
    return word_ST

def vector_average(vec_LS):
    "Returns the average of an 8-list of natural numbers."
    sm = 0
    if len(vec_LS) == 8:
        for i in range(len(vec_LS)):
            sm = sm + vec_LS[i]
        return sm / 8
    else:
        print("L99. ERROR in vector_average: argument vec_LS has length other than 8.")

def is_proper_keyword(word_ST):
    "Returns True if word_ST is an 8-string of capital letters."
    if word_ST.isalpha():
        if len(word_ST) == 8:
            return word_ST.isupper()
        else:
            return False
    else:
        return False

def is_proper_keywordoid(word_ST):
    "Returns True if word_ST is an 8-string of alphanumerics."
    proper = True
    for i in range(len(word_ST)):
        if not word_ST[i].isalnum():    
            proper = False
    return proper

def is_string(a_ST):
    return a_ST == str(a_ST)        

def phi_lett(vec_LS):
    "Returns a letter which is the modulo Z sum of the natural numbers in the 8-list vec_LS. First part of fingerprint/hash."
    sm = 0
    for i in range(len(vec_LS)):
        sm = sm + vec_LS[i]
    return to_char(neo_mod(sm))

def phi_variance(vec_LS):
    "Returns the variance of an 8-list of natural numbers. Second part of fingerprint/hash of such an 8-list."
    sm = 0
    mean = vector_average(vec_LS)
    for i in range(len(vec_LS)):
        summand = (vec_LS[i] - mean)**2
    return int(summand / 8.0 * 100000) / 100000

def phi_ordnum(word_ST):
    "Returns the 'order number' of an 8-list of natural numbers. Third part of a fingerprint/hash of such an 8-list."
    if is_proper_keywordoid(word_ST):
        x1 = word_ST[1] > word_ST[0]
        x2 = word_ST[2] > word_ST[1]
        x3 = word_ST[3] > word_ST[2]
        x4 = word_ST[4] > word_ST[3]
        x5 = word_ST[5] > word_ST[4]
        x6 = word_ST[6] > word_ST[5]
        x7 = word_ST[7] > word_ST[6]
        x8 = word_ST[2:4] > word_ST[0:2]
        x9 = word_ST[4:6] > word_ST[2:4]
        x10 = word_ST[6:8] > word_ST[4:6]
        x11 = word_ST[4:8] > word_ST[0:4]
        num = x1 + x2*2 + x3*4 + x4*8 + x5*16 + x6*32 + x7*64 + x8*128 + x9*256 * x10*512 + x11*1024
        return num
    else:
        print("L154. ERROR in phi_ordnum: argument word_ST is not a proper wordoid.")

"functions that are subsidiary to VAL"
def is_string_a_float(st):
    pair = st.split('.')
    if len(pair) != 2:
        return False
    else:
        return pair[0].isdigit() and pair[1].isdigit()

def is_string_a_numeral(st):
    return st.isdigit() or is_string_a_float(st)

def string_to_fract(st):
    "Converts, e.g., '123' to 0.123."
    I = int(st)
    L = len(st)
    return I / 10 ** L

def string_to_float(st):
    "Converts a string containing a float into a float. (Assume that there is no exponential notation.)"
    pair = st.split('.')
    I = int(pair[0])
    F = string_to_fract(pair[1])
    return I+F

def VAL(st):
    if is_string_a_float(st):
        return string_to_float(st)
    else:
        return int(st)

def string_hash_6(st):
    x = 31
    Z = 999983
    for i in range(len(st)):
        if (i == 0):
            accumulator = ord(st[0])
        else:
            accumulator = ((x * accumulator) + ord(st[i])) % Z
    return accumulator

def vector_hash_6(vector_LS):
    x = 31
    Z = 999983
    for i in range(16):
        if (i == 0):
            accumulator = vector_LS[0]
        else:
            accumulator = ((x * accumulator) + vector_LS[i]) % Z
    return accumulator

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

def stringify_tuple(a_tuple):
    a_string = "("
    for item in a_tuple:
        a_string += str(item)
        a_string += ";;"
    a_string = a_string[0:-2] + ")"
    return a_string

def swallow_number(a_string):
    digits_LS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while (len(a_string) > 0) and (a_string[0] in digits_LS):
        a_string = a_string[1:]
    return a_string

def if_page_then_swallow(a_string):
    digits_LS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if (a_string[0:3] == "P. ") and (a_string[3] in digits_LS):
        a_string = a_string[3:]
        a_string = swallow_number(a_string)
        if (len(a_string) > 0) and (a_string[0] == " "):
            a_string = a_string[1:]
        else:
            print("L262. ERROR in if_page_then_swallow: No space after the page number.")
            a_string = ""
    return a_string

def if_paragraph_then_swallow(a_string):
    digits_LS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if (a_string[0:5] == "PAR. ") and (a_string[5] in digits_LS):
        a_string = a_string[5:]
        a_string = swallow_number(a_string)
        if (len(a_string) > 0) and (a_string[0] == " "):
            a_string = a_string[1:]
        else:
            print("L274. ERROR in if_paragraph_then_swallow: No space after the paragraph number.")
            a_string = ""
    return a_string

def letter_count(a_string):
    a_string = if_page_then_swallow(a_string)
    a_string = if_paragraph_then_swallow(a_string)
    if is_eight_free(a_string):
        a_string = a_string.replace(" ", "")
        return len(a_string)
    else:
        return -9

def is_UALPHAnumeric(a_string):
    allowed_chars_LS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    allowed_chars_LS += ["A", "B", "C", "D", "E", "F", "G", "H", "Y"]
    allowed_chars_LS += ["I", "J", "K", "L", "M", "N", "O", "P", "Z"]
    allowed_chars_LS += ["Q", "R", "S", "T", "U", "V", "W", "X", " "]
    OK = True
    for i in range(len(a_string)):
        a_char = a_string[i]
        if not (a_char in allowed_chars_LS):
            OK = False
    return OK

def is_eight_free(a_string):
    a_list = a_string.split(" ")
    OK = True
    while len(a_list) > 0:
        extract = a_list[0]
        a_list = a_list[1:]
        if len(extract) == 8:
            OK = False
    return OK


"PRE-MAIN"

data = []
"LOAD?"
ans = ""
while not (ans in ['y', 'n']):
    ans = input("Load (y/n)? ")
if ans == "y":
    filename_OK = False
    while not filename_OK:
        f_ST = input("Enter filename: ")
        if (len(f_ST) < 6) or not (f_ST[-5:] == ".1H4D"):
            print("Error: The filename's extension should be .1H4D.")
        else:
            filename_OK = True
    with open(f_ST) as f:
        for line in f:
            line = line.rstrip('\n')
            if (line[0] == "(") and (line[-1] == ")"):
                line = line[1:-1]
                line_LS = line.split(';;')
                if len(line_LS) == 4:
                    line_LS[3] = int(line_LS[3])
                    line_LS[2] = VAL(line_LS[2])
                    data.append((line_LS[0], line_LS[1], line_LS[2], line_LS[3]))
                elif len(line_LS) == 2:
                    if not line_LS[0] in ["Executor:", "Book:", "Author:", "Publisher:", "Location:", "Codeword hash:"]:
                        print("L335. ERROR: Not an approved first element for an ordered pair.")
                    if (line_LS[0] == "Executor:") and (not line_LS[1] == "OneHundredWords2FourDigits_2.py"): 
                        print("L337. ERROR: I am not the executor of this file.")    
                    if line_LS[0] == "Book:":
                        the_book = line_LS[1]
                        print("Book: " + the_book + "\n")
                    elif line_LS[0] == "Author:":
                        the_author = line_LS[1]
                        print("Author: " + the_author + "\n")
                    elif line_LS[0] == "Publisher:":
                        the_publisher = line_LS[1]
                        print("Publisher: " + the_publisher + "\n")
                    elif line_LS[0] == "Location:":
                        the_location = line_LS[1]
                        print("Location: " + the_location + "\n")
                    elif line_LS[0] == "Codeword hash:":
                        the_codeword_hash = int(line_LS[1])
                        print("Codeword hash: " + str(the_codeword_hash) + "\n")
                    data.append((line_LS[0], line_LS[1]))                        
                else:
                    print("L355. len(line_LS) = " + str(len(line_LS)))
                    print("L356. ERROR")
            else:
                print("L358. ERROR: Line is not wrapped in parentheses.")
    is_loaded = True
    print("File has been loaded.")
else:
    is_loaded = False


"MAIN"
is_toy_version = False          # This line is user-modifiable; the RHS should be either True or False.
errorFlag = False
if not is_loaded:
    data = [0]
    keywords_LS = []
old_vector_left_LS = [0, 0, 0, 0, 0, 0, 0, 0]
old_vector_right_LS = [0, 0, 0, 0, 0, 0, 0, 0]
if is_toy_version:
    upper_bound = 12
else:
    upper_bound = 100
for i in range(1, upper_bound + 1):
    if not is_loaded:
        "not is_loaded"
        enter_loop_BL = True
        while enter_loop_BL:
            loc = input("\nInput location #" + str(i) + ": ")
            OK = False
            while not OK:
                word_ST = ""
                while not is_proper_keyword(word_ST):
                    word_ST = input("Keyword #" + str(i) + ": ")
                    if not is_proper_keyword(word_ST):
                        print("Error: Please enter an eight-letter word in all caps (or \"XXXXXXXX\" to cancel).")                    
                OK = True
            time.sleep(1)
            if (word_ST == "XXXXXXXX"):
                OK = True
                respuesta = "N"
            else:
                OK = False
            while not OK:
                respuesta = input("Is the index–keyword pair correct (Y/N)? ")
                if (respuesta in ["Y", "N"]):
                    OK = True
            if (respuesta == "Y"):
                enter_loop_BL = False
                if (word_ST in keywords_LS):
                    print("Please use a keyword that is different from any previous keyword.")
                    enter_loop_BL = True
                if not is_UALPHAnumeric(if_paragraph_then_swallow(if_page_then_swallow(loc)).replace(" ", "")):
                    print("Error: After (optionally) specifying the page number (through \"P. #\")")
                    print("and (optionally, and immediately afterwards) specifying the paragraph number")
                    print("(through \"PAR. #\"), the remainder of the location (i.e., index) string should")
                    print("consist only of spaces, digits, and uppercase letters. Please try again.")
                    enter_loop_BL = True                    
                if (letter_count(loc) < 6):
                    if (letter_count(loc) == -9):
                        print("No word in the index should have exactly eight letters. Please try again.")
                        enter_loop_BL = True
                    else:
                        print("Index word(s) should have at least six letters among them. Please try again.")
                        enter_loop_BL = True
        keywords_LS.append(word_ST)                
    elif is_loaded:
        "is_loaded"
        print("\nLocation #" + str(i) + ": " + data[i][0])
        OK = False
        while not OK:
            word_ST = ""
            while not is_proper_keyword(word_ST):
                word_ST = input("Keyword #" + str(i) + ": ")
                if not is_proper_keyword(word_ST):
                    print("Error: Please enter an eight-letter word in all caps.")                
            vec_LS = transnumeration(word_ST)
            lett0 = phi_lett(vec_LS)
            variance0 = phi_variance(vec_LS)
            ordnum0 = phi_ordnum(word_ST)
            if (data[i][1] == lett0) and (data[i][2] == variance0) and (data[i][3] == ordnum0):
                print("Fingerprint OK.")
                OK = True
            else:
                print("Fingerprint not ok; try again.")
    else:
        print("\nL440. ERROR: is_loaded should be Boolean.")
                
    "Add to previous word."
    vector_LS = transnumeration(word_ST)
    vecsum_left_LS = vector_sum(old_vector_left_LS, vector_LS)
    old_vector_left_LS = left_rotate(vecsum_left_LS)
    vecsum_right_LS = vector_sum(old_vector_right_LS, vector_LS)
    old_vector_right_LS = right_rotate(vecsum_right_LS)
    if i==25 or (is_toy_version and i==3):
        vecsum_left_25 = old_vector_left_LS
        vecsum_right_25 = old_vector_right_LS
        vecsum_total_25 = vecsum_left_25 + vecsum_right_25
    if i==50 or (is_toy_version and i==6):
        vecsum_left_50 = old_vector_left_LS
        vecsum_right_50 = old_vector_right_LS
        vecsum_total_50 = vecsum_left_50 + vecsum_right_50
    if i==75 or (is_toy_version and i==9):
        vecsum_left_75 = old_vector_left_LS
        vecsum_right_75 = old_vector_right_LS
        vecsum_total_75 = vecsum_left_75 + vecsum_right_75
    if i==100 or (is_toy_version and i==12):
        vecsum_left_100 = old_vector_left_LS
        vecsum_right_100 = old_vector_right_LS
        vecsum_total_100 = vecsum_left_100 + vecsum_right_100
    "Fingerprint."
    lett = phi_lett(vector_LS)
    variance = phi_variance(vector_LS)
    ordnum = phi_ordnum(word_ST)
    print("phi_lett = " + lett + "\nphi_variance = " + str(variance) + "\nphi_ordnum = " + str(ordnum))
    if not is_loaded:
        data.append((loc, lett, variance, ordnum))

"Extract single digits from the four sums."
digits = [-1, -1, -1, -1]
digits[0] = vector_hash_6(vecsum_total_25) % 10
digits[1] = vector_hash_6(vecsum_total_50) % 10
digits[2] = vector_hash_6(vecsum_total_75) % 10
digits[3] = vector_hash_6(vecsum_total_100) % 10

"Check the digits for redundancies."
if digits[0] == digits[1]:
    print("Error: Digits 0 and 1 are the same.")
    errorFlag = True

if digits[0] == digits[2]:
    print("Error: Digits 0 and 2 are the same.")
    errorFlag = True

if digits[0] == digits[3]:
    print("Error: Digits 0 and 3 are the same.")
    errorFlag = True

if digits[1] == digits[2]:
    print("Error: Digits 1 and 2 are the same.")
    errorFlag = True

if digits[1] == digits[3]:
    print("Error: Digits 1 and 3 are the same.")
    errorFlag = True

if digits[2] == digits[3]:
    print("Error: Digits 2 and 3 are the same.")
    errorFlag = True

if not errorFlag:
    print("\nThe digits are OK (i.e., all different from each other).\n")
    codeword_hash = string_hash_6(str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3]))

if (not errorFlag) and (is_loaded):
    print("CAMOUFLAGE TRELLIS")
    print("Add each row of digits module 10 mentally in order to obtain each digit.")
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

if not is_loaded:
    data[0] = ("Codeword hash:", codeword_hash)
else:
    if codeword_hash == the_codeword_hash:
        print("Output's fingerprint is OK.")
    else:
        print("L534. ERROR: Output's hash is NOT OK.")
        print("codeword_hash = " + str(codeword_hash))
        print("the_codeword_hash = " + str(the_codeword_hash))

if not is_loaded:
    ans_CH = ""
    while not ((ans_CH == "y") or (ans_CH == "n")):
        ans_CH = input("Save (y/n)?")
    if ans_CH == "y":
        data.append(("Executor:", "OneHundredWords2FourDigits_2.py"))
        a_book = input("What is the book's name? ")
        an_author = input("Who is the book's author? ")
        a_publisher = input("Who is the book's publisher? ")
        a_location = input("Where is the book usually located? ")
        data.append(("Book:", a_book))
        data.append(("Author:", an_author))
        data.append(("Publisher:", a_publisher))
        data.append(("Location:", a_location))
        filename_OK = False
        while not filename_OK:
            f_ST = input("Enter filename: ")
            if (len(f_ST) < 6) or not (f_ST[-5:] == ".1H4D"):
                print("Error: The filename should have extension .1H4D.")
            else:
                filename_OK = True
        "save data in filename"
        with open(f_ST, 'w') as f:
            for item in data:
                f.write(stringify_tuple(item) + '\n')
        print("The new file has been written. Reconstruct the password in order to confirm it.")
        print("Do not assign the password until it has been confirmed.\n")
        print("When assigning the password, it has to be entered twice. The first time from")
        print("one camouflage trellis; the second time from another camouflage trellis.\n")
        print("METADATA")
        print("Filename: " + f_ST)
        print("Executor: OneHundredWords2FourDigits_2.py")
        print("Book's name: " + a_book)
        print("Book's author: " + an_author)
        print("Books' publisher: " + a_publisher)
        print("Book's location: " + a_location)

else:
    print("Close this window down when ending the session.")
    print("If the password has just been assigned then record its metadata in")
    print("the log for the post to which the password has been assigned to guard.\n")    
    print("Also play some mind-clearing game or puzzle.")
