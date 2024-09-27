"Called VigintiModule_2.py"

"A filename (of a file processed by the program) should have extension .16A ."
"The output password has entropy 16*lg(62) = 95.3 ."

def neo_code(ch):
    "0=0, 1=1, ..., 9=9, A=10, B=11, ..., Y=34, Z=35, a=36, b=37, ..., y=60, z=61"
    if ((ord(ch) >= 48) and (ord(ch) <= 57)):
        return ord(ch) - 48
    elif ((ord(ch) >= 65) and (ord(ch) <= 90)):
        return ord(ch) - 55
    elif ((ord(ch) >= 97) and (ord(ch) <= 122)):
        return ord(ch) - 61
    else:
        print("15. ERROR")

def transnumeration(word_st):
    "Convert an 8-string of capital letters to an 8-list numbers (each one from 1 to 26)." 
    lst = []
    for i in range(len(word_st)):
        ch = word_st[i]
        lst.append(neo_code(ch))
    if len(lst) == 8:
        return lst
    else:
        print("26. ERROR in transnumeration.")

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
        print("ERROR in new_mod: argument num < 0")
    else:
        print("ERROR in new_mod: argument is not a number.")

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
        print("106. ERROR")

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

def isalphanumeric(char):
    if ((ord(char) >= 48) and (ord(char) <= 57)):
        return True
    elif ((ord(char) >= 65) and (ord(char) <= 90)):
        return True
    elif ((ord(char) >= 97) and (ord(char) <= 122)):
        return True
    else:
        return False

def isproperwordoid(word_ST):
    "Returns True if word_ST is an 8-string of alphanumerics."
    proper = True
    for i in range(len(word_ST)):
        if not isalphanumeric(word_ST[i]):
            proper = False
    return proper
        

def phi_lett(vec_LS):
    "Returns a letter which is the modulo Z sum of the natural numbers in the 8-list vec_LS. First part of fingerprint/hash."
    sm = 0
    for i in range(len(vec_LS)):
        sm = sm + vec_LS[i]
    #return chr(64 + mod(sm))
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
    if isproperwordoid(word_ST):
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
        print("205. ERROR in phi_ordnum: argument word_ST is not a proper wordoid.")

"functions that are subsidiary to VAL"
def is_string_a_float(st):
    pair = st.split('.')
    if len(pair) != 2:
        return False
    else:
        return pair[0].isdigit() and pair[1].isdigit()

def is_string_a_numeral(st):
    return st.isdigit() or is_string_a_float(st)

digit_to_int = {'1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '0' : 0}

def string_to_int(st):
    "Converts a string containing a natural number into an integer."
    L = len(st)
    sigma = 0
    for I in range(1, L+1):
        digit_st = st[-I]
        digit = digit_to_int[digit_st]
        power = 10 ** (I - 1)
        sigma += digit * power
    return sigma

def string_to_fract(st):
    "Converts, e.g., '123' to 0.123 ."
    I = string_to_int(st)
    L = len(st)
    return I / 10 ** L

def string_to_float(st):
    "Converts a string containing a float into a float. (Assume that there is no exponential notation.)"
    pair = st.split('.')
    I = string_to_int(pair[0])
    F = string_to_fract(pair[1])
    return I+F

def VAL(st):
    if is_string_a_float(st):
        return string_to_float(st)
    else:
        return string_to_int(st)


"PROTO-MAIN"

data = []
"LOAD?"
ans = ""
while not (ans in ['y', 'n']):
    ans = input("Load (y/n)? ")
if ans == "y":
    f_ST = input("Enter filename: ")
    if not (f_ST[-4:] == ".16A"):
        print("261. ERROR: Filename's extension should be .16A .")
        f_ST = ""
    with open(f_ST) as f:
        for line in f:
            line = line.rstrip('\n')
            if (line[0] == "(") and (line[-1] == ")"):
                line = line[1:-1]
                line_LS = line.split(', ')
                if len(line_LS) == 4:
                    line_LS[1] = line_LS[1][1]
                    line_LS[3] = int(line_LS[3])
                    line_LS[2] = VAL(line_LS[2])
                    data.append((line_LS[0], line_LS[1], line_LS[2], line_LS[3]))
                elif len(line_LS) == 6:
                    line_LS[0] = line_LS[0][1]
                    line_LS[1] = VAL(line_LS[1])
                    line_LS[2] = int(line_LS[2])
                    line_LS[3] = line_LS[3][1]
                    line_LS[4] = VAL(line_LS[4])
                    line_LS[5] = int(line_LS[5])
                    data.append((line_LS[0], line_LS[1], line_LS[2], line_LS[3], line_LS[4], line_LS[5]))
                elif len(line_LS) == 2:
                    if not (line_LS[0][1:10] == "Executor:"):
                        print("281. ERROR")
                    if not (line_LS[1][1:19] == "VigintiModule_2.py"):
                        print("283. ERROR: I am not the executor of this file.")
                    #data.append((line_LS[0], line_LS[1]))
                else:
                    print("280. len(line_LS) = " + str(len(line_LS)))
                    print("281. ERROR")
            else:
                print("286. ERROR ~ 210")
    is_loaded = True
    print("File has been loaded.")
else:
    is_loaded = False


"MAIN"
is_toy_version = False          # This line is user-modifiable; the RHS should be either True or False.
if not is_loaded:
    data = [0]
old_vector_left_LS = [0, 0, 0, 0, 0, 0, 0, 0]
old_vector_right_LS = [0, 0, 0, 0, 0, 0, 0, 0]
if is_toy_version:
    upper_bound = 10
else:
    upper_bound = 20
for i in range(1, upper_bound + 1):
    if not is_loaded:
        loc = input("\nInput location #" + str(i) + ": ")
    else:
        print("\nLocation #" + str(i) + ": " + data[i][0])
    OK = False
    while not OK:
        word_ST = ""
        while not isproperword(word_ST):
            word_ST = input("Word #" + str(i) + ": ")
        if not is_loaded:
            OK = True
        else:
            vec_LS = transnumeration(word_ST)
            lett0 = phi_lett(vec_LS)
            variance0 = phi_variance(vec_LS)
            ordnum0 = phi_ordnum(word_ST)
            if (data[i][1] == lett0) and (data[i][2] == variance0) and (data[i][3] == ordnum0):
                print("Fingerprint OK.")
                OK = True
            else:
                print("Fingerprint not ok; try again.")
    "Add to previous word."
    vector_LS = transnumeration(word_ST)
    vecsum_left_LS = vector_sum(old_vector_left_LS, vector_LS)
    old_vector_left_LS = left_rotate(vecsum_left_LS)
    vecsum_right_LS = vector_sum(old_vector_right_LS, vector_LS)
    old_vector_right_LS = right_rotate(vecsum_right_LS)
    "Fingerprint."
    lett = phi_lett(vector_LS)
    variance = phi_variance(vector_LS)
    ordnum = phi_ordnum(word_ST)
    print("phi_lett = " + lett + "\nphi_variance = " + str(variance) + "\nphi_ordnum = " + str(ordnum))
    if not is_loaded:
        data.append((loc, lett, variance, ordnum))
"Now convert vecsum_LS back to word."
output_left = transcharacterization(vecsum_left_LS)
output_right = transcharacterization(vecsum_right_LS)
if is_loaded:
    print("\noutput_left is " + output_left)
    print("\noutput_right is " + output_right)
    print("\nNet output is " + output_left + output_right)
lett_left = phi_lett(vecsum_left_LS)
variance_left = phi_variance(vecsum_left_LS)
ordnum_left = phi_ordnum(output_left)
if is_loaded:
    print("lett_left = " + lett_left + "\nvariance_left = " + str(variance_left) + "\nordnum_left = " + str(ordnum_left))
lett_right = phi_lett(vecsum_right_LS)
variance_right = phi_variance(vecsum_right_LS)
ordnum_right = phi_ordnum(output_right)
if is_loaded:
    print("lett_right = " + lett_right + "\nvariance_right = " + str(variance_right) + "\nordnum_right = " + str(ordnum_right))
if not is_loaded:
    data[0] = (lett_left, variance_left, ordnum_left, lett_right, variance_right, ordnum_right)
    "lett_left and lett_right probably match though."
else:
    if (lett_left == data[0][0]) and (variance_left == data[0][1]) and (ordnum_left == data[0][2]):
        if (lett_right == data[0][3]) and (variance_right == data[0][4]) and (ordnum_right == data[0][5]):
            print("Output's fingerprint is OK.")
        else:
            print("Output's right fingerprint is NOT OK.")
    else:
        print("Output's left fingerprint is NOT OK.")

if not is_loaded:
    ans_CH = ""
    while not ((ans_CH == "y") or (ans_CH == "n")):
        ans_CH = input("Save (y/n)?")
    if ans_CH == "y":
        data.append(("Executor:", "VigintiModule_2.py"))
        f_ST = input("Enter filename: ")
        "save data in filename"
        with open(f_ST, 'w') as f:
            for item in data:
                f.write(str(item) + '\n')
        print("File written.\n")
else:
    print("Close this window down when ending the session.")
        



