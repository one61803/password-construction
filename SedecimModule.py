
"""Variable type markers:
 CH : character
 ST : string
 NT : integer
 FL : float
 IS : Boolean
 BL : Boolean
 LSNT : list of integers
 LSST : list of strings
 DC : dictionary (associative array)
 RC : record, i.e., list of elements with different types
 DB : database, i.e., list of records
 FILE : file."""

def code(CH):
    "A=1, B=2, ..., Z=26"
    return ord(CH) - 64

def transnumeration(word_ST):
    "Convert an 8-string of capital letters to an 8-list numbers (each one from 1 to 26)." 
    lst_LSNT = []
    for i_NT in range(len(word_ST)):
        CH = word_ST[i_NT]
        lst_LSNT.append(code(CH))
    if len(lst_LSNT) == 8:
        return lst_LSNT
    else:
        print("ERROR in transnumeration.")

def bubble_sort_sub_A(num_LSNT):
    new_LSNT = []
    new_LSNT.append(min(num_LSNT[0], num_LSNT[1]))
    new_LSNT.append(max(num_LSNT[0], num_LSNT[1]))
    new_LSNT.append(min(num_LSNT[2], num_LSNT[3]))
    new_LSNT.append(max(num_LSNT[2], num_LSNT[3]))
    new_LSNT.append(min(num_LSNT[4], num_LSNT[5]))
    new_LSNT.append(max(num_LSNT[4], num_LSNT[5]))
    new_LSNT.append(min(num_LSNT[6], num_LSNT[7]))
    new_LSNT.append(max(num_LSNT[6], num_LSNT[7]))
    return new_LSNT

def bubble_sort_sub_B(num_LSNT):
    new_LSNT = []
    new_LSNT.append(num_ls[0])
    new_LSNT.append(min(num_LSNT[1], num_LSNT[2]))
    new_LSNT.append(max(num_LSNT[1], num_LSNT[2]))
    new_LSNT.append(min(num_LSNT[3], num_LSNT[4]))
    new_LSNT.append(max(num_LSNT[3], num_LSNT[4]))
    new_LSNT.append(min(num_LSNT[5], num_LSNT[6]))
    new_LSNT.append(max(num_LSNT[5], num_LSNT[6]))
    new_LSNT.append(num_LSNT[7])
    return new_LSNT

def bubble_sort(num_LSNT):
    "Bubble sort 8-list of integers into increasing order."
    new_LSNT = bubble_sort_sub_A(num_LSNT)   # 0 to 1
    new_LSNT = bubble_sort_sub_B(new_LSNT)   # 1 to 2
    new_LSNT = bubble_sort_sub_A(new_LSNT)   # 2 to 3
    new_LSNT = bubble_sort_sub_B(new_LSNT)   # 3 to 4
    new_LSNT = bubble_sort_sub_A(new_LSNT)   # 4 to 5
    new_LSNT = bubble_sort_sub_B(new_LSNT)   # 5 to 6
    new_LSNT = bubble_sort_sub_A(new_LSNT)   # 6 to 7
    return new_LSNT

def mod(num_NT):
    "Returns a number between 1 and 26 (inclusive) that is equivalent (modulo 26) to num_NT."
    new_num_NT = num_NT
    if num_NT == 0:
        return 26
    elif num_NT > 0:
        while new_num_NT > 26:
            new_num_NT = new_num_NT - 26
        return new_num_NT
    elif num_NT < 0:
        print("ERROR in mod: argument num < 0")
    else:
        print("ERROR in mod: argument num is not a number.")

def vector_sum(word1_LSNT, word2_LSNT):
    "Adds two 8-lists of natural numbers component-wise modulo 26."
    new_word_LSNT = []
    for i_NT in range(len(word1_LSNT)):
        num1_NT = word1_LSNT[i_NT]
        num2_NT = word2_LSNT[i_NT]
        new_word_LSNT.append(mod(num1_NT + num2_NT))
    return new_word_LSNT

def transcharacterization(vector_LSNT):
    "Convert an 8-list of natural numbers into an 8-string of capital letters. This is the inverse of transnumeration."
    word_ST = ""
    for i_NT in range(len(vector_LSNT)):
        CH = chr(64 + vector_LSNT[i_NT])
        word_ST = word_ST + CH
    return word_ST

def vector_average(vec_LSNT):
    "Returns the average of an 8-list of natural numbers. The return value should be a float."
    sm_NT = 0
    if len(vec_LSNT) == 8:
        for i_NT in range(len(vec_LSNT)):
            sm_NT = sm_NT + vec_LSNT[i_NT]
        return sm_NT / 8
    else:
        print("ERROR in vector_average: argument vec_LS has length other than 8.")

def isproperword(word_ST):
    "Returns True if word_ST is an 8-string of capital letters."
    if word_ST.isalpha():
        if len(word_ST) == 8:
            return word_ST.isupper()
        else:
            return False
    else:
        return False

def phi_lett(vec_LSNT):
    "Returns a letter which is the modulo Z sum of the natural numbers in the 8-list vec_LSNT. First part of fingerprint/hash."
    sm_NT = 0
    for i_NT in range(len(vec_LSNT)):
        sm_NT = sm_NT + vec_LSNT[i_NT]
    return chr(64 + mod(sm_NT))

def phi_variance(vec_LSNT):
    "Returns the variance of an 8-list of natural numbers. Second part of fingerprint/hash of such an 8-list."
    sum_FL = 0
    mean_FL = vector_average(vec_LSNT)
    for i_NT in range(len(vec_LSNT)):
        summand_FL = (vec_LSNT[i_NT] - mean_FL)**2
        sum_FL += summand_FL
    return sum_FL / 8


def phi_ordnum(word_ST):
    "Returns the 'order number' of an 8-list of natural numbers. Third part of a fingerprint/hash of such an 8-list."
    if isproperword(word_ST):
        x1_BL = word_ST[1] > word_ST[0]
        x2_BL = word_ST[2] > word_ST[1]
        x3_BL = word_ST[3] > word_ST[2]
        x4_BL = word_ST[4] > word_ST[3]
        x5_BL = word_ST[5] > word_ST[4]
        x6_BL = word_ST[6] > word_ST[5]
        x7_BL = word_ST[7] > word_ST[6]
        x8_BL = word_ST[2:4] > word_ST[0:2]
        x9_BL = word_ST[4:6] > word_ST[2:4]
        x10_BL = word_ST[6:8] > word_ST[4:6]
        x11_BL = word_ST[4:8] > word_ST[0:4]
        num_NT = x1_BL + x2_BL*2 + x3_BL*4 + x4_BL*8 + x5_BL*16 + x6_BL*32 + x7_BL*64 + x8_BL*128 + x9_BL*256 * x10_BL*512 + x11_BL*1024
        return num_NT
    else:
        print("ERROR in phi_ordnum: argument word_ST is not a proper word.")

"functions that are subsidiary to VAL"
def is_string_a_float(ST):
    pair_LSST = ST.split('.')
    if len(pair_LSST) != 2:
        return False
    else:
        return pair_LSST[0].isdigit() and pair_LSST[1].isdigit()

def is_string_a_numeral(ST):
    return ST.isdigit() or is_string_a_float(ST)

digit_to_int_DC = {'1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '0' : 0}

def string_to_int(ST):
    "Converts a string containing a natural number into an integer."
    L_NT = len(ST)
    sigma_NT = 0
    for I_NT in range(1, L_NT + 1):
        digit_CH = ST[-I_NT]
        digit_NT = digit_to_int_DC[digit_CH]
        power_NT = 10 ** (I_NT - 1)
        sigma_NT += digit_NT * power_NT
    return sigma_NT

def string_to_fract(ST):
    "Converts, e.g., '123' to 0.123 . Return value is a float."
    I_NT = string_to_int(ST)
    L_NT = len(ST)
    return I_NT / 10 ** L_NT

def string_to_float(ST):
    "Converts a string containing a float into a float. (Assume that there is no exponential notation.)"
    pair_ST = ST.split('.')
    I_NT = string_to_int(pair_ST[0])
    F_FL = string_to_fract(pair_ST[1])
    return I_NT + F_FL

def VAL(ST):
    if is_string_a_float(ST):
        return string_to_float(ST)
    else:
        return string_to_int(ST)


"PROTO-MAIN"

data_DB = []
"LOAD?"
ans_CH = ""
while not (ans_CH in ['y', 'n']):
    ans_CH = input("Load (y/n)? ")
if ans_CH == "y":
    f_ST = input("Enter filename: ")
    with open(f_ST) as f_FILE:
        for line_ST in f_FILE:
            line_ST = line_ST.rstrip('\n')
            if (line_ST[0] == "(") and (line_ST[-1] == ")"):
                line_ST = line_ST[1:-1]
                line_LSST = line_ST.split(', ')
                if len(line_LSST) == 4:
                    a_CH = line_LSST[1][1]
                    a_NT = int(line_LSST[3])
                    a_FL = VAL(line_LSST[2])
                    data_DB.append((line_LSST[0], a_CH, a_FL, a_NT))
                elif len(line_LSST) == 6:
                    #"Zeroth line should have a three-element record."
                    "Zeroth line should have a six-element record."
                    print(f"line_ST = {line_ST}")
                    a_CH = line_LSST[0][1]
                    a_NT = int(line_LSST[2])
                    a_FL = VAL(line_LSST[1])
                    b_CH = line_LSST[3][1]
                    b_FL = VAL(line_LSST[4])
                    b_NT = int(line_LSST[5])
                    data_DB.append((a_CH, a_FL, a_NT, b_CH, b_FL, b_NT))
                else:
                    print("228. ERROR")
                    print(f"len(line_LSST) = {len(line_LSST)}")
                    print(f"line_LSST = {line_LSST}")
            else:
                print("230. ERROR")
    IS_loaded = True
    print("File has been loaded.")
else:
    IS_loaded = False


"MAIN"
#IS_toy_version = True          # This line is user-modifiable; the RHS should be either True or False.
Lis_LSST = []
if not IS_loaded:
    data_DB = [0]
old_word_ST = "ZZZZZZZZ"
old_vector_LSNT = transnumeration(old_word_ST)
#if IS_toy_version:
upper_bound_NT = 16
#else:
#    upper_bound_NT = 400
for i_NT in range(1, upper_bound_NT + 1):
    if not IS_loaded:
        loc_ST = input("\nInput location #" + str(i_NT) + ": ")
    else:
        print("\nLocation #" + str(i_NT) + ": " + data_DB[i_NT][0])
    IS_OK = False
    while not IS_OK:
        word_ST = ""
        while not isproperword(word_ST):
            word_ST = input("Word #" + str(i_NT) + ": ")
        if not IS_loaded:
            IS_OK = True
        else:
            vec_LSNT = transnumeration(word_ST)
            lett0_CH = phi_lett(vec_LSNT)
            variance0_FL = phi_variance(vec_LSNT)
            ordnum0_NT = phi_ordnum(word_ST)
            if (data_DB[i_NT][1] == lett0_CH) and (data_DB[i_NT][2] == variance0_FL) and (data_DB[i_NT][3] == ordnum0_NT):
                print("Fingerprint OK.")
                IS_OK = True
            else:
                print("Fingerprint not OK; try again.")
    "Append last-inputted word to list of words (Lis_LSST)."
    #vector_LS = transnumeration(word_ST)
    #vecsum_LS = vector_sum(old_vector_LS, vector_LS)
    #old_vector_LS = bubble_sort(vecsum_LS)
    Lis_LSST.append(word_ST)
    vector_LSNT = transnumeration(word_ST)
    "Fingerprint of last-inputted word."
    lett_CH = phi_lett(vector_LSNT)
    variance_FL = phi_variance(vector_LSNT)
    ordnum_NT = phi_ordnum(word_ST)
    print("phi_lett = " + lett_CH + "\nphi_variance = " + str(variance_FL) + "\nphi_ordnum = " + str(ordnum_NT))
    if not IS_loaded:
        data_DB.append((loc_ST, lett_CH, variance_FL, ordnum_NT))
"Extract new word from list of words (Lis_LSST)."
new_word_ST = ""
new_word_ST += Lis_LSST[0][1]
new_word_ST += Lis_LSST[1][3]
new_word_ST += Lis_LSST[2][5]
new_word_ST += Lis_LSST[3][7]
new_word_ST += Lis_LSST[4][1]
new_word_ST += Lis_LSST[5][3]
new_word_ST += Lis_LSST[6][5]
new_word_ST += Lis_LSST[7][7]
new_word_ST += Lis_LSST[8][0]
new_word_ST += Lis_LSST[9][2]
new_word_ST += Lis_LSST[10][4]
new_word_ST += Lis_LSST[11][6]
new_word_ST += Lis_LSST[12][0]
new_word_ST += Lis_LSST[13][2]
new_word_ST += Lis_LSST[14][4]
new_word_ST += Lis_LSST[15][6]
#"Now convert vecsum_LS back to word."
#output = transcharacterization(vecsum_LS)
output_ST = new_word_ST
left_ST = output_ST[:8]
right_ST = output_ST[8:]
#output_LSNT = transnumeration(output_ST)
left_LSNT = transnumeration(left_ST)
right_LSNT = transnumeration(right_ST)
print("\nOutput is " + output_ST)
a_lett_CH = phi_lett(left_LSNT)
a_variance_FL = phi_variance(left_LSNT)
a_ordnum_NT = phi_ordnum(left_ST)
b_lett_CH = phi_lett(right_LSNT)
b_variance_FL = phi_variance(right_LSNT)
b_ordnum_NT = phi_ordnum(right_ST)
print("Left phi_lett = " + a_lett_CH + "\nLeft phi_variance = " + str(a_variance_FL) + "\nLeft phi_ordnum = " + str(a_ordnum_NT))
print("Right phi_lett = " + b_lett_CH + "\nRight phi_variance = " + str(b_variance_FL) + "\nRight phi_ordnum = " + str(b_ordnum_NT))
if not IS_loaded:
    data_DB[0] = (a_lett_CH, a_variance_FL, a_ordnum_NT, b_lett_CH, b_variance_FL, b_ordnum_NT)
else:
    if (a_lett_CH == data_DB[0][0]) and (a_variance_FL == data_DB[0][1]) and (a_ordnum_NT == data_DB[0][2]):
        if (b_lett_CH == data_DB[0][3]) and (b_variance_FL == data_DB[0][4]) and (b_ordnum_NT == data_DB[0][5]):
            print("Output's fingerprint is OK.")
        else:
            print("Right side of output's fingerprint is not OK.")
    else:
        print("Left side of output's fingerprint is not OK.")

if not IS_loaded:
    ans_CH = ""
    while not ((ans_CH == "y") or (ans_CH == "n")):
        ans_CH = input("Save (y/n)?")
    if ans_CH == "y":
        f_ST = input("Enter filename: ")
        "Save data in filename."
        with open(f_ST, 'w') as f_FILE:
            for item_RC in data_DB:
                f_FILE.write(str(item_RC) + '\n')
        print("File written.")
            
        



