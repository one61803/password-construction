"This file is called TwoHundredWords2FourDigits_6.py."
"It was forked from TwoHundredWords2FourDigits_5.py and modified with the help of \
FourHundredWords2FourDigits_13.py."
"123456789A123456789B123456789C123456789D123456789E12345689F123456789G123456789H123456789I123456789J123456789K123456789L"
"Right margin set at I3."
import random
import time
from datetime import date
from array import *

"A filename (of a file processed by the program) should have extension .2H4D."
"The output password has password entropy 4*lg(10) = 13.2."
"The output password has information entropy lg(10*9*8*7) = 12.3 shannons."
"The output of shuttle output mode of this program can be read with ShuttleReader_2.py."

"""SUMMARY OF PROGRAM'S ATTRIBUTES
Name: TwoHundredWords2FourDigits_6.py
Extension of password constructing file: .2H4D
Input work level: 200 words
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
        print("L29. ERROR in neo_code")

def transnumeration(word_st):
    "Convert an 8-string of capital letters to an 8-list numbers (each one from 1 to 26)." 
    lst = []
    for i in range(len(word_st)):
        ch = word_st[i]
        lst.append(neo_code(ch))
    if len(lst) == 8:
        return lst
    else:
        print("L40. ERROR in transnumeration.")

def left_rotate(num_ls):
    "Leftward one-place cyclic permutation of a list of eight numbers."
    new_ls = []
    for i in [1, 2, 3, 4, 5, 6, 7]:
        new_ls.append(num_ls[i])
    new_ls.append(num_ls[0])
    return new_ls

def right_rotate(num_ls):
    "Rightward one-place cyclic permutation of a list of eight numbers."
    new_ls = []
    new_ls.append(num_ls[7])
    for i in [0, 1, 2, 3, 4, 5, 6]:
        new_ls.append(num_ls[i])
    return new_ls

def neo_mod(num):
    "Returns a number between 0 and 61 (inclusive) that is equivalent (mod 62) to num."
    new_num = num
    if (num >= 0):
        while (new_num > 61):
            new_num = new_num - 62
        return new_num
    elif (num < 0):
        print("L66. ERROR in neo_mod: argument num < 0")
    else:
        print("L68. ERROR in neo_mod: argument is not a number.")

def vector_sum(word1_LS, word2_LS):
    "Adds two 8-lists of natural numbers component-wise modulo 62."
    new_word_LS = []
    for i in range(len(word1_LS)):
        num1 = word1_LS[i]
        num2 = word2_LS[i]
        new_word_LS.append(neo_mod(num1 + num2))
    return new_word_LS

def to_char(num):
    "Converts a number from 0 to 61 amphi-inclusive into a character of three types:\
    (1) a digit, (2) an uppercase letter, (3) a lowercase letter. (The letters belong \
    to the English alphabet.)"
    if ((num >= 0) and (num <= 9)):
        return chr(48 + num)
    elif ((num >= 10) and (num <= 35)):
        return chr(55 + num)
    elif ((num >= 36) and (num <= 61)):
        return chr(61 + num)
    else:
        print("L89. ERROR in to_char.")

def transcharacterization(vector_LS):
    "Convert an 8-list of natural numbers into an 8-string of alphanumerics. \
     This is the inverse of transnumeration."
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
        print("L108. ERROR in vector_average: argument vec_LS has length other than 8.")

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

def phi_lett(vec_LS):
    "Returns a letter which is the modulo Z sum of the natural numbers in the 8-list \
     vec_LS. First part of fingerprint/hash."
    sm = 0
    for i in range(len(vec_LS)):
        sm = sm + vec_LS[i]
    return to_char(neo_mod(sm))

def phi_variance(vec_LS):
    "Returns the variance of an 8-list of natural numbers. \
     Second part of fingerprint/hash of such an 8-list."
    sm = 0
    mean = vector_average(vec_LS)
    for i in range(len(vec_LS)):
        summand = (vec_LS[i] - mean)**2
    return int(summand / 8.0 * 100000) / 100000

def phi_ordnum(word_ST):
    "Returns the 'order number' of an 8-list of natural numbers. \
     Third part of a fingerprint/hash of such an 8-list."
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
        num = x1 + x2*2 + x3*4 + x4*8 + x5*16 + x6*32 + x7*64 + x8*128 + x9*256 * x10*512 \
              + x11*1024
        return num
    else:
        print("L163. ERROR in phi_ordnum: argument word_ST is not a proper wordoid.")

"functions that are subsidiary to VAL"
def is_string_a_decimal(st):
    "Returns True if string st contains a decimal number: two natural numbers separated \
     by a period."
    if (st[0] == "-"):
        st = st[1:]
    pair = st.split('.')
    if (len(pair) != 2):
        return False
    else:
        return (pair[0].isdigit() or (pair[0] == '')) and pair[1].isdigit()

def is_string_a_numeral(st):
    "Returns True if the string contains a number."
    if (st[0] == "-"):
        st = st[1:]
    return st.isdigit() or is_string_a_decimal(st)

def string_to_fract(st):
    "Converts, e.g., '123' to 0.123."
    I = int(st)
    L = len(st)
    return I / 10 ** L

def string_decimal_to_number(st):
    "Converts a string containing a decimal number into that number. \
     (Assume that there is no exponential notation.)"
    pair = st.split('.')
    if (pair[0] == ""):
        pair[0] = "0"
    elif (pair[0] == "-"):
        pair[0] = "-0"
    I = int(pair[0])
    F = string_to_fract(pair[1])
    if (I >= 0):
        if (pair[0][0:2] == "-0"):
            return -F
        else:
            return I+F
    else:
        return -I-F

def VAL(st):
    "Converts a string containing a number into the number contained by that string. \
     (The name 'VAL' is borrowed from BASIC.)"
    if is_string_a_numeral(st):
        if is_string_a_decimal(st):
            return string_decimal_to_number(st)
        else:
            return int(st)
    else:
        print("L216. ERROR: string argument st should contain a number.")

def string_hash_6(st):
    "Calculates a hash for string st using a method similar to vector_hash_6."
    x = 31
    Z = 999983
    for i in range(len(st)):
        if (i == 0):
            accumulator = ord(st[0])
        else:
            accumulator = ((x * accumulator) + ord(st[i])) % Z
    return accumulator

def vector_hash_6(vector_LS):
    "Calculates a polynomial in x whose coefficients are components of vector_LS, \
     using Horner's method, for the purpose of providing a hash for a string which is \
     encoded in vector_LS." 
    x = 31
    Z = 999983
    for i in range(16):
        if (i == 0):
            accumulator = vector_LS[0]
        else:
            accumulator = ((x * accumulator) + vector_LS[i]) % Z
    return accumulator

def buffer_digit():
    "Prompts the user with a string of 16 random digits and a question mark, asking for \
     the sum modulo 10 of those digits, and re-prompting if the answer is wrong."
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
    "Writes a line of 16 digits whose sum modulo 10 equals parameter digit. \
     (The first 15 are random and the last one is compensating in order for the sum to \
     equal the target digit.)" 
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

def stringify_tuple(a_tuple):
    "Packages the data in a_tuple into a string that can be written into a file, \
     with double-semicolon separators and parenthetical boundaries."
    a_string = "("
    for item in a_tuple:
        a_string += str(item)
        a_string += ";;"
    a_string = a_string[0:-2] + ")"
    return a_string

def swallow_number(a_string):
    "Removes a number from the beginning of a_string."
    digits_LS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while (len(a_string) > 0) and (a_string[0] in digits_LS):
        a_string = a_string[1:]
    return a_string

def if_page_then_swallow(a_string):
    "Checks a_string to see if it starts with a page prefix and if it does, then removes it."
    digits_LS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if (a_string[0:3] == "P. ") and (a_string[3] in digits_LS):
        a_string = a_string[3:]
        a_string = swallow_number(a_string)
        if (len(a_string) > 0) and (a_string[0] == " "):
            a_string = a_string[1:]
        else:
            print("L307. ERROR in if_page_then_swallow: No space after the page number.")
            a_string = ""
    return a_string

def if_paragraph_then_swallow(a_string):
    "Checks a_string to see if it starts with a paragraph prefix and if it does, \
     then removes it."
    digits_LS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if (a_string[0:5] == "PAR. ") and (a_string[5] in digits_LS):
        a_string = a_string[5:]
        a_string = swallow_number(a_string)
        if (len(a_string) > 0) and (a_string[0] == " "):
            a_string = a_string[1:]
        else:
            print("L321. ERROR in if_paragraph_then_swallow: No space after the paragraph \
number.")
            a_string = ""
    return a_string

def letter_count(a_string):
    "Counts the quantity of alphanumbers in the latter (non-prefix, index-word) part of \
     a location string." 
    a_string = if_page_then_swallow(a_string)
    a_string = if_paragraph_then_swallow(a_string)
    if is_eight_free(a_string):
        a_string = a_string.replace(" ", "")
        return len(a_string)
    else:
        return -9

def index_word_count(loc_string):
    "Counts the number of index words (or numbers) in loc_string."
    loc_string = if_page_then_swallow(loc_string)
    loc_string = if_paragraph_then_swallow(loc_string)
    if (loc_string[-2:] == " S"):
        loc_string = loc_string[0:-2]
    while (loc_string.count(" S ") > 0):
        loc_string = loc_string.replace(" S ", " ")
    while (loc_string.count("  ") > 0):
        loc_string = loc_string.replace("  ", " ")
    words_LS = loc_string.split(" ")
    return len(words_LS)

def is_UALPHAnumeric(a_string):
    "Returns True if string a_string contains only uppercase alphanumbers."
    return a_string.isalnum() and (a_string == a_string.upper())

def is_eight_free(a_string):
    "Checks to see if any word in a string of words has eight-letters. If it does \
     then return False else return True."
    a_list = a_string.split(" ")
    OK = True
    while len(a_list) > 0:
        extract = a_list[0]
        a_list = a_list[1:]
        if len(extract) == 8:
            OK = False
    return OK

def pr_pa(a_string, opt):
    "'print pause': Prints string a_string, then pauses for five seconds if the Boolean \
     parameter opt is set to True. (The pause is skipped if opt is False.)"
    print(a_string)
    if opt:
        time.sleep(5)

def help_intro():
    "Introductory help scroll."
    page = 1
    been_there_already = []
    while (page > 0):
        match page:
            case 1:
                help_page_1(not (1 in been_there_already))
            case 2:
                help_page_2(not (2 in been_there_already))
            case 3:
                help_page_3(not (3 in been_there_already))
            case 4:
                help_page_4(not (4 in been_there_already))
            case 5:
                help_page_5(not (5 in been_there_already))
            case 6:
                help_page_6(not (6 in been_there_already))
            case 7:
                help_page_7(not (7 in been_there_already))
            case 8:
                help_page_8(not (8 in been_there_already))
            case 9:
                help_page_9(not (9 in been_there_already))
            case 10:
                help_page_10(not (10 in been_there_already))
            case 11:
                help_page_11(not (11 in been_there_already))
            case 12:
                help_page_12(not (12 in been_there_already))
            case 13:
                help_page_13(not (13 in been_there_already))
            case 14:
                help_page_14(not (14 in been_there_already))
            case 15:
                help_page_15(not (15 in been_there_already))
        been_there_already.append(page)
        cont = input("\nPress <ENTER> to continue or < and <ENTER> to go back one page \
or X and <ENTER> to\nexit the help scroll.")
        if (cont == "X"):
            page = 0
        elif (cont == "<"):
            page -= 1
        else:
            page += 1
            if (page > 15):
                page = 0

def help_page_1(opt):
    "help paragraph 1"
    pr_pa("\n(When entering a location string in “create new” mode:) periods should", opt)
    pr_pa("only be used to specify the page number (through \"P. {#} \") and the", opt)
    pr_pa("paragraph number (through \"PAR. {#} \"). If the page number is specified", opt)
    pr_pa("then it must be followed immediately by a specification of the paragraph", opt)
    pr_pa("number; and if the paragraph number is specified then it must be preceded", opt)
    pr_pa("immediately by a specification of the page number. The \"P. {#} PAR. {#} \"", opt)
    pr_pa("prefix is optional and what is being prefixed is the string of index words;", opt)
    pr_pa("if there is no such prefix then the index words appear by themselves. The", opt)
    pr_pa("index words as they appear in the book have to be converted to all caps and", opt)
    pr_pa("any punctuation among them other than spaces have to be stripped out.", opt)
    pr_pa("(Numbers may be included among the index words.) The index words are words", opt)
    pr_pa("that immediately precede the keyword; they \"point\" at the keyword, as it", opt)
    pr_pa("were.", opt)

def help_page_2(opt):
    "help paragraph 2"
    pr_pa("\nBy keyword is meant the fill-in-the-blank word, as it were. It must be", opt)
    pr_pa("exactly eight letters and converted to all caps regardless of its", opt)
    pr_pa("capitalization in the book. No word among the index words may be of exactly", opt)
    pr_pa("eight letters. The index words must include at least six letters among them.", opt)
    pr_pa("(There has to be at least one index word.) The index words have to have the", opt)
    pr_pa("same sequence that they have in the book, which is to say that no words", opt)
    pr_pa("among them may be skipped when being inputted into a location string. So if", opt)
    pr_pa("there is an eight-letter word among them that is required to be included in", opt)
    pr_pa("order to reach at least six letters then that index–keyword pair is", opt)
    pr_pa("invalidated and the user should skip past it and onto the next index–keyword", opt)
    pr_pa("pair in the book.", opt)
        
def help_page_3(opt):
    "help paragraph 3"
    pr_pa("\nWhen \"mining\" a given paragraph in the book for index–keyword pairs,", opt)
    pr_pa("such pairs should be input sequentially in the same order that they would ", opt)
    pr_pa("appear from reading that paragraph normally (i.e., left-to-right in a given", opt)
    pr_pa("line and top-to-bottom among the lines of a paragraph). If a location string", opt)
    pr_pa("does not include page–paragraph specification then it is assumed that the", opt)
    pr_pa("same paragraph is being referred to as by the previous location string.", opt)

def help_page_4(opt):
    "help paragraph 4"
    pr_pa("\nWhen moving on to a new paragraph (because the current paragraph being", opt)
    pr_pa("mined has run out of keywords) then the new location string should include", opt)
    pr_pa("page number and paragraph number attributes of that new paragraph.", opt)
    pr_pa("When starting to mine a new paragraph, no words from the previous", opt)
    pr_pa("paragraph may be used as index words for any eight-letter word in", opt)
    pr_pa("that new paragraph. So if the new paragraph starts with an eight-letter", opt)
    pr_pa("word, then that eight-letter word must be skipped (and thereby", opt)
    pr_pa("not be chosen as a keyword) because it has no index words preceding it.", opt)
    pr_pa("Likewise, if the first eight-letter word of the new paragraph has", opt)
    pr_pa("index words (at the beginning of the new paragraph) whose quantity of", opt)
    pr_pa("letters do not reach six, then that eight-letter word must be skipped.", opt)
    pr_pa("When starting to mine a new page, no words from the previous page", opt)
    pr_pa("may be used as index words for eight-letter words in the new page.", opt)
    
def help_page_5(opt):
    "help paragraph 5"
    pr_pa("\nThe quantity of index words to include in the location string may", opt)
    pr_pa("be chosen at will, as long as the quantity of letters included among", opt)
    pr_pa("them reaches at least six. When stripping an apostrophe from among", opt)
    pr_pa("a sequence of index words, it may either be replaced with a space", opt)
    pr_pa("or with nothing at all (i.e., the empty string); so that either", opt)
    pr_pa("the two sides of the apostrophe split up into two separate words", opt)
    pr_pa("or they conjoin into a single word. A hyphen between a pair of", opt)
    pr_pa("words can be replaced with a space; but a hyphen breaking a single", opt)
    pr_pa("word up at the end of a line can be removed, thereby joining", opt)
    pr_pa("the word back together.", opt)
    
def help_page_6(opt):
    "help paragraph 6"
    pr_pa("\nIt might be simpler to not use as a keyword any word that includes", opt)
    pr_pa("(or is abutted by) an apostrophe (or an apostrophe and letter(s) to the", opt)
    pr_pa("right of the apostrophe) (or, for that matter, any diacritic, or", opt)
    pr_pa("superscripted number). Just skip it; there are plenty of other words", opt)
    pr_pa("to choose from elsewhere in the text. If a word that ends in apostrophe “s”", opt)
    pr_pa("has eight letters (not counting the apostrophe “s”), then to use that word", opt)
    pr_pa("as an index word, replace the apostrophe with the empty string (so that the", opt)
    pr_pa("“s” gets appended to the word when being inputted into the location string).", opt)
    pr_pa("If a word that ends in apostrophe “s” has seven letters (not counting the", opt)
    pr_pa("apostrophe “s”), then to use that word as an index word, replace the", opt)
    pr_pa("apostrophe with a space (so that the “s” gets separated from the word and", opt)
    pr_pa("gets treated like a separate particle); that way the word is treated as a", opt)
    pr_pa("licit, seven-letter word instead of as an illicit eight-letter word.", opt)

def help_page_7(opt):
    "help paragraph 7"
    pr_pa("\nIf a paragraph on a given page started on the previous page then", opt)
    pr_pa("the starting paragraph number for that page is 0; otherwise the", opt)
    pr_pa("starting paragraph number for that page is 1. It is possible for", opt)
    pr_pa("a given paragraph to have no words that may be turned into keywords.", opt)
    pr_pa("It is also possible to skip a paragraph at will, for example if it", opt)
    pr_pa("contains a table or a quotation or equations or a dialogue or", opt)
    pr_pa("something else that makes it seem harder to deal with. An eight-letter", opt)
    pr_pa("word can only be used once as a keyword for the same password.", opt)
    pr_pa("If, say, some tables or dialogues in a given page make numbering paragraphs", opt)
    pr_pa("harder for that given page, then it may be convenient to simply skip that", opt)
    pr_pa("page (and not mine for eight-letter words in it).", opt)

def help_page_8(opt):
    "help paragraph 8"
    pr_pa("\nWhat happens if one enters an erroneous location string and is", opt)
    pr_pa("being prompted for the keyword belonging to that erroneous location?", opt)
    pr_pa("The most expedient manner of dealing with this situation is to", opt)
    pr_pa("enter \"XXXXXXXX\" as the keyword; this will immediately cancel the", opt)
    pr_pa("location–keyword pair and cause a prompting for a replacement pair.", opt)
    pr_pa("Otherwise there is one second (at least) to think about the", opt)
    pr_pa("correctness of the pair before answering the follow-up", opt)
    pr_pa("Y-or-N question. (Answering \"Y\" accepts the pair; answering", opt)
    pr_pa("\"N\" rejects it.)", opt)

def help_page_9(opt):
    "help paragraph 9"
    pr_pa("\nWhen a book is used for constructing a password, one should not", opt)
    pr_pa("make any markings on it, either with pencil or otherwise, that", opt)
    pr_pa("would facilitate reconstructing the password. (Example: underlining", opt)
    pr_pa("keywords.) That would be considered cheating. It can be helpful", opt)
    pr_pa("to choose a book that is hardcover and lays flatly open easily.", opt)
    pr_pa("The data file that is used to (re)construct a password should not", opt)
    pr_pa("be named after the book that its data refers to. The book should", opt)
    pr_pa("be specified within the data file anyway. Instead it is better to name", opt)
    pr_pa("the data file after the use that will be made of the password,", opt)
    pr_pa("possibly also qualified by the date when the data file was", opt)
    pr_pa("created. If the book has 366 main-text pages or more, then", opt)
    pr_pa("it is possible (when constructing a new password with it) to pick a", opt)
    pr_pa("page of that book based on the current day of the year. For example,", opt)
    pr_pa("if a password is created on May 12 of a common year, then start", opt)
    pr_pa("on page 132 of such a book, because May 12 is day 132 of a common year.", opt)

def help_page_10(opt):
    "help paragraph 10"
    pr_pa("\nWhen requested to input a location string, it is possible to", opt)
    pr_pa("make a query about a specific eight-letter word, to see if it", opt)
    pr_pa("is already in use as a keyword or if it is acceptable to be", opt)
    pr_pa("inducted into the database of keywords. In order to do this,", opt)
    pr_pa("enter the question mark character (\"?\") followed by the", opt)
    pr_pa("eight-letter word that is being queried about. The response", opt)
    pr_pa("will be immediate (and briefly evading the entry of a", opt)
    pr_pa("location string); then there will be a return to requesting", opt)
    pr_pa("for an entry of a location string. If page and paragraph number", opt)
    pr_pa("prefixes have already been written into the location string", opt)
    pr_pa("(but without yet hitting <ENTER>) then it is possible to then type", opt)
    pr_pa("\"?\" and the eight-letter word that one might have doubts about", opt)
    pr_pa("in order to query about it; then all the characters preceding", opt)
    pr_pa("the question mark will be ignored, as if everything before it", opt)
    pr_pa("were a comment. However, this comment can be helpful to the user", opt)
    pr_pa("for not losing track of what paragraph one is currently focusing", opt)
    pr_pa("one's attention on. If one had entered page and paragraph", opt)
    pr_pa("prefixes right before asking a question; then, after receiving", opt)
    pr_pa("an answer, one can copy those same page and paragraph prefixes", opt)
    pr_pa("from the line above and keep on mining for potential keywords", opt)
    pr_pa("in that paragraph. So the conveniences of the mid-sentence", opt)
    pr_pa("query are two: (1) not having to press backspace to", opt)
    pr_pa("delete what is already in the current entry, and (2) keeping", opt)
    pr_pa("what is before the question mark as a comment or prompt that can", opt)
    pr_pa("then be copied at the beginning of the next entry.", opt)

def help_page_11(opt):
    "help paragraph 11"
    pr_pa("\nIf an eight-letter word in the book is misspelled then ignore it,", opt)
    pr_pa("just skip past it; do not employ it for constructing the password.", opt)
    pr_pa("Also ignore any headlines. If a word is split between two pages and", opt)
    pr_pa("immediately precedes an eight-letter word, then the latter part of it", opt)
    pr_pa("(that lies at the beginning of the latter page) can be used as an index", opt)
    pr_pa("if it contains at least six letters (but not exactly eight); do not prepend", opt)
    pr_pa("the former part of it that lies at the end of the former page.", opt)

def help_page_12(opt):
    "help paragraph 12"
    pr_pa("\nIf, while reconstructing a password for the first time (i.e., “confirming”", opt)
    pr_pa("it), a flaw is noticed in a location string, then a way to deal with", opt)
    pr_pa("it can be to write a note about it on a piece of paper", opt)
    pr_pa("including three data: (1) the current, flawed location", opt)
    pr_pa("string, (2) the “fingerprint” (a tripartite hash consisting of a", opt)
    pr_pa("character, a decimal number, and a natural number), and (3)", opt)
    pr_pa("the corrected location string. When done confirming the password,", opt)
    pr_pa("open the password-constructing database file with some plain-text editor;", opt)
    pr_pa("use the editor’s search function to search for each flawed", opt)
    pr_pa("location string; check that the fingerprint on that line matches", opt)
    pr_pa("the fingerprint that has been noted for that location string (and note that", opt)
    pr_pa("double semicolons are used as separators on each record of the database (as", opt)
    pr_pa("stored in the text file)); then replace the flawed location string in the", opt)
    pr_pa("targeted record with the corrected location string.", opt)
    pr_pa("An alternative is to open the database file with a text editor while", opt)
    pr_pa("the reconstruction is still running/going on; and, whenever a flaw", opt)
    pr_pa("in a location string is detected, going over to the database text file", opt)
    pr_pa("and making the correction directly, without going through the", opt)
    pr_pa("intermediate step of writing all the errors down on a piece of paper.", opt)

def help_page_13(opt):
    "help paragraph 13"
    pr_pa("\nExample of a typical correction of a location string: prepending extra", opt)
    pr_pa("index words to the substring of index words in a location string.", opt)
    pr_pa("Why might one be compelled to do this? Suppose that some string of index", opt)
    pr_pa("words points to more than one word in a given paragraph. Suppose that the", opt)
    pr_pa("first such word (at least) that it points to is not a keyword. Then,", opt)
    pr_pa("the index string should be expanded (in the only direction possible:", opt)
    pr_pa("namely, backwards, i.e., leftwards) so as to disambiguate between those", opt)
    pr_pa("multiple words that are being pointed to in order to pinpoint only the", opt)
    pr_pa("meant keyword.", opt)

def help_page_14(opt):
    "help paragraph 14"
    pr_pa("\nA possible rule of thumb for preventing such ambiguities is to include,", opt)
    pr_pa("whenever possible, three words in the index string. This heuristic rule", opt)
    pr_pa("should be excepted only when there are only one or two words between", opt)
    pr_pa("the latest keyword and the previous eight-letter word. Because of such", opt)
    pr_pa("exceptability, this rule of thumb should not be rigidly enforced by this", opt)
    pr_pa("software (but it could be made to give a warning (which can be either", opt)
    pr_pa("heeded or overriden)). [That has been implemented now in the latest", opt)
    pr_pa("version.] Another possible error in a location string is missing the prefix", opt)
    pr_pa("for page number and paragraph number when the associated index word is in", opt)
    pr_pa("a different paragraph than the previous index word. There is now a", opt)
    pr_pa("“??” command in creation mode that causes the last-declared page and", opt)
    pr_pa("paragraph numbers to be displayed.", opt)

def help_page_15(opt):
    "help paragraph 15"
    pr_pa("Now there is also a “:CORRECTION:” command for both “create new” and", opt)
    pr_pa("“reconstruct” modes: it allows prepending a missing page–paragraph", opt)
    pr_pa("prefix to the previous entry. This is how it words for “reconstruct”", opt)
    pr_pa("mode: suppose that for the current entry the user notices that", opt)
    pr_pa("the location string is missing a necessary page–paragraph prefix", opt)
    pr_pa("(because the keyword with the given index words cannot be found", opt)
    pr_pa("in the paragraph of the previous entry). In such a case,", opt)
    pr_pa("when the correct keyword is found in the different paragraph,", opt)
    pr_pa("enter the keyword. But then, when prompted for the keyword of the", opt)
    pr_pa("next entry, type “:CORRECTION:” and <ENTER>. Then the user will", opt)
    pr_pa("be prompted for a page number and a paragraph number; then", opt)
    pr_pa("the page–paragraph prefix will be prepended to the location string", opt)
    pr_pa("of that previous entry; and focus will return to the present entry.", opt)
    print("\n")

def is_string(param):
    "Boolean-valued function which checks whether parameter param is a string or not."
    return (param == str(param))

"Functions for writing in the password shuttle."
def four_digit_shuffle(a, b, c, d):
    "Shuffles a quadruplet of four digits (or any four values passed as parameters, \
     actually)."
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
    """Given digit dgt, this function returns a quadruplet of four digits that somewhat
    covertly imply that digit. Here is how it works: There are five even digits and five odd
    digits. To mask an even digit, present the remaining four even digits in shuffled order.
    To mask an odd digit, present the remaining four odd digits in shuffled order."""
    a = (dgt + 2) % 10
    b = (dgt + 4) % 10
    c = (dgt + 6) % 10
    d = (dgt + 8) % 10
    return four_digit_shuffle(a, b, c, d)

def four_digit_mask(a, b, c, d):
    """Given a quadruplet of digits, returns a 16-tuple of digits that imply those four
    digits; but in a way that might not be immediately obvious: that is, in a way that might
    prevent their instantaneous, all-at-once apperception. How it works: The one_digit_mask
    of each digit is interleaved with the one_digit_mask's of the other three digits."""
    a_m = one_digit_mask(a)
    b_m = one_digit_mask(b)
    c_m = one_digit_mask(c)
    d_m = one_digit_mask(d)
    return (a_m[0], b_m[0], c_m[0], d_m[0], a_m[1], b_m[1], c_m[1], d_m[1], a_m[2], \
            b_m[2], c_m[2], d_m[2], a_m[3], b_m[3], c_m[3], d_m[3])

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

def camouflage_trellis(digits_AR):
    "Outputs the four digits in a masked way, so that the user cannot (or should not) \
     perceive them all at once."
    print("\nCAMOUFLAGE TRELLIS")
    print("Add each row of digits module 10 mentally in order to obtain each digit.")
    print("Rows that end in question mark are buffers, but their sum must be input before")
    print("moving on to the next line.\n")
    cont = True    # default
    while cont:
        print("The four digits are (add):\n")
        buffer_digit()
        for i in range(4):
            digit_mask(digits_AR[i])
            buffer_digit()
        cont_answer = ""        # continue answer = answer about continuation
        while not (cont_answer in ["y", "n"]):
            cont_answer = input("Another (y/n)? ")
        if (cont_answer == "n"):
            cont = False
        else:
            print("\n\n\n\n")

def password_shuttle(digits_AR):
    shuttle_position = 0
    while not (shuttle_position in ["1", "2"]):
        shuttle_position = input("What position: 1 or 2? ")
    if (shuttle_position == "1"):
        file_1 = open("shuttle_2.txt", "w")
        file_1.write(four_digit_mask_Mro_ST(digits_AR[0], digits_AR[1], digits_AR[2], \
                                            digits_AR[3]) + "\n")
        file_1.close()
        print("The password has been written into the shuttle's first position.")
    elif (shuttle_position == "2"):
        file_1 = open("shuttle_2.txt", "a")
        file_1.write(four_digit_mask_Mro_ST(digits_AR[0], digits_AR[1], digits_AR[2], \
                                            digits_AR[3]))
        file_1.close()
        print("The password has been written into the shuttle's second position.")
    return int(shuttle_position)

def swift_alter():
    "Swift alteration mode. Global variables used: data, the_book, the_author, \
     the_publisher, the_codeword_hash, old_f_ST, keywords_LS, upper_bound."
    global mm, nn, debug_0, upper_bound, keywords_LS, data, is_toy_version
    "(MAIN)"
    errorFlag = False
    old_vector_left_LS = [0, 0, 0, 0, 0, 0, 0, 0]
    old_vector_right_LS = [0, 0, 0, 0, 0, 0, 0, 0]
    DEBUG(debug_0, f"len(keywords_LS) = {len(keywords_LS)}")
    DEBUG(debug_0, f"keywords_LS = {keywords_LS}")
    vecsum_left = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    vecsum_right = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
                   [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    vecsum_total = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    "ignore prefix"
    for i in range(1, upper_bound + 1):
        "mode: alter"
        if not (i in [mm[0], mm[1], mm[2]]) \
           and not (is_toy_version and (i in [nn[0], nn[1], nn[2]])):
            print(f"\nLocation #{i}: {data[i][0]}")
            word_ST = keywords_LS[i - 1]
            print(f"Keyword #{i}: {word_ST}")
            vec_LS = transnumeration(word_ST)
            lett0 = phi_lett(vec_LS)
            variance0 = phi_variance(vec_LS)
            ordnum0 = phi_ordnum(word_ST)
            if (data[i][1] == lett0) and (data[i][2] == variance0) \
               and (data[i][3] == ordnum0):
                print("Fingerprint OK.")
            else:
                print("Error: Fingerprint not OK.")
                quit()
        elif (i in [mm[0], mm[1], mm[2]]) \
             or (is_toy_version and (i in [nn[0], nn[1], nn[2]])):
            word_ST = ""
            while not is_proper_keyword(word_ST):
                word_ST = input(f"\nEnter some all-caps eight-letter word for location {i}: ")
                if not is_proper_keyword(word_ST):
                    print("Error: Please enter an eight-letter word in all caps.")
            vec_LS = transnumeration(word_ST)
            lett0 = phi_lett(vec_LS)
            variance0 = phi_variance(vec_LS)
            ordnum0 = phi_ordnum(word_ST)
            data[i] = (word_ST +  " =", lett0, variance0, ordnum0)
            print(f"Alteration at location {i} has been done.")
        "Add to previous word."
        vector_LS = transnumeration(word_ST)
        vecsum_left_LS = vector_sum(old_vector_left_LS, vector_LS)
        old_vector_left_LS = left_rotate(vecsum_left_LS)
        vecsum_right_LS = vector_sum(old_vector_right_LS, vector_LS)
        old_vector_right_LS = right_rotate(vecsum_right_LS)
        for ii in [0, 1, 2, 3]:
            if (i == mm[ii]) or (is_toy_version and (i == nn[ii])):
                vecsum_left[ii] = old_vector_left_LS
                vecsum_right[ii] = old_vector_right_LS
                vecsum_total[ii] = vecsum_left[ii] + vecsum_right[ii]
        "Fingerprint (of a keyword)."
        lett = phi_lett(vector_LS)
        variance = phi_variance(vector_LS)
        ordnum = phi_ordnum(word_ST)
        print(f"phi_lett = {lett}\nphi_variance = {variance}\nphi_ordnum = {ordnum}")
        time.sleep(0.3)
    "Extract single digits from the four sums."
    digits = array('i', [-1, -1, -1, -1])
    for ii in [0, 1, 2, 3]:
        digits[ii] = vector_hash_6(vecsum_total[ii]) % 10
    "Check the digits for redundancies."
    for ii in [0, 1, 2]:
        for jj in range(ii + 1, 4):
            if (digits[ii] == digits[jj]):
                print("Error: Digits %d and %d are the same." % (ii, jj))
                errorFlag = True
    if not errorFlag:
        print("The digits are OK (i.e., all different from each other).\n")
    elif errorFlag:
        print("Error: The digits are not OK.")
        answer_CH = ""
        while not (answer_CH in ["y", "n"]):
            answer_CH = input("Would you like to try \"swift alter\" mode again \
(\"y\", \"n\")? ")
            if not (answer_CH in ["y", "n"]):
                print("Error: please enter either \"y\" or \"n\".")
        if (answer_CH == "y"):
            return swift_alter()                  # recursive
        else:
            return 0
    #codeword_hash = string_hash_6(str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3]))
    codeword_hash = 12
    if not errorFlag:
        data[0] = ("Codeword hash:", codeword_hash)
    elif errorFlag:
        data[0] = ("Codeword hash:", -13)
    if not errorFlag:
        ans_CH = ""
        while not (ans_CH in ["y", "n"]):
            ans_CH = input("\nSave (y/n)? ")
            if not (ans_CH in ["y", "n"]):
                print("Error: Please enter either \"y\" or \"n\".")
        if (ans_CH == "n"):
            return 0.5
        elif (ans_CH == "y"):
            a_book = the_book
            an_author = the_author
            a_publisher = the_publisher
            a_location = the_location
            filename_OK = False
            while not filename_OK:
                f_ST = input("Enter filename: ")
                if (len(f_ST) < 6) or not (f_ST[-5:] == ".2H4D"):
                    print("Error: The filename should have extension .2H4D.")
                elif (f_ST == old_f_ST):
                    print("Error: The altered file should have a different filename \
from the original file.")
                else:
                    filename_OK = True
            "save data in file"
            with open(f_ST, "w") as f:
                for item in data:
                    f.write(stringify_tuple(item) + "\n")
            print("The altered file has been written.")
            print("When assigning the password, it has to be entered twice: the first")
            print("time from one camouflage trellis, the second time from another")
            print("(different) camouflage trellis.")
            print("METADATA")
            print(f"Filename: {f_ST}")
            print("Executor: FourHundredWords2FourDigits_13.py")
            print(f"Book's name: {a_book}")
            print(f"Book's author: {an_author}")
            print(f"Book's publisher: {a_publisher}")
            print(f"Book's location: {a_location}")
            "output"
            output_mode = ""
            while not (output_mode in ["t",  "s"]):
                output_mode = input("\nCamouflage trellis (t) or password shuttle (s)? ")
            if (output_mode == "t"):
                camouflage_trellis(digits)
            if (output_mode == "s"):
                shuttle_pos = password_shuttle(digits)
            "log: swift alteration"
            antwoord_CH = ""
            while not (antwoord_CH in ["y", "n"]):
                antwoord_CH = input("\nWould you like this alteration episode to be \
logged (y/n)? ")
            if (antwoord_CH == "y"):
                "append entry in password_construction_log.txt"
                with open("password_construction_log.txt", "a") as fil_chron:
                    fil_chron.write("- - - - - - - -\n")
                    todays_date = date.today()
                    fil_chron.write(f"Today's date: {todays_date}\n")
                    fil_chron.write(f"Created through swift alteration: {f_ST}\n")
                    fil_chron.write(f"It was modified from: {old_f_ST}\n")
                    if (output_mode == "t"):
                        fil_chron.write("Output mode: trellis\n")
                    elif (output_mode == "s"):
                        fil_chron.write(f"Output mode: shuttle, #{shuttle_pos}\n")
                print("A brief mention has been written in password_construction_log.txt.")                   
            return 1

def DEBUG(flag_BL, msg_ST):
    "Prints msg_ST only if flag_BL is True."
    if flag_BL:
        print(msg_ST)

def what_prefix(datum_ST):
    "Extracts the page–paragraph prefix from datum_ST and returns it."
    index_word_string = if_paragraph_then_swallow(if_page_then_swallow(datum_ST))
    prefix_length_NT = len(datum_ST) - len(index_word_string)
    the_prefix_ST = datum_ST[0:prefix_length_NT]
    return the_prefix_ST

def if_not_is_proper_keyword(word_ST):
    "Deals with argument word_ST not being a proper keyword. If it is a correction \
request, then deal with it; otherwise give an error message."
    global data, prefix, reconstruct_changed
    if not is_proper_keyword(word_ST):
        if (i > 1) and (word_ST == ":CORRECTION:"):
            print(f"Current previous (#{i - 1}) location string: \
{data[i - 1][0]}")
            if (data[i - 1][0].count(".") == 0):
                page_num = input("Enter the page number: ")
                par_num = input("Enter the paragraph number: ")
                new_prefix = f"P. {page_num} PAR. {par_num} "
                if not (new_prefix == prefix):
                    data[i - 1] = (new_prefix + data[i - 1][0], \
                                   data[i - 1][1], data[i - 1][2], \
                                   data[i - 1][3])
                    print(f"New previous (#{i - 1}) location string: \
{data[i - 1][0]}")
                    reconstruct_changed = True
                    prefix = new_prefix
                else:
                    print("Error: The same location prefix should")
                    print("not be repeated.")
                print("\nNow back to the present entry.")
                print(f"\nLocation #{i}: {data[i][0]}")
            elif (data[i - 1][0].count(".") == 2):
                page_num = input("Enter the new page number: ")
                par_num = input("Enter the new paragraph number: ")
                new_prefix = f"P. {page_num} PAR. {par_num} "
                new_datum = \
                          data[i - 1][0].replace(\
                              what_prefix(data[i - 1][0]), new_prefix)
                data[i - 1] = (new_datum, data[i - 1][1], \
                               data[i - 1][2], data[i - 1][3])
                prefix = new_prefix
                print(\
                f"New previous (#{i - 1}) location string: {data[i - 1][0]}")
                reconstruct_changed = True
                print("\nNow back to the present entry.")
                print(f"\nLocation #{i}: {data[i][0]}")
            else:
                print("Error: Cannot prepend a page-number prefix to")
                print("a string that already has periods in it.")
        elif (i == 1) and (word_ST == ":CORRECTION:"):
            print("Error: It is not possible to correct a non-existent")
            print("zeroth entry.")
        elif (word_ST == "??"):
            if (len(prefix) > 0):
                print(prefix)
            else:
                print("No page number — paragraph number prefix has")
                print("been entered yet.")
        else:                        
            print("Error: Please enter an eight-letter word in all caps.")
    

"PRE-MAIN"

data = []
debug_0 = False
debug_1 = False
debug_2 = False
"LOAD?"
mode = ""
while not (mode in ['c', 'r', 'a']):
    mode = input("Create new (c), reconstruct (r), or alter (a)? ")
if (mode == "r") or (mode == "a"):
    filename_OK = False
    while not filename_OK:
        f_ST = input("Enter filename: ")
        if (len(f_ST) < 6) or not (f_ST[-5:] == ".2H4D"):
            print("Error: The filename's extension should be .2H4D.")
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
                    if not line_LS[0] in ["Executor:", "Book:", "Author:", "Publisher:", \
                                          "Location:", "Codeword hash:"]:
                        print("L1041. ERROR: Not an approved first element for an \
ordered pair.")
                    if (line_LS[0] == "Executor:") \
                       and (not line_LS[1] == "TwoHundredWords2FourDigits_6.py"): 
                        print("Error: I am not the executor of this file.")
                        exit()
                    if line_LS[0] == "Book:":
                        the_book = line_LS[1]
                        print(f"Book: {the_book}\n")
                    elif line_LS[0] == "Author:":
                        the_author = line_LS[1]
                        print(f"Author: {the_author}\n")
                    elif line_LS[0] == "Publisher:":
                        the_publisher = line_LS[1]
                        print(f"Publisher: {the_publisher}\n")
                    elif line_LS[0] == "Location:":
                        the_location = line_LS[1]
                        print(f"Location: {the_location}\n")
                    elif line_LS[0] == "Codeword hash:":
                        the_codeword_hash = int(line_LS[1])
                        if (the_codeword_hash == -13) and (mode == "r"):
                            print("There is an error with the password; so it should not \
be reconstructed.")
                            print("Instead, consider altering it.")
                            quit()
                    data.append((line_LS[0], line_LS[1]))                        
                else:
                    print(f"L1069. len(line_LS) = {len(line_LS)}")
                    print("L1070. ERROR")
            else:
                print("L1072. ERROR: Line is not wrapped in parentheses.")
    print("File has been loaded.")

    if (mode == "a"):
        old_f_ST = f_ST
    elif (mode == "r"):
        reconstruct_changed = False
        old_f_ST = f_ST               # might be used in swift_alter

"MAIN"
is_toy_version = False          # This line is user-modifiable; the RHS should be
                                # either True or False.
errorFlag = False
mm = array('i', [50, 100, 150, 200])
nn = array('i', [5, 10, 15, 20])
keywords_LS = []
if (mode == "c"):
    data = [0]
old_vector_left_LS = [0, 0, 0, 0, 0, 0, 0, 0]
old_vector_right_LS = [0, 0, 0, 0, 0, 0, 0, 0]
if is_toy_version:
    print("This execution is in toy mode.")
    upper_bound = nn[3]
else:
    upper_bound = mm[3]
if (mode == "c"):
    print("Type \":HELP:\" and <ENTER> for explanatory help.")
older_prefix = ""
prefix = ""
vecsum_left = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
vecsum_right = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
vecsum_total = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
prefix_changed = False
for i in range(1, upper_bound + 1):
    if (mode == "c"):
        "mode: create new"
        enter_loop_BL = True
        while enter_loop_BL:
            loc = input(f"\nInput location #{i}: ")
            prefix_changed = False
            if (loc == ":HELP:"):
                help_intro()
                OK = True
                word_ST = "ZZZZZZZZ"
            elif (i > 1) and (loc == ":CORRECTION:"):
                print(f"Current previous (#{i - 1}) location string: {data[i - 1][0]}")
                if (data[i - 1][0].count(".") == 0):
                    page_num = input("Enter the page number: ")
                    par_num = input("Enter the paragraph number: ")
                    new_prefix = f"P. {page_num} PAR. {par_num} "
                    if not (new_prefix == prefix):
                        data[i - 1] = (new_prefix + data[i - 1][0], data[i - 1][1], \
                                       data[i - 1][2], data[i - 1][3])
                        print(f"New previous (#{i - 1}) location string: {data[i - 1][0]}")
                        prefix = new_prefix
                        older_prefix = new_prefix
                        word_ST = "ZZZZZZZZ"
                        OK = True
                        respuesta = "N"
                    else:
                        print("Error: The same location should not be repeated.")
                elif (data[i - 1][0].count(".") == 2):
                    page_num = input("Enter the new page number: ")
                    par_num = input("Enter the new paragraph number: ")
                    new_prefix = f"P. {page_num} PAR. {par_num}"
                    new_datum = data[i - 1][0].replace(what_prefix(data[i - 1][0]), \
                                                       new_prefix)
                    data[i - 1] = (new_datum, data[i - 1][1], data[i - 1][2], data[i - 1][3])
                    prefix = new_prefix
                    older_prefix = new_prefix
                    print(f"New previous (#{i - 1}) location string: {data[i - 1][0]}")
                    word_ST = "ZZZZZZZZ"
                    OK = True
                    respuesta = "N"
                else:
                    print(f"L1147. ERROR: Wrong number of periods \
({data[i - 1][0].count('.')}) in the location string.")
            elif (i == 1) and (loc == ":CORRECTION:"):
                print("Error: it is not possible to correct a non-existent zeroth entry.")
                word_ST = "ZZZZZZZZ"
                OK = True
                respuesta = "N"
            #END
            elif (loc == "??"):
                if (len(prefix) > 0):
                    print(prefix)
                else:
                    print("No page number – paragraph number prefix has been entered yet.")
                word_ST = "ZZZZZZZZ"
                OK = True
                respuesta = "N"
            elif (len(loc) > 0) and (loc[0] == "?"):
                question = loc[1:]
                if not is_proper_keyword(question):
                    print("No; a keyword should be an eight-letter word in all caps.")
                elif (question in keywords_LS):
                    print("No; the word is already in use as a keyword.")
                else:
                    print("Yes; it is acceptable as a new keyword.")
                OK = True
                respuesta = "N"
                word_ST = "ZZZZZZZZ"
            elif (loc.count("?") == 1) and not (loc[-1] == "?"):
                split_LS = loc.split("?")
                second_ST = split_LS[1]
                if not is_proper_keyword(second_ST):
                    print("No; a keyword should be an eight-letter word in all caps.")
                elif (second_ST in keywords_LS):
                    print("No; the word is already in use as a keyword.")
                else:
                    print("Yes; it is acceptable as a new keyword.")
                OK = True
                respuesta = "N"
                word_ST = "ZZZZZZZZ"
            elif (len(loc) == 0):
                print("Error: The location string should not be null.")
                word_ST = "ZZZZZZZZ"
                OK = True
                respuesta = "N"
            elif not (loc.count(".") in [0, 2]):
                if (loc.count(".") > 2):
                    print("Error: There cannot be more than two periods.")
                    print("Type :HELP: and <ENTER> for explanatory help.")
                else:
                    print("Error: There cannot be just one period.")
                    if (loc[0:5] == "PAR. ") and (loc[5:6].isdigit()):
                        print("Specification of paragraph number should be immediately")
                        print("preceded by a specification of page number. I.e., a")
                        print("\"PAR. {#} \"prefixshould be immediately preceded by a")
                        print("\"P. {#} \" prefix.")
                    elif (loc[0:3] == "P. ") and (loc[3:4].isdigit()):
                        print("Specification of page number should be immediately followed")
                        print("by a specification of paragraph number. I.e., a")
                        print("\"P. {#} \" prefix should be immediately followed by a")
                        print("\"PAR. {#} \" prefix.")
                    else:
                        print("Type :HELP: and <ENTER> for explanatory help.")
                OK = True
                respuesta = "N"
                word_ST = "ZZZZZZZZ"
            elif \
not is_UALPHAnumeric(if_paragraph_then_swallow(if_page_then_swallow(loc)).replace(" ", "")): 
                print("Error: After (optionally) specifying the page number (through")
                print("\"P. {#} \") and (included as part of the option) specifying the")
                print("paragraph number (through \"PAR. {#} \"), the remainder of the")
                print("location string should consist only of spaces, digits, and uppercase")
                print("letters. Please try again.")
                OK = True
                respuesta = "N"
                word_ST = "ZZZZZZZZ"
            elif (letter_count(loc) < 6):
                if (letter_count(loc) == -9):
                    print("Error: No word in the index should have exactly eight letters.")
                    print("Please try again.")
                else:
                    print("Error: Index word(s) should have at least six letters among")
                    print("them. Please try again.")
                OK = True
                respuesta = "N"
                word_ST = "ZZZZZZZZ"
            elif (index_word_count(loc) < 3):
                print("Warning: The quantity of index words is less than three.")
                response = ""
                while not (response in ["CONTINUE", "RETRY"]):
                    response = input("Continue anyway (\"CONTINUE\") or retry (\"RETRY\")? ")
                    if not (response in ["CONTINUE", "RETRY"]):
                        print("Error: type either \"CONTINUE\" or \"RETRY\"and then")
                        print("press <ENTER>.")
                if (response == "RETRY"):
                    OK = True
                    respuesta = "N"
                    word_ST = "ZZZZZZZZ"
                elif (response == "CONTINUE"):
                    OK = False
                    "update of prefix: 'create new' mode > 'CONTINUE' case"
                    if (len(what_prefix(loc)) > 0):
                        if (what_prefix(loc) == prefix):
                            print("Error: The prefix has been repeated, but the location")
                            print("string is now being automatically corrected.")
                            loc = loc[len(prefix):]
                        else:
                            older_prefix = prefix
                            prefix = what_prefix(loc)
                            DEBUG(debug_1, f"L1255. prefix = {prefix}")
                            prefix_changed = True
                    else:
                        older_prefix = prefix
            else:
                OK = False
                "update of prefix: 'create new' mode"
                if (len (what_prefix(loc)) > 0):
                    if (what_prefix(loc) == prefix):
                        print("Error: The prefix has been repeated; but the location")
                        print("string is now being automatically corrected.")
                        loc = loc[len(prefix):]
                    else:
                        older_prefix = prefix
                        prefix = what_prefix(loc)
                        DEBUG(debug_1, f"L1274. prefix = {prefix}")
                        prefix_changed = True
                else:
                    older_prefix = prefix
            while not OK:
                word_ST = ""
                while not is_proper_keyword(word_ST):
                    word_ST = input(f"Keyword #{i}: ")
                    if not is_proper_keyword(word_ST):
                        if (word_ST == ":HELP:"):
                            help_intro()
                        else:                        
                            print("Error: Please enter an eight-letter word in")
                            print("all caps (or \"XXXXXXXX\" to cancel).")                    
                OK = True
            if (word_ST == "XXXXXXXX"):
                OK = True
                respuesta = "N"
                print("The index–keyword pair has been canceled.")
                if prefix_changed:
                    prefix = older_prefix
                    DEBUG(debug_1, f"L1295. prefix = {prefix}")
            elif (word_ST == "ZZZZZZZZ"):
                OK = True
                respuesta = "N"
                if prefix_changed:
                    prefix = older_prefix
                    DEBUG(debug_1, f"L1301. prefix = {prefix}")
            elif (word_ST in keywords_LS):
                OK = True
                respuesta = "N"
                print("Please use a keyword that is different from any previous keyword.")
                if prefix_changed:
                    prefix = older_prefix
                    DEBUG(debug_1, f"L1308. prefix = {prefix}")
            else:
                OK = False
                time.sleep(1)
            while not OK:
                respuesta = input("Is the index–keyword pair correct (Y/N)? ")
                if (respuesta in ["Y", "N"]):
                    OK = True
            if (respuesta == "Y"):
                enter_loop_BL = False
            elif (respuesta == "N") and prefix_changed:
                prefix = older_prefix
                DEBUG(debug_1, f"prefix = {prefix}")
        keywords_LS.append(word_ST)
    elif (mode == "r"):
        "mode: reconstruct"
        print(f"\nLocation #{i}: {data[i][0]}")
        OK = False
        "update of prefix: 'reconstruct' mode"
        datum = data[i][0]
        if (len(what_prefix(datum)) > 0):
            if (what_prefix(datum) == prefix):
                print("Error: The prefix has been repeated; but the location string")
                print("is now being automatically corrected.")
                new_datum = datum[len(prefix):]
                data[i] = (new_datum, data[i][1], data[i][2], data[i][3])
            else:
                prefix = what_prefix(datum)
                DEBUG(debug_1, f"prefix = {prefix}")
        while not OK:
            word_ST = ""
            while not is_proper_keyword(word_ST):
                word_ST = input(f"Keyword #{i}: ")
                if not is_proper_keyword(word_ST):
                    if (i > 1) and (word_ST == ":CORRECTION:"):
                        print(\
                            f"Current previous (#{i - 1}) location string: {data[i - 1][0]}")
                        if (data[i - 1][0].count(".") == 0):
                            page_num = input("Enter the page number: ")
                            par_num = input("Enter the paragraph number: ")
                            new_prefix = f"P. {page_num} PAR. {par_num}"
                            if not (new_prefix == prefix):
                                data[i - 1] = (new_prefix + data[i - 1][0], \
                                               data[i - 1][1], data[i - 1][2], \
                                               data[i - 1][3])
                                print(f"New previous (#{i - 1}) location string: \
{data[i - 1][0]}")
                                reconstruct_changed = True
                                prefix = new_prefix
                                DEBUG(debug_1, f"prefix = {prefix}")
                            else:
                                print("Error: The same location prefix should not be \
repeated.")
                            print("\nNow back to the present entry.")
                            print(f"\nLocation #{i}: {data[i][0]}")
                        elif (data[i - 1][0].count(".") == 2):
                            page_num = input("Enter the new page number: ")
                            par_num = input("Enter the new paragraph number: ")
                            new_prefix = f"P. {page_num} PAR. {par_num} "
                            new_datum = \
                                      data[i - 1][0].replace(what_prefix(data[i - 1][0]), \
                                                             new_prefix)
                            data[i - 1] = (new_datum, data[i - 1][1], data[i - 1][2], \
                                           data[i - 1][3])
                            prefix = new_prefix
                            print(f"New previous (#{i - 1}) location string: \
{data[i - 1][0]}")
                            reconstruct_changed = True
                            print("\nNow back to the present entry.")
                            print(f"\nLocation #{i}: {data[i][0]}")
                        else:
                            print("Error: Cannot prepend a page-number prefix to a string")
                            print("that already has periods in it.")
                    elif (i == 1) and (word_ST == ":CORRECTION:"):
                        print("Error: It is not possible to correct a non-existent, \
zeroth entry.")              
                    elif (word_ST == "??"):
                        if (len(prefix) > 0):
                            print(prefix)
                        else:
                            print("No page number – paragraph number prefix has been \
entered yet")
                    else:
                        print("Error: Please enter an eight-letter word in all caps.")                
            vec_LS = transnumeration(word_ST)
            lett0 = phi_lett(vec_LS)
            variance0 = phi_variance(vec_LS)
            ordnum0 = phi_ordnum(word_ST)
            if (data[i][1] == lett0) and (data[i][2] == variance0) \
               and (data[i][3] == ordnum0):
                print("Fingerprint OK.")
                OK = True
                keywords_LS.append(word_ST)
            else:
                print("Fingerprint not ok; try again.")
    elif (mode == "a"):
        "mode: alter"
        if not (i in [mm[0], mm[1], mm[2]]) and (not (is_toy_version \
                                                     and (i in [nn[0], nn[1], nn[2]]))):
            print(f"\nLocation #{i}: {data[i][0]}")
            OK = False
            "update of prefix: 'alter' mode"
            datum = data[i][0]
            if (len(what_prefix(datum)) > 0):
                if (what_prefix(datum) == prefix):
                    print("Error: The prefix has been repeated, but the location string")
                    print("is now being automatically corrected.")
                    new_datum = datum[len(prefix):]
                    data[i] = (new_datum, data[i][1], data[i][2], data[i][3])
                else:
                    prefix = what_prefix(datum)
                    DEBUG(debug_1, f"prefix = {prefix}")
            while not OK:
                word_ST = ""
                while not is_proper_keyword(word_ST):
                    word_ST = input(f"Keyword #{i}: ")
                    #BEGIN
                    #if not is_proper_keyword(word_ST):
                    #    if (i > 1) and (word_ST == ":CORRECTION:"):
                    #        print(f"Current previous (#{i - 1}) location string: \
#{data[i - 1][0]}")
                    #        if (data[i - 1][0].count(".") == 0):
                    #            page_num = input("Enter the page number: ")
                    #            par_num = input("Enter the paragraph number: ")
                    #            new_prefix = f"P. {page_num} PAR. {par_num} "
                    #            if not (new_prefix == prefix):
                    #                data[i - 1] = (new_prefix + data[i - 1][0], \
                    #                               data[i - 1][1], data[i - 1][2], \
                    #                               data[i - 1][3])
                    #                print(f"New previous (#{i - 1}) location string: \
#{data[i - 1][0]}")
                    #                reconstruct_changed = True
                    #                prefix = new_prefix
                    #                DEBUG(f"prefix = {prefix}")
                    #            else:
                    #                print("Error: The same location prefix should")
                    #                print("not be repeated.")
                    #            print("\nNow back to the present entry.")
                    #            print(f"\nLocation #{i}: {data[i][0]}")
                    #        elif (data[i - 1][0].count(".") == 2):
                    #            page_num = input("Enter the new page number: ")
                    #            par_num = input("Enter the new paragraph number: ")
                    #            new_prefix = f"P. {page_num} PAR. {par_num} "
                    #            new_datum = \
                    #                      data[i - 1][0].replace(\
                    #                          what_prefix(data[i - 1][0]), new_prefix)
                    #            data[i - 1] = (new_datum, data[i - 1][1], \
                    #                           data[i - 1][2], data[i - 1][3])
                    #            prefix = new_prefix
                    #            print(\
                    #            f"New previous (#{i - 1}) location string: {data[i - 1][0]}")
                    #            reconstruct_changed = True
                    #        else:
                    #            print("Error: Cannot prepend a page-number prefix to")
                    #            print("a string that already has periods in it.")
                    #    elif (i == 1) and (word_ST == ":CORRECTION:"):
                    #        print("Error: It is not possible to correct a non-existent")
                    #        print("zeroth entry.")
                    #    elif (word_ST == "??"):
                    #        if (len(prefix) > 0):
                    #            print(prefix)
                    #        else:
                    #            print("No page number — paragraph number prefix has")
                    #            print("been entered yet.")
                    #    else:                        
                    #        print("Error: Please enter an eight-letter word in all caps.")
                    #END
                    #BEGIN
                    if_not_is_proper_keyword(word_ST)
                    #END
                vec_LS = transnumeration(word_ST)
                lett0 = phi_lett(vec_LS)
                variance0 = phi_variance(vec_LS)
                ordnum0 = phi_ordnum(word_ST)
                if (data[i][1] == lett0) and (data[i][2] == variance0) \
                   and (data[i][3] == ordnum0):
                    print("Fingerprint OK.")
                    OK = True
                    keywords_LS.append(word_ST)
                else:
                    print("Fingerprint not ok; try again.")
        elif (i in [mm[0], mm[1], mm[2]]) or (is_toy_version \
                                              and (i in [nn[0], nn[1], nn[2]])):
            word_ST = ""
            while not is_proper_keyword(word_ST):
                word_ST = \
                        input(f"\nEnter some all-caps eight-letter word for location {i}: ")
                #BEGIN
                #if not is_proper_keyword(word_ST):
                #    print("Error: Please enter an eight-letter word in all caps.")
                #END
                #BEGIN
                if_not_is_proper_keyword(word_ST)
                #END
            keywords_LS.append(word_ST)
            vec_LS = transnumeration(word_ST)
            lett0 = phi_lett(vec_LS)
            variance0 = phi_variance(vec_LS)
            ordnum0 = phi_ordnum(word_ST)
            data[i] = (word_ST + " =", lett0, variance0, ordnum0)
            print(f"Alteration at location {i} has been done.")
    else:
        print("L1496. ERROR: variable mode should be one of c, r, a.")
                
    "Any mode: add to previous word."
    vector_LS = transnumeration(word_ST)
    vecsum_left_LS = vector_sum(old_vector_left_LS, vector_LS)
    old_vector_left_LS = left_rotate(vecsum_left_LS)
    vecsum_right_LS = vector_sum(old_vector_right_LS, vector_LS)
    old_vector_right_LS = right_rotate(vecsum_right_LS)
    for ii in [0, 1, 2, 3]:
        if (i == mm[ii]) or (is_toy_version and (i == nn[ii])):
            DEBUG(debug_2, f"L1452. i = {i}, ii = {ii}")
            vecsum_left[ii] = old_vector_left_LS
            vecsum_right[ii] = old_vector_right_LS
            vecsum_total[ii] = vecsum_left[ii] + vecsum_right[ii]
            DEBUG(debug_2, f"L1456. vecsum_left[{ii}] = {vecsum_left[ii]}")
            DEBUG(debug_2, f"L1457. vecsum_right[{ii}] = {vecsum_right[ii]}")
            DEBUG(debug_2, f"L1458. vecsum_total[{ii}] = {vecsum_total[ii]}")
    "Fingerprint (of a keyword)."
    lett = phi_lett(vector_LS)
    variance = phi_variance(vector_LS)
    ordnum = phi_ordnum(word_ST)
    print(f"phi_lett = {lett}\nphi_variance = {variance}\nphi_ordnum = {ordnum}")
    if (mode == "c"):
        data.append((loc, lett, variance, ordnum))

"Extract single digits from the four sums."
digits = [-1, -1, -1, -1]
for ii in [0, 1, 2, 3]:
    DEBUG(debug_2, f"L1467. vecsum_total[{ii}] = {vecsum_total[ii]}")
    digits[ii] = vector_hash_6(vecsum_total[ii]) % 10

"Check the digits for redundancies."
for ii in [0, 1, 2]:
    for jj in range(ii + 1, 4):
        if (digits[ii] == digits[jj]):
            print("Error: Digits %d and %d are the same." % (ii, jj))
            errorFlag = True
if not errorFlag:
    print("The digits are OK (i.e., all different from each other).\n")
elif (mode == "r") or (mode == "a"):
    print("Error: The digits are not OK.")
    if (mode == "r"):
        quit()
elif (mode == "c"):
    print("Error: The digits are not OK. (At least two digits are equal to each other.)")
    print("A possibility is to save the erroneous word-labyrinth and then")
    print("reopen it in 'alter' mode, perform an alteration that fixes the digit")
    print("crash problem, and then save that. (Note that an attempt to go through")
    print("the unaltered word-labyrinth in 'reconstruct' mode will yield error.)")
#codeword_hash = string_hash_6(str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3]))
codeword_hash = 12

if (mode == "r"):
    if (codeword_hash == the_codeword_hash):
        vestigial_BL = True
    else:
        print("L1607. ERROR: Output's hash is NOT OK.")
        print(f"codeword hash = {codeword_hash}")
        print(f"the_codeword_hash = {the_codeword_hash}")
        quit()

if (not errorFlag) and (mode == "r"):
    output_mode = ""
    while not (output_mode in ["t", "s"]):
        output_mode = input("Camouflage trellis (t) or password shuttle (s)? ")

if (not errorFlag) and (mode == "r") and (output_mode == "t"):
    camouflage_trellis(digits)

if (not errorFlag) and (mode == "r") and (output_mode == "s"):
    shuttle_pos = password_shuttle(digits)

if (mode == "c") or (mode == "a"):
    if not errorFlag:
        data[0] = ("Codeword hash:", codeword_hash)
    elif errorFlag:
        data[0] = ("Codeword hash:", -13)

if (mode == "c"):
    ans_CH = ""
    while not ((ans_CH == "y") or (ans_CH == "n")):
        ans_CH = input("Save (y/n)?")
    if ans_CH == "y":
        data.append(("Executor:", "TwoHundredWords2FourDigits_6.py"))
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
            if (len(f_ST) < 6) or not (f_ST[-5:] == ".2H4D"):
                print("Error: The filename should have extension .2H4D.")
            else:
                filename_OK = True        
        "save data in filename"
        with open(f_ST, 'w') as f:
            for item in data:
                f.write(stringify_tuple(item) + '\n')
        if not errorFlag:
            print("The new file has been written. Reconstruct the password in order to")
            print("confirm it. Do not assign the password until it has been confirmed.\n")
            print("When assigning the password, it has to be entered twice: the first")
            print("time from one camouflage trellis, the second time from another")
            print("(different) camouflage trellis.\n")
        elif errorFlag:
            print("The new file has been written. Do not reconstruct it but instead")
            print("alter it.\n")
        print("METADATA")
        print(f"Filename: {f_ST}")
        print("Executor: TwoHundredWords2FourDigits_6.py")
        print(f"Book's name: {a_book}")
        print(f"Book's author: {an_author}")
        print(f"Books' publisher: {a_publisher}")
        print(f"Book's location: {a_location}")
        "log: creation"
        antwoord_CH = ""
        while not (antwoord_CH in ["y", "n"]):
            antwoord_CH = \
                        input("\nWould you like this creation session to be logged (y/n)? ")
        if (antwoord_CH == "y"):
            "append entry to password_construction_log.txt"
            with open("password_construction_log.txt", "a") as fil_chron:
                fil_chron.write("- - - - - - - - - - - - - - - -\n")
                todays_date = date.today()
                fil_chron.write(f"Today's date: {todays_date}\n")
                fil_chron.write(f"Created a new word-labyrinth: {f_ST}\n")
            print("A brief mention has been written in password_construction_log.txt.")

if (mode == "a") and not errorFlag:
    ans_CH = ""
    while not ((ans_CH == "y") or (ans_CH == "n")):
        ans_CH = input("\nSave (y/n)? ")
    if (ans_CH == "y"):
        a_book = the_book
        an_author = the_author
        a_publisher = the_publisher
        a_location = the_location
        filename_OK = False
        while not filename_OK:
            f_ST = input("Enter filename: ")
            if (len(f_ST) < 6) or (not (f_ST[-5:] == ".2H4D")):
                print("Error: The filename should have extension .2H4D.")
            elif (f_ST == old_f_ST):
                print("Error: The altered file should have a filename that is")
                print("different from the original file's filename.")
            else:
                filename_OK = True
        "save data in file"
        with open(f_ST, "w") as f:
            for item in data:
                f.write(stringify_tuple(item) + "\n")
        print("The altered file has been saved.")
        print("When assigning the password, it has to be entered twice: the first")
        print("time from one camouflage trellis, the second time from another")
        print("(different) camouflage trellis.")
        print("METADATA")
        print("Filename: " + f_ST)
        print("Executor: TwoHundredWords2FourDigits_6.py")
        print(f"Book's name: {a_book}")
        print(f"Book's author: {an_author}")
        print(f"Book's publisher: {a_publisher}")
        print(f"Book's location: {a_location}")
        "output"
        output_mode = ""
        while not (output_mode in ["t", "s"]):
            output_mode = input("Camouflage trellis (t) or password shuttle (s)? ")
        if (output_mode == "t"):
            camouflage_trellis(digits)
        if (output_mode == "s"):
            shuttle_pos = password_shuttle(digits)
        "log: alteration"
        antwoord_CH = ""
        while not (antwoord_CH in ["y", "n"]):
            antwoord_CH = \
                    input("\nWould you like this alteration session to be logged (y/n)? ")
        if (antwoord_CH == "y"):
            "append entry to password_construction_log.txt"
            with open("password_construction_log.txt", "a") as fil_chron:
                fil_chron.write("- - - - - - - - - - - - - - - -\n")
                todays_date = date.today()
                fil_chron.write(f"Today's date: {todays_date}\n")
                fil_chron.write(f"Created through alteration: {f_ST}\n")
                fil_chron.write(f"It was modified from: {old_f_ST}\n")
                if (output_mode == "t"):
                    fil_chron.write("Output mode: trellis\n")
                elif (output_mode == "s"):
                    fil_chron.write(f"Output mode: shuttle, #{shuttle_pos}\n")
            print("A brief mention has been written in password_construction_log.txt.")

DEBUG(debug_0, f"mode = {mode}")
DEBUG(debug_0, f"errorFlag = {errorFlag}")
if (mode == "a") and errorFlag:
    answer_CH = ""
    while not (answer_CH in ["y", "n"]):
        answer_CH = input("Would you like to enter \"swift alter\" mode (\"y\", \"n\")? ")
        if not (answer_CH in ["y", "n"]):
            print("Error: please enter either \"y\" or \"n\".")
        if (answer_CH == "y"):
            print(f"Net result = {swift_alter()}")
        

if (mode == "r") and not errorFlag:
    if reconstruct_changed:
        ans_CH = ""
        while not ((ans_CH == "y") or (ans_CH == "n")):
            ans_CH = input("\nSave (y/n)? ")
        if (ans_CH == "y"):
            "save data in the file"
            with open(f_ST, "w") as f:
                for item in data:
                    f.write(stringify_tuple(item) + "\n")
            print("The corrections to the file have been written.")
    print("Close this window down when ending the session.")
    print("If the password has just been assigned then record its metadata in")
    print("the log for the post which the password has been assigned to guard.\n")    
    print("Also play some mind-clearing game or puzzle.\n")
    print("METADATA")
    print(f"Filename: {f_ST}")
    print("Executor: TwoHundredWords2FourDigits_6.py")
    print(f"Book's name: {the_book}")
    print(f"Book's author: {the_author}")
    print(f"Books' publisher: {the_publisher}")
    print(f"Book's location: {the_location}")
    "log: reconstruction"
    antwoord_CH = ""
    while not (antwoord_CH in ["y", "n"]):
        antwoord_CH = \
                input("\nWould you like this reconstruction session to be logged (y/n)? ")
    if (antwoord_CH == "y"):
        "append entry to password_construction_log.txt"
        with open("password_construction_log.txt", "a") as fil_chron:
            fil_chron.write("- - - - - - - - - - - - - - - -\n")
            todays_date = date.today()
            fil_chron.write(f"Today's date: {todays_date}\n")
            fil_chron.write(f"Reconstructed: {f_ST}\n")
            if (output_mode == "t"):
                fil_chron.write("Output mode: trellis\n")
            elif (output_mode == "s"):
                fil_chron.write(f"Output mode: shuttle, #{shuttle_pos}\n")
        print("A brief mention has been written in password_construction_log.txt.")
    "swift alter mode"
    answer_CH = ""
    while not (answer_CH in ["y", "n"]):
        answer_CH = input("Would you like to enter \"swift alter\" mode (\"y\", \"n\")? ")
        if not (answer_CH in ["y", "n"]):
            print("Error: please enter either \"y\" or \"n\".")
    if (answer_CH == "y"):
        print("Net result = " + str(swift_alter()))
"FINIS PROGRAMMATIS"
