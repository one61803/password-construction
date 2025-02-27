"This file is called FourHundredWords2SixteenAlphanumbers_5.py."
"It was forked from FourHundredWords2SixteenAlphanumbers_4.py."
"""Objective: Add an output and a log section to the end of
mode alter.
Also: updating help_intro, turning it into a help scroll.
Also: propagating an update of the inputting system from
FourHundredWords2FourDigits_11.py hither.
Also: add swift_alter function and call it at the conclusion of
reconstruct mode. (Not at the conclusion of alter mode. Why not?
swift_alter is called at the end of alter mode in 4H4D(11) because
creating a new (word-labyrinth that outputs a) four-digit password
is always risky because there is a liability for a 'digit crash'.
The chance of not having a digit crash is (10*9*8*7)/(10*10*10*10)
 = 50.4%.)
 Also: new NATO_alphanumber and NATO_spell_out functions for help
 with outputting alphanumberic passwords."""
import random
import time
from datetime import date

"A filename (of a file processed by the program) should have extension .4H16A."
"The output password has password entropy 16*lg(62) = 95.2."
"The input consists of 400 eight-letter words, uppercase."
"The output consists of sixteen alphanumeric characters."

"""SUMMARY OF PROGRAM'S ATTRIBUTES
Name: FourHundredWords2SixteenAlphanumbers_5.py
Extension of password constructing file: .4H16A
Input work level: 400 words
Output password entropy: 95.2 bits"""

def neo_code(ch):
    "0=0, 1=1, ..., 9=9, A=10, B=11, ..., Y=34, Z=35, a=36, b=37, ..., y=60, z=61"
    if ((ord(ch) >= 48) and (ord(ch) <= 57)):
        return ord(ch) - 48
    elif ((ord(ch) >= 65) and (ord(ch) <= 90)):
        return ord(ch) - 55
    elif ((ord(ch) >= 97) and (ord(ch) <= 122)):
        return ord(ch) - 61
    else:
        print("L30. ERROR in neo_code.")

def transnumeration(word_st):
    "Convert an 8-string of capital letters to an 8-list numbers (each one from 1 to 26)." 
    lst = []
    for i in range(len(word_st)):
        ch = word_st[i]
        lst.append(neo_code(ch))
    if len(lst) == 8:
        return lst
    else:
        print("L41. ERROR in transnumeration.")

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
    if num >= 0:
        while new_num > 61:
            new_num = new_num - 62
        return new_num
    elif num < 0:
        print("L65. ERROR in neo_mod: argument num < 0")
    else:
        print("L67. ERROR in neo_mod: argument is not a number.")

def vector_sum(word1_LS, word2_LS):
    "Adds two 8-lists of natural numbers component-wise modulo 62."
    new_word_LS = []
    for i in range(len(word1_LS)):
        num1 = word1_LS[i]
        num2 = word2_LS[i]
        new_word_LS.append(neo_mod(num1 + num2))
    return new_word_LS

def to_char(num):
    "Converts a number from 0 to 61 amphi-inclusive into a character of three types: (1) a digit,\
    (2) an uppercase letter, (3) a lowercase letter. (The letters belonging to the English alphabet.)"
    if ((num >= 0) and (num <= 9)):
        return chr(48 + num)
    elif ((num >= 10) and (num <= 35)):
        return chr(55 + num)
    elif ((num >= 36) and (num <= 61)):
        return chr(61 + num)
    else:
        print("L86. ERROR in to_char.")

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
        print("L104. ERROR in vector_average: argument vec_LS has length other than 8.")

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
    "Boolean-valued function which checks whether parameter param is a string or not."    
    return a_ST == str(a_ST)        

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
        print("L161. ERROR in phi_ordnum: argument word_ST is not a proper wordoid.")

"functions that are subsidiary to VAL"
def is_string_a_decimal(st):    
    "Returns True if string st contains a decimal number: two natural numbers separated by a period."
    if (st[0] == "-"):
        st = st[1:]
    pair = st.split('.')
    if (len(pair) != 2):
        return False
    else:
        return pair[0].isdigit() and pair[1].isdigit()

def is_string_a_number(st):
    "Returns True if the string contains a number."
    if (st[0] == "-"):
        st = st[1:]
    return st.isdigit() or is_string_a_decimal(st)

def string_to_fract(st):
    "Converts, e.g., '123' to 0.123: an integer into a fractional part."
    I = int(st)
    L = len(st)
    return I / 10 ** L

def string_decimal_to_number(st):
    "Converts a string containing a decimal number into that number. (It is assumed that there is no exponential notation.)"
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
    "Converts a string containing a number into the number contained by that string. (The name 'VAL'\
    is borrowed from BASIC.)"
    if is_string_a_number(st):
        if is_string_a_decimal(st):
            return string_decimal_to_number(st)
        else:
            return int(st)
    else:
        print("L223. ERROR: string argument st should contain a number.")

def string_hash_16(st):
    "Calculates a hash for string st using a method similar to vector_hash_6."
    x = 101
    Z = 9999999999999937
    for i in range(len(st)):
        if (i == 0):
            accumulator = ord(st[0])
        else:
            accumulator = ((x * accumulator) + ord(st[i])) % Z
    return accumulator

def vector_hash_16(vector_LS):
    "Calculates a polynomial in x whose coefficients are components of vector_LS, using Horner's method, \
    for the purpose of providing a hash for a string which is encoded in vector_LS."
    x = 101
    Z = 9999999999999937
    for i in range(16):
        if (i == 0):
            accumulator = vector_LS[0]
        else:
            accumulator = ((x * accumulator) + vector_LS[i]) % Z
    return accumulator

def stringify_tuple(a_tuple):
    "Packages the data in a_tuple into a string that can be written into a file, with double-semicolon \
    separators and parenthetical boundaries."    
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
            print("L230. ERROR in if_page_then_swallow: No space after the page number.")
            a_string = ""
    return a_string

def if_paragraph_then_swallow(a_string):
    "Checks a_string to see if it starts with a paragraph prefix and if it does, then removes it."    
    digits_LS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if (a_string[0:5] == "PAR. ") and (a_string[5] in digits_LS):
        a_string = a_string[5:]
        a_string = swallow_number(a_string)
        if (len(a_string) > 0) and (a_string[0] == " "):
            a_string = a_string[1:]
        else:
            print("L242. ERROR in if_paragraph_then_swallow: No space after the paragraph number.")
            a_string = ""
    return a_string

def letter_count(a_string):
    "Counts the quantity of alphanumbers in the latter (non-prefix, index-word) part of a location string."    
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
    "Checks to see if any word in a string of words has eight-letters. If it does then return False\
    else return True."    
    a_list = a_string.split(" ")
    OK = True
    while len(a_list) > 0:
        extract = a_list[0]
        a_list = a_list[1:]
        if len(extract) == 8:
            OK = False
    return OK

def print_pause(a_string):
    "Prints string a_string, then pauses for five seconds if the Boolean parameter opt is set to True.\
    (The pause is skipped if opt is False.)"    
    print(a_string)
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
        cont = input("\nPress <ENTER> to continue or < and <ENTER> to go back one page or X and <ENTER> to\nexit the help scroll.")
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
    print_pause("\n(When entering a location string in “create new” mode:) periods should only be", opt)
    print_pause("used to specify the page number (through \"P. {#} \") and the", opt)
    print_pause("paragraph number (through \"PAR. {#} \"). If the page number is specified", opt)
    print_pause("then it must be followed immediately by a specification of the paragraph", opt)
    print_pause("number; and if the paragraph number is specified then it must be preceded", opt)
    print_pause("immediately by a specification of the page number. The \"P. {#} PAR. {#} \" prefix", opt)
    print_pause("is optional and what is being prefixed is the string of index words; if there", opt)
    print_pause("is no such prefix then the index words appear by themselves. The index words", opt)
    print_pause("as they appear in the book have to be converted to all caps and any", opt)
    print_pause("punctuation among them other than spaces have to be stripped out. (Numbers", opt)
    print_pause("may be included among the index words.) The index words are words that", opt)
    print_pause("immediately precede the keyword; they \"point\" at the keyword, as it were.", opt)

def help_page_2(opt):
    "help paragraph 2"
    print_pause("\nBy keyword is meant the fill-in-the-blank word, as it were. It must be", opt)
    print_pause("exactly eight letters and converted to all caps regardless of its capitalization", opt)
    print_pause("in the book. No word among the index words may be of exactly eight letters.", opt)
    print_pause("The index words must include at least six letters among them. (There has to", opt)
    print_pause("be at least one index word.) The index words have to have the same sequence", opt)
    print_pause("that they have in the book, which is to say that no words among them", opt)
    print_pause("may be skipped when being inputted into a location string. So if there", opt)
    print_pause("is an eight-letter word among them that is required to be included in order", opt)
    print_pause("to reach at least six letters then that index–keyword pair is invalidated", opt)
    print_pause("and the user should skip past it and onto the next index–keyword pair in the", opt)
    print_pause("book.", opt)
        
def help_page_3(opt):
    "help paragraph 3"
    print_pause("\nWhen \"mining\" a given paragraph in the book for index–keyword pairs, such", opt)
    print_pause("pairs should be input sequentially in the same order that they would appear from", opt)
    print_pause("reading that paragraph normally (i.e., left-to-right in a given line and", opt)
    print_pause("top-to-bottom among the lines of a paragraph). If a location string does not", opt)
    print_pause("include page–paragraph specification then it is assumed that the same paragraph", opt)
    print_pause("is being referred to as by the previous location string.", opt)

def help_page_4(opt):
    "help paragraph 4"
    print_pause("\nWhen moving on to a new paragraph (because the current paragraph being mined", opt)
    print_pause("has run out of keywords) then the new location string should include", opt)
    print_pause("page number and paragraph number attributes of that new paragraph.", opt)
    print_pause("When starting to mine a new paragraph, no words from the previous", opt)
    print_pause("paragraph may be used as index words for any eight-letter word in", opt)
    print_pause("that new paragraph. So if the new paragraph starts with an eight-letter", opt)
    print_pause("word, then that eight-letter word must be skipped (and thereby", opt)
    print_pause("not be chosen as a keyword) because it has no index words preceding it.", opt)
    print_pause("Likewise, if the first eight-letter word of the new paragraph has", opt)
    print_pause("index words (at the beginning of the new paragraph) whose quantity of", opt)
    print_pause("letters do not reach six, then that eight-letter word must be skipped.", opt)
    print_pause("When starting to mine a new page, no words from the previous page", opt)
    print_pause("may be used as index words for eight-letter words in the new page.", opt)
    
def help_page_5(opt):
    "help paragraph 5"
    print_pause("\nThe quantity of index words to include in the location string may", opt)
    print_pause("be chosen at will, as long as the quantity of letters included among", opt)
    print_pause("them reaches at least six. When stripping an apostrophe from among", opt)
    print_pause("a sequence of index words, it may either be replaced with a space", opt)
    print_pause("or with nothing at all (i.e., the empty string); so that either", opt)
    print_pause("the two sides of the apostrophe split up into two separate words", opt)
    print_pause("or they conjoin into a single word. A hyphen between a pair of", opt)
    print_pause("words can be replaced with a space; but a hyphen breaking a single", opt)
    print_pause("word up at the end of a line can be removed, thereby joining", opt)
    print_pause("the word back together.", opt)
    
def help_page_6(opt):
    "help paragraph 6"
    print_pause("\nIt might be simpler to not use as a keyword any word that includes", opt)
    print_pause("(or is abutted by) an apostrophe (or an apostrophe and letter(s) to the", opt)
    print_pause("right of the apostrophe) (or, for that matter, any diacritic, or", opt)
    print_pause("superscripted number). Just skip it; there are plenty of other words", opt)
    print_pause("to choose from elsewhere in the text. If a word that ends in apostrophe “s”", opt)
    print_pause("has eight letters (not counting the apostrophe “s”), then to use that word", opt)
    print_pause("as an index word, replace the apostrophe with the empty string (so that the", opt)
    print_pause("“s” gets appended to the word when being inputted into the location string).", opt)
    print_pause("If a word that ends in apostrophe “s” has seven letters (not counting the", opt)
    print_pause("apostrophe “s”), then to use that word as an index word, replace the", opt)
    print_pause("apostrophe with a space (so that the “s” gets separated from the word and gets", opt)
    print_pause("treated like a separate particle); that way the word is treated as a licit", opt)
    print_pause("seven-letter word instead of as an illicit eight-letter word.", opt)

def help_page_7(opt):
    "help paragraph 7"
    print_pause("\nIf a paragraph on a given page started on the previous page then", opt)
    print_pause("the starting paragraph number for that page is 0; otherwise the", opt)
    print_pause("starting paragraph number for that page is 1. It is possible for", opt)
    print_pause("a given paragraph to have no words that may be turned into keywords.", opt)
    print_pause("It is also possible to skip a paragraph at will, for example if it", opt)
    print_pause("contains a table or a quotation or equations or a dialogue or", opt)
    print_pause("something else that makes it seem harder to deal with. An eight-letter", opt)
    print_pause("word can only be used once as a keyword for the same password.", opt)
    print_pause("If, say, some tables or dialogues in a given page make numbering paragraphs", opt)
    print_pause("harder for that given page, then it may be convenient to simply skip that", opt)
    print_pause("page (and not mine for eight-letter words in it).", opt)

def help_page_8(opt):
    "help paragraph 8"
    print_pause("\nWhat happens if one enters an erroneous location string and is", opt)
    print_pause("being prompted for the keyword belonging to that erroneous location?", opt)
    print_pause("The most expedient manner of dealing with this situation is to", opt)
    print_pause("enter \"XXXXXXXX\" as the keyword; this will immediately cancel the", opt)
    print_pause("location–keyword pair and cause a prompting for a replacement pair.", opt)
    print_pause("Otherwise there is one second (at least) to think about the", opt)
    print_pause("correctness of the pair before answering the follow-up", opt)
    print_pause("Y-or-N question. (Answering \"Y\" accepts the pair; answering", opt)
    print_pause("\"N\" rejects it.)", opt)

def help_page_9(opt):
    "help paragraph 9"
    print_pause("\nWhen a book is used for constructing a password, one should not", opt)
    print_pause("make any markings on it, either with pencil or otherwise, that", opt)
    print_pause("would facilitate constructing the password. (Example: underlining", opt)
    print_pause("keywords.) That would be considered cheating. It can be helpful", opt)
    print_pause("to choose a book that is hardcover and lays flatly open easily.", opt)
    print_pause("The data file that is used to (re)construct a password should not", opt)
    print_pause("be named after the book that its data refers to. The book should", opt)
    print_pause("be specified within the data file anyway. Instead it is better to name", opt)
    print_pause("the data file after the use that will be made of the password,", opt)
    print_pause("possibly also qualified by the date when the data file was", opt)
    print_pause("created. If the book has 366 main-text pages or more, then", opt)
    print_pause("it is possible (when constructing a new password with it) to pick a", opt)
    print_pause("page of that book based on the current day of the year. For example,", opt)
    print_pause("if a password is created on May 12 of a common year, then start", opt)
    print_pause("on page 132 of such a book, because May 12 is day 132 of a common year.", opt)

def help_page_10(opt):
    "help paragraph 10"
    print_pause("\nWhen requested to input a location string, it is possible to", opt)
    print_pause("make a query about a specific eight-letter word, to see if it", opt)
    print_pause("is already in use as a keyword or if it is acceptable to be", opt)
    print_pause("inducted into the database of keywords. In order to do this,", opt)
    print_pause("enter the question mark character (\"?\") followed by the", opt)
    print_pause("eight-letter word that is being queried about. The response", opt)
    print_pause("will be immediate (and briefly evading the entry of a", opt)
    print_pause("location string); then there will be a return to requesting", opt)
    print_pause("for an entry of a location string. If page and paragraph number", opt)
    print_pause("prefixes have already been written into the location string", opt)
    print_pause("(but without yet hitting <ENTER>) then it is possible to then type", opt)
    print_pause("\"?\" and the eight-letter word that one might have doubts about", opt)
    print_pause("in order to query about it; then all the characters preceding", opt)
    print_pause("the question mark will be ignored, as if everything before it", opt)
    print_pause("were a comment. However, this comment can be helpful to the user", opt)
    print_pause("for not losing track of what paragraph one is currently focusing", opt)
    print_pause("one's attention on. If one had entered page and paragraph", opt)
    print_pause("prefixes right before asking a question; then, after receiving", opt)
    print_pause("an answer, one can copy those same page and paragraph prefixes", opt)
    print_pause("from the line above and keep on mining for potential keywords", opt)
    print_pause("in that paragraph. So the conveniences of the mid-sentence", opt)
    print_pause("query are two: (1) not having to press backspace to", opt)
    print_pause("delete what is already in the current entry, and (2) keeping", opt)
    print_pause("what is before the question mark as a comment or prompt that can", opt)
    print_pause("then be copied at the beginning of the next entry.", opt)

def help_page_11(opt):
    "help paragraph 11"
    print_pause("\nIf an eight-letter word in the book is misspelled then ignore it,", opt)
    print_pause("just skip past it; do not employ it for constructing the password.", opt)
    print_pause("Also ignore any headlines. If a word is split between two pages and", opt)
    print_pause("immediately precedes an eight-letter word, then the latter part of it", opt)
    print_pause("(that lies at the beginning of the latter page) can be used as an index", opt)
    print_pause("if it contains at least six letters (but not exactly eight); do not prepend", opt)
    print_pause("the former part of it that lies at the end of the former page.", opt)

def help_page_12(opt):
    "help paragraph 12"
    print_pause("\nIf, while reconstructing a password for the first time (i.e., “confirming”", opt)
    print_pause("it), a flaw is noticed in a location string, then a way to deal with", opt)
    print_pause("it can be to write a note about it on a piece of paper", opt)
    print_pause("including three data: (1) the current, flawed location", opt)
    print_pause("string, (2) the “fingerprint” (a tripartite hash consisting of a", opt)
    print_pause("character, a floating-point number, and a natural number), and (3)", opt)
    print_pause("the corrected location string. When done confirming the password,", opt)
    print_pause("open the password-constructing database file with some plain-text editor;", opt)
    print_pause("use the editor’s search function to search for the each flawed", opt)
    print_pause("location string; check that the fingerprint on that line matches", opt)
    print_pause("the fingerprint that has been noted for that location string (and note that double", opt)
    print_pause("semicolons are used as separators on each record of the database (as stored", opt)
    print_pause("in the text file)); then replace the flawed location string in the", opt)
    print_pause("targeted record with the corrected location string.", opt)
    print_pause("An alternative is to open the database file with a text editor while", opt)
    print_pause("the reconstruction is still running/going on; and, whenever a flaw", opt)
    print_pause("in a location string is detected, going over to the database text file", opt)
    print_pause("and making the correction directly, without going through the", opt)
    print_pause("intermediate step of writing all the errors down on a piece of paper.", opt)

def help_page_13(opt):
    "help paragraph 13"
    print_pause("\nExample of a typical correction of a location string: prepending extra", opt)
    print_pause("index words to the substring of index words in a location string.", opt)
    print_pause("Why might one be compelled to do this? Suppose that some string of index", opt)
    print_pause("words points to more than one word in a given paragraph. Suppose that the", opt)
    print_pause("first such word (at least) that it points to is not a keyword. Then,", opt)
    print_pause("the index string should be expanded (in the only direction possible:", opt)
    print_pause("namely, backwards, i.e., leftwards) so as to disambiguate between those", opt)
    print_pause("multiple words that are being pointed to in order to pinpoint only the", opt)
    print_pause("meant keyword.", opt)

def help_page_14(opt):
    "help paragraph 14"
    print_pause("\nA possible rule of thumb for preventing such ambiguities is to include,", opt)
    print_pause("whenever possible, three words in the index string. This heuristic rule", opt)
    print_pause("should be excepted only when there are only one or two words between", opt)
    print_pause("the latest keyword and the previous eight-letter word. Because of such", opt)
    print_pause("exceptability, this rule of thumb should not be rigidly enforced by this", opt)
    print_pause("software (but it could be made to give a warning (which can be either", opt)
    print_pause("heeded or overriden)). [That has been implemented now in the latest version.]", opt)
    print_pause("Another possible error in a location string is missing the prefix for", opt)
    print_pause("page number and paragraph number when the associated index word is in", opt)
    print_pause("a different paragraph from the previous index word. There is now a", opt)
    print_pause("“??” command in creation mode that causes the last-declared page and", opt)
    print_pause("paragraph numbers to be displayed.", opt)
    print("\n")

def help_page_15(opt):
    "help paragraph 15"
    print_pause("Now there is also a “:CORRECTION:” command for both “create new” and", opt)
    print_pause("“reconstruct” modes: it allows prepending a missing page–paragraph", opt)
    print_pause("prefix to the previous entry. This is how it words for “reconstruct”", opt)
    print_pause("mode: suppose that for the current entry the user notices that", opt)
    print_pause("the location string is missing a necessary page–paragraph prefix", opt)
    print_pause("(because the keyword with the given index words cannot be found", opt)
    print_pause("in the paragraph of the previous entry). In such a case,", opt)
    print_pause("when the correct keyword is found in the correct paragraph,", opt)
    print_pause("enter the keyword. But then, when prompted for the keyword of the", opt)
    print_pause("next entry, type “:CORRECTION:” and <ENTER>. Then the user will", opt)
    print_pause("be prompted for a page number and a paragraph number; then", opt)
    print_pause("the page–paragraph prefix will be prepended to the location string", opt)
    print_pause("of that previous entry; and focus will return to the present entry.", opt)

def NATO_alphanumber(char_CH):
    "NATO phonetic alphabet: base case"
    match char_CH:
        case "A":
            return "Alpha"
        case "B":
            return "Bravo"
        case "C":
            return "Charlie"
        case "D":
            return "Delta"
        case "E":
            return "Echo"
        case "F":
            return "Foxtrot"
        case "G":
            return "Golf"
        case "H":
            return "Hotel"
        case "I":
            return "India"
        case "J":
            return "Juliett"
        case "K":
            return "Kilo"
        case "L":
            return "Lima"
        case "M":
            return "Mike"
        case "N":
            return "November"
        case "O":
            return "Oscar"
        case "P":
            return "Papa"
        case "Q":
            return "Quebec"
        case "R":
            return "Romeo"
        case "S":
            return "Sierra"
        case "T":
            return "Tango"
        case "U":
            return "Uniform"
        case "V":
            return "Victor"
        case "W":
            return "Whiskey"
        case "X":
            return "Xray"
        case "Y":
            return "Yankee"
        case "Z":
            return "Zulu"
        case "a":
            return "alpha"
        case "b":
            return "bravo"
        case "c":
            return "charlie"
        case "d":
            return "delta"
        case "e":
            return "echo"
        case "f":
            return "foxtrot"
        case "g":
            return "golf"
        case "h":
            return "hotel"
        case "i":
            return "india"
        case "j":
            return "juliett"
        case "k":
            return "kilo"
        case "l":
            return "lima"
        case "m":
            return "mike"
        case "n":
            return "november"
        case "o":
            return "oscar"
        case "p":
            return "papa"
        case "q":
            return "quebec"
        case "r":
            return "romeo"
        case "s":
            return "sierra"
        case "t":
            return "tango"
        case "u":
            return "uniform"
        case "v":
            return "victor"
        case "w":
            return "whiskey"
        case "x":
            return "xray"
        case "y":
            return "yankee"
        case "z":
            return "zulu"
        case "1":
            return "1ne"
        case "2":
            return "2wo"
        case "3":
            return "3hree"
        case "4":
            return "4our"
        case "5":
            return "5ive"
        case "6":
            return "6ix"
        case "7":
            return "7even"
        case "8":
            return "8ight"
        case "9":
            return "9ine"
        case "0":
            return "0ero"

def NATO_spell_out(string_ST):
    "NATO (phonetic alphabet) spelling-out of argument string_ST."
    spell_out = ""
    while (len(string_ST) > 0):
        char_CH = string_ST[0:1]
        string_ST = string_ST[1:]
        spell_out += NATO_alphanumber(char_CH) + " "
        if (len(string_ST) in [12, 8, 4]):
            spell_out += "\n"
    return spell_out

def swift_alter():
    "Swift alteration mode. Assumed global variables: data, the_book, the_author, the_publisher, the_codeword_hash, old_f_ST, keywords_LS, upper_bound."
    "(MAIN)"
    old_vector_left_LS = [0, 0, 0, 0, 0, 0, 0, 0]
    old_vector_right_LS = [0, 0, 0, 0, 0, 0, 0, 0]
    "ignore prefix"
    for i in range(1, upper_bound + 1):
        "mode: alter"
        if not (i in [100, 200, 300]) and not (is_toy_version and (i in [10, 20, 30])):
            print(f"\nLocation #{i}: {data[i][0]}")
            word_ST = keywords_LS[i - 1]
            print(f"Keyword #{i}: {word_ST}")
            vec_LS = transnumeration(word_ST)
            lett0 = phi_lett(vec_LS)
            variance0 = phi_variance(vec_LS)
            ordnum0 = phi_ordnum(word_ST)
            if (data[i][1] == lett0) and (data[i][2] == variance0) and (data[i][3] == ordnum0):
                print("Fingerprint OK.")
            else:
                print("Error: Fingerprint not OK.")
                quit()
        elif (i in [100, 200, 300]) or (is_toy_version and (i in [10, 20, 30])):
            word_ST = ""
            while not is_proper_keyword(word_ST):
                word_ST = input(f"\nEnter some all-caps eight-letter word for location {i}: ")
                if not is_proper_keyword(word_ST):
                    print("Error: Please enter an eight-letter word in all caps.")
            vec_LS = transnumeration(word_ST)
            lett0 = phi_lett(vec_LS)
            variance0 = phi_variance(vec_LS)
            ordnum0 = phi_ordnum(word_ST)
            data[i] = (word_ST + " =", lett0, variance0, ordnum0)
            print(f"Alteration at location {i} has been done.")
        "Add to previous word."
        vector_LS = transnumeration(word_ST)
        vecsum_left_LS = vector_sum(old_vector_left_LS, vector_LS)
        old_vector_left_LS = left_rotate(vecsum_left_LS)
        vecsum_right_LS = vector_sum(old_vector_right_LS, vector_LS)
        old_vector_right_LS = right_rotate(vecsum_right_LS)
        if (i == 400) or (is_toy_version and (i == 40)):
            vecsum_left_400 = old_vector_left_LS
            vecsum_right_400 = old_vector_right_LS
            vecsum_total_400 = vecsum_left_400 + vecsum_right_400
        "Fingerprint (of a keyword)."
        lett = lett0
        variance = variance0
        ordnum = ordnum0
        #data[i] = (word_ST + " =", lett, variance, ordnum)
        print(f"phi_lett = {lett}\nphi_variance = {variance}\nphi_ordnum = {ordnum}")
        time.sleep(1)
    "outputting"
    output = transcharacterization(vecsum_total_400)
    #output = output.upper()
    codeword_hash = string_hash_16(output)
    print(f"\nThe password is {output}")
    print(f"\nNATO alphanumeric spell-out of the password: {NATO_spell_out(output)}")
    data[0] = ("Codeword hash:", codeword_hash)
    "save?"
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
            if (len(f_ST) < 7) or not (f_ST[-6:] == ".4H16A"):
                print("Error: The filename should have extension .4H16A.")
            elif (f_ST == old_f_ST):
                print("Error: The altered file should have a different filename from the original file.")
            else:
                filename_OK = True
        "save data in file"
        with open(f_ST, "w") as f:
            for item in data:
                f.write(stringify_tuple(item) + "\n")
        print("The altered file has been written.")
        print("When assigning the password, it has to be entered twice. The first time from,")
        print("e.g., a handwritten copy; the second time from, e.g., a photographic copy")
        print("(taken by smartphone) or else a second handwritten copy (independent of the first).\n")
        print("METADATA")
        print(f"Filename: {f_ST}")
        print("Executor: FourHundredWords2SixteenAlphanumbers_5.py")
        print(f"Book's name: {a_book}")
        print(f"Book's author: {an_author}")
        print(f"Book's publisher: {a_publisher}")
        print(f"Book's location: {a_location}")
        "log: swift alteration"
        antwoord_CH = ""
        while not (antwoord_CH in ["y", "n"]):
            antwoord_CH = input("\nWould you like this alteration episode to be logged (y/n)? ")
        if (antwoord_CH == "y"):
            "append entry in password_construction_log.txt"
            with open("password_construction_log.txt", "a") as fil_chron:
                fil_chron.write("- - - - - - - - - - - - - - - -\n")
                todays_date = date.today()
                fil_chron.write(f"Today's date: {todays_date}\n")
                fil_chron.write(f"Created through swift alteration: {f_ST}\n")
                fil_chron.write(f"It was modified from: {old_f_ST}\n")
            print("A brief mention has been written in password_construction_log.txt.")                   
        return 1

def DEBUG(flag_BL, line_NT, msg_ST):
    "If flag_BL is True then prints line number line_NT followed by message msg_ST."
    if flag_BL:
        print(f"L{line_NT}. {msg_ST}")

def what_prefix(datum_ST):
    "Extracts the page–paragraph prefix from datum_ST and returns it."
    index_word_string = if_paragraph_then_swallow(if_page_then_swallow(datum_ST))
    prefix_length_NT = len(datum_ST) - len(index_word_string)
    the_prefix_ST = datum_ST[0:prefix_length_NT]
    return the_prefix_ST
            

"PRE-MAIN"

data = []
"LOAD?"
mode = ""
while not (mode in ['c', 'r', 'a']):
    mode = input("Create new (c), reconstruct (r), or alter (a)? ")
if (mode == "r") or (mode == "a"):
    filename_OK = False
    while not filename_OK:
        f_ST = input("Enter filename: ")
        if (len(f_ST) < 7) or not (f_ST[-6:] == ".4H16A"):
            print("Error: The filename's extension should be .4H16A.")
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
                        print("L308. ERROR: Not an approved first element for an ordered pair.")
                    if (line_LS[0] == "Executor:") and (not line_LS[1] == "FourHundredWords2SixteenAlphanumbers_5.py"): 
                        print("L310. ERROR: I am not the executor of this file.")
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
                        print(f"Codeword hash: {the_codeword_hash}\n")
                    data.append((line_LS[0], line_LS[1]))                        
                else:
                    print(f"L329. len(line_LS) = {len(line_LS)}")
                    print("L330. ERROR")
            else:
                print("L332. ERROR: Line is not wrapped in parentheses.")
    print("File has been loaded.")

    if (mode == "a"):
        old_f_ST = f_ST
    elif (mode == "r"):
        reconstruct_changed = False
        old_f_ST = f_ST                  # might be used in swift_alter


"MAIN"
is_toy_version = False          # This line is user-modifiable; the RHS should be either True or False.
if (mode == "c"):
    data = [0]
    keywords_LS = []
elif (mode == "r") or (mode == "a"):
    keywords_LS = []
old_vector_left_LS = [0, 0, 0, 0, 0, 0, 0, 0]
old_vector_right_LS = [0, 0, 0, 0, 0, 0, 0, 0]
if is_toy_version:
    print("This execution is in toy mode.")
    upper_bound = 40
else:
    upper_bound = 400
if (mode == "c"):
    print("Type \":HELP:\" and <ENTER> for explanatory help.")
older_prefix = ""
prefix = ""
prefix_changed = False
for i in range(1, upper_bound + 1):
    if (mode == "c"):
        "mode: create new"
        enter_loop_BL = True
        while enter_loop_BL:
            loc = input(f"\nInput location #{i}: ")
            prefix_changed = False      # pref.
            if (loc == ":HELP:"):
                help_intro()
                OK = True
                #respuesta = "N"
                word_ST = "ZZZZZZZZ"
            elif (i > 1) and (loc == ":CORRECTION:"):
                print(f"Current previous (#{i - 1}) location string: {data[i - 1][0]}")
                if (data[i - 1][0].count(".") == 0):
                    page_num = input("Enter the page number: ")
                    par_num = input("Enter the paragraph number: ")
                    new_prefix = f"P. {page_num} PAR. {par_num} "
                    if not (new_prefix == prefix):
                        data[i - 1] = (new_prefix + data[i - 1][0], data[i - 1][1], data[i - 1][2], data[i - 1][3])
                        print(f"New previous (#{i - 1}) location string: {data}")
                        prefix = new_prefix
                        older_prefix = prefix
                        word_ST = "ZZZZZZZZ"
                        OK = True
                        respuesta = "N"                        
                    else:
                        print("Error: The same location prefix should not be repeated.")                 
                elif (data[i - 1][0].count(".") == 2):
                    page_num = input("Enter the new page number: ")
                    par_num = input("Enter the new paragraph number: ")
                    new_prefix = f"P. {page_num} PAR. {par_num} "
                    new_datum = data[i - 1][0].replace(what_prefix(data[i - 1][0]), new_prefix)
                    data[i - 1] = (new_datum, data[i - 1][1], data[i - 1][2], data[i - 1][3])
                    prefix = new_prefix
                    older_prefix = prefix
                    print(f"New previous (#{i - 1}) location string: {data[i - 1][0]}")
                    word_ST = "ZZZZZZZZ"
                    OK = True
                    respuesta = "N"       
                else:
                    print(f"L906. ERROR: Wrong number of periods ({data[i - 1][0].count('.')}) in the location string.")
            elif (i == 1) and (loc == ":CORRECTION:"):
                print("Error: it is not possible to correct a non-existent zeroth entry.")
                word_ST = "ZZZZZZZZ"
                OK = True
                respuesta = "N"
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
                        print("Specification of paragraph number should be immediately preceded")
                        print("by a specification of page number. I.e., a \"PAR. {#} \" prefix")
                        print("should be immediately preceded by a \"P. {#} \" prefix.")
                    elif (loc[0:3] == "P. ") and (loc[3:4].isdigit()):
                        print("Specification of page number should be immediately followed")
                        print("by a specification of paragraph number. I.e., a \"P. {#} \" prefix")
                        print("should be immediately followed by a \"PAR. {#} \" prefix.")
                    else:
                        print("Type :HELP: and <ENTER> for explanatory help.")
                OK = True
                respuesta = "N"
                word_ST = "ZZZZZZZZ"
            elif not is_UALPHAnumeric(if_paragraph_then_swallow(if_page_then_swallow(loc)).replace(" ", "")):
                print("Error: After (optionally) specifying the page number (through \"P. {#} \")")
                print("and (included as part of the option) specifying the paragraph number")
                print("(through \"PAR. {#} \"), the remainder of the location string should")
                print("consist only of spaces, digits, and uppercase letters (containing at least")
                print("six non-spaces). Please try again.")
                OK = True
                respuesta = "N"
                word_ST = "ZZZZZZZZ"
            elif (letter_count(loc) < 6):
                if (letter_count(loc) == -9):
                    print("Error: No word in the index should have exactly eight letters. Please try again.")
                else:
                    print("Error: Index word(s) should have at least six letters among them. Please try again.")
                OK = True
                respuesta = "N"
                word_ST = "ZZZZZZZZ"
            elif (index_word_count(loc) < 3):
                print("Warning: The quantity of index words is less than three.")
                response = ""
                while not (response in ["CONTINUE", "RETRY"]):
                    response = input("Continue anyway (\"CONTINUE\") or retry (\"RETRY\")? ")
                    if not (response in ["CONTINUE", "RETRY"]):
                        print("Error: type either \"CONTINUE\" or \"RETRY\" and then press <ENTER>.")
                if (response == "RETRY"):
                    OK = True
                    respuesta = "N"
                    word_ST = "ZZZZZZZZ"
                elif (response == "CONTINUE"):
                    OK = False
                    "update of prefix: 'create new' mode > 'CONTINUE' case"
                    if (len(what_prefix(loc)) > 0):
                        if (what_prefix(loc) == prefix):
                            print("Error: The prefix has been repeated, but the location string is now\nbeing automatically corrected.")
                            loc = loc[len(prefix):]
                        else:
                            older_prefix = prefix
                            prefix = what_prefix(loc)
                            prefix_changed = True
                    else:
                        oldex_prefix = prefix
            else:
                OK = False
                "update of prefix: 'create new' mode"
                if (len(what_prefix(loc)) > 0):
                    if (what_prefix(loc) == prefix):
                        print("Error: The prefix has been repeated; but the location string is now\nbeing automatically corrected.")
                        loc = loc[len(prefix):]
                    else:
                        older_prefix = prefix
                        prefix = what_prefix(loc)
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
                            print("Error: Please enter an eight-letter word in all caps (or \"XXXXXXXX\" to cancel).")
                OK = True
            if (word_ST == "XXXXXXXX"):
                OK = True
                respuesta = "N"
                print("The index–keyword pair has been canceled.")
                if prefix_changed:
                    prefix = older_prefix
            elif (word_ST == "ZZZZZZZZ"):
                OK = True
                respuesta = "N"
                if prefix_changed:
                    prefix = older_prefix
            elif (word_ST in keywords_LS):
                OK = True
                respuesta = "N"
                print("Please use a keyword that is different from any previous keyword.")
                if prefix_changed:
                    prefix = older_prefix
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
        keywords_LS.append(word_ST)                
    elif (mode == "r"):
        "mode: reconstruct"
        print("\nLocation #" + str(i) + ": " + data[i][0])
        OK = False
        "update of prefix: 'reconstruct' mode"
        datum = data[i][0]
        if (len(what_prefix(datum)) > 0):
            if (what_prefix(datum) == prefix):
                print("Error: The prefix has been repeated; but the location string is now\nbeing automatically corrected.")
                new_datum = datum[len(prefix):]
                data[i] = (new_datum, data[i][1], data[i][2], data[i][3])
            else:
                prefix = what_prefix(datum)
        while not OK:
            word_ST = ""
            while not is_proper_keyword(word_ST):
                word_ST = input(f"Keyword #{i}: ")
                if not is_proper_keyword(word_ST):
                    if (i > 1) and (word_ST == ":CORRECTION:"):
                        print(f"Current previous (#{i - 1}) location string: {data[i - 1][0]}")
                        if (data[i - 1][0].count(".") == 0):
                            page_num = input("Enter the page number: ")
                            par_num = input("Enter the paragraph number: ")
                            new_prefix = f"P. {page_num} PAR. {par_num} "
                            if not (new_prefix == prefix):
                                data[i - 1] = (new_prefix + data[i - 1][0], data[i - 1][1], data[i - 1][2], data[i - 1][3])
                                print(f"New previous (#{i - 1}) location string: {data[i - 1][0]}")
                                reconstruct_changed = True
                                prefix = new_prefix
                            else:
                                print("Error: The same location prefix should not be repeated.")
                            print("\nNow back to the present entry.")
                            print(f"\nLocation #{i}: {data[i][0]}")
                        elif (data[i - 1][0].count(".") == 2):
                            page_num = input("Enter the new page number: ")
                            par_num = input("Enter the new paragraph number: ")
                            new_prefix = f"P. {page_num} PAR. {par_num} "
                            new_datum = data[i - 1][0].replace(what_prefix(data[i - 1][0]), new_prefix)
                            data[i - 1] = (new_datum, data[i - 1][1], data[i - 1][2], data[i - 1][3])
                            prefix = new_prefix
                            print(f"New previous (#{i - 1}) location string: {data[i - 1][0]}")
                            reconstruct_changed = True
                        else:
                            print("Error: Cannot prepend a page-number prefix to a string that already has periods in it.")
                    elif (i == 1) and (word_ST == ":CORRECTION:"):
                        print("Error: It is not possible to correct a non-existent zeroth entry.")
                    elif (word_ST == "??"):
                        if (len(prefix) > 0):
                            print(prefix)
                        else:
                            print("No page number – paragraph number prefix has been entered yet.")
                    else:                                   
                        print("Error: Please enter an eight-letter word in all caps.")
            vec_LS = transnumeration(word_ST)
            lett0 = phi_lett(vec_LS)
            variance0 = phi_variance(vec_LS)
            ordnum0 = phi_ordnum(word_ST)
            if (data[i][1] == lett0) and (data[i][2] == variance0) and (data[i][3] == ordnum0):
                print("Fingerprint OK.")
                OK = True
                keywords_LS.append(word_ST)
            else:
                print("Fingerprint not ok; try again.")
    elif (mode == "a"):
        "mode: alter"
        if not (i in [100, 200, 300]) and not (is_toy_version and (i in [10, 20, 30])):
            print(f"\nLocation #{i}: {data[i][0]}")
            OK = False
            "update of prefix: 'alter' mode"
            datum = data[i][0]
            if (len(what_prefix(datum)) > 0):
                if (what_prefix(datum) == prefix):
                    print("Error: The prefix has been repeated; but the location string is now\nbeing automatically corrected.")
                    new_datum = datum[len(prefix):]
                    data[i] = (new_datum, data[i][1], data[i][2], data[i][3])
                else:
                    prefix = what_prefix(datum)
            while not OK:
                word_ST = ""
                while not is_proper_keyword(word_ST):
                    word_ST = input(f"Keyword #{i}: ")
                    if not is_proper_keyword(word_ST):
                        if (i > 1) and (word_ST == ":CORRECTION:"):
                            print(f"Current previous (#{i - 1}) location string: {data[i - 1][0]}")
                            if (data[i - 1][0].count(".") == 0):
                                page_num = input("Enter the page number: ")
                                par_num = input("Enter the paragraph number: ")
                                new_prefix = f"P. {page_num} PAR. {par_num} "
                                if not (new_prefix == prefix):
                                    data[i - 1] = (new_prefix + data[i - 1][0], data[i - 1][1], data[i - 1][2], data[i - 1][3])
                                    print(f"New previous (#{i - 1}) location string: {data[i - 1][0]}")
                                    reconstruct_changed = True
                                    prefix = new_prefix
                                else:
                                    print("Error: The same location prefix should not be repeated.")
                                print("\nNow back to the present entry.")
                                print(f"\nLocation #{i}: {data[i][0]}")
                            elif (data[i - 1][0].count(".") == 2):
                                page_num = input("Enter the new page number: ")
                                par_num = input("Enter the new paragraph number: ")
                                new_prefix = f"P. {page_num} PAR. {par_num} "
                                new_datum = data[i - 1][0].replace(what_prefix(data[i - 1][0]), new_prefix)
                                data[i - 1] = (new_datum, data[i - 1][1], data[i - 1][2], data[i - 1][3])
                                prefix = new_prefix
                                print(f"New previous (#{i - 1}) location string: {data[i - 1][0]}")
                                reconstruct_changed = True
                            else:
                                print("Error: Cannot prepend a page-number prefix to a string that already has periods in it.")
                        elif (i == 1) and (word_ST == ":CORRECTION:"):
                            print("Error: It is not possible to correct a non-existent zeroth entry.")
                        elif (word_ST == "??"):
                            if (len(prefix) > 0):
                                print(prefix)
                            else:
                                print("Error: Please enter an eight-letter word in all caps.")
                vec_LS = transnumeration(word_ST)
                lett0 = phi_lett(vec_LS)
                variance0 = phi_variance(vec_LS)
                ordnum0 = phi_ordnum(word_ST)
                if (data[i][1] == lett0) and (data[i][2] == variance0) and (data[i][3] == ordnum0):
                    print("Fingerprint OK.")
                    OK = True
                    keywords_LS.append(word_ST)                    
                else:
                    print("Fingerprint not ok; try again.")
        elif (i in [100, 200, 300]) or (is_toy_version and (i in [10, 20, 30])):
            word_ST = ""
            while not is_proper_keyword(word_ST):
                word_ST = input(f"\nEnter some all-caps eight-letter word for location {i}: ")
                if not is_proper_keyword(word_ST):
                    print("Error: Please enter an eight-letter word in all caps.")
            keywords_LS.append(word_ST)
            vec_LS = transnumeration(word_ST)
            lett0 = phi_lett(vec_LS)
            variance0 = phi_variance(vec_LS)
            ordnum0 = phi_ordnum(word_ST)
            data[i] = (word_ST + " =", lett0, variance0, ordnum0)
            print(f"Alteration at location {i} has been done.")
    else:
        print("L446. ERROR: variable mode should be one of c, r, a.")
                
    "Any mode: add to previous word."
    vector_LS = transnumeration(word_ST)
    vecsum_left_LS = vector_sum(old_vector_left_LS, vector_LS)
    old_vector_left_LS = left_rotate(vecsum_left_LS)
    vecsum_right_LS = vector_sum(old_vector_right_LS, vector_LS)
    old_vector_right_LS = right_rotate(vecsum_right_LS)
    if (i == 400) or (is_toy_version and (i == 40)):
        vecsum_left_400 = old_vector_left_LS
        vecsum_right_400 = old_vector_right_LS
        vecsum_total_400 = vecsum_left_400 + vecsum_right_400
    "Fingerprint (of a keyword input)."
    lett = phi_lett(vector_LS)
    variance = phi_variance(vector_LS)
    ordnum = phi_ordnum(word_ST)
    print(f"phi_lett = {lett}\nphi_variance = {variance}\nphi_ordnum = {ordnum}")
    if (mode == "c"):
        data.append((loc, lett, variance, ordnum))

"outputting"
output = transcharacterization(vecsum_total_400)
#output = output.upper()
codeword_hash = string_hash_16(output)

if (mode == "r") or (mode == "a"):
    print(f"\nThe password is {output}")
    print(f"\nNATO alphanumeric spell-out of the password: {NATO_spell_out(output)}")

if (mode == "c") or (mode == "a"):
    data[0] = ("Codeword hash:", codeword_hash)

if (mode == "r"):
    if (codeword_hash == the_codeword_hash):
        print("Output's fingerprint is OK.")
    else:
        print("L480. ERROR: Output's hash is NOT OK.")
        print("codeword_hash = " + str(codeword_hash))
        print("the_codeword_hash = " + str(the_codeword_hash))

"saving & logging"
if (mode == "c"):
    ans_CH = ""
    while not ((ans_CH == "y") or (ans_CH == "n")):
        ans_CH = input("\nSave (y/n)? ")
    if ans_CH == "y":
        data.append(("Executor:", "FourHundredWords2SixteenAlphanumbers_5.py"))
        a_book = input("\nWhat is the book's name? ")
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
            if (len(f_ST) < 7) or not (f_ST[-6:] == ".4H16A"):
                print("Error: The filename should have extension .4H16A.")
            else:
                filename_OK = True
        "save data in filename"
        with open(f_ST, 'w') as f:
            for item in data:
                f.write(stringify_tuple(item) + '\n')
        print("The new file has been written. Reconstruct the password in order to confirm it.")
        print("Do not assign the password until it has been confirmed.\n")
        print("When assigning the password, it has to be entered twice. The first time from,")
        print("e.g., a handwritten copy; the second time from, e.g., a photographic copy")
        print("(taken by smartphone) or else a second handwritten copy (independent of the first).\n")
        print("METADATA")
        print("Filename: " + f_ST)
        print("Executor: FourHundredWords2SixteenAlphanumbers_5.py")        
        print("Book's name: " + a_book)
        print("Book's author: " + an_author)
        print("Books' publisher: " + a_publisher)
        print("Book's location: " + a_location)
        "log: creation"
        antwoord_CH = ""
        while not (antwoord_CH in ["y", "n"]):
            antwoord_CH = input("\nWould you like this creation session to be logged (y/n)? ")
        if (antwoord_CH == "y"):
            "append entry in password_construction_log.txt"
            with open("password_construction_log.txt", "a") as fil_chron:
                fil_chron.write("- - - - - - - - - - - - - - - -\n")
                todays_date = date.today()
                fil_chron.write(f"Today's date: {todays_date}\n")
                fil_chron.write(f"Created a new word-labyrinth: {f_ST}\n")              
            print("A brief mention has been written in password_construction_log.txt.")          

if (mode == "a"):
    ans_CH = ""
    while not ((ans_CH == "y") or (ans_CH == "n")):
        ans_CH = input("\nSave (y/n)? ")
        if not (ans_CH in ["y", "n"]):
            print("Error: please enter either \"y\" or \"n\".")
    if (ans_CH == "y"):
        a_book = the_book
        an_author = the_author
        a_publisher = the_publisher
        a_location = the_location
        filename_OK = False
        while not filename_OK:
            f_ST = input("Enter filename: ")
            if (len(f_ST) < 7) or (not (f_ST[-6:] == ".4H16A")):
                print ("Error: The filename should have extension .4H16A.")
            elif (f_ST == old_f_ST):
                print("Error: The altered file should be different than the loaded file.")
            else:
                filename_OK = True
        "save data in file"
        with open(f_ST, "w") as f:
            for item in data:
                f.write(stringify_tuple(item) + "\n")
        print("The altered file has been saved.") #Reconstruct the password in order to confirm it.")
        #print("Do not assign the password until it has been confirmed.\n")
        print("When assigning the password, it has to be entered twice. The first time from,")
        print("e.g., a handwritten copy; the second time from, e.g., a photographic copy")
        print("(taken by smartphone) or else a second handwritten copy (independent of the first).\n")
        print("METADATA")
        print(f"Filename: {f_ST}")
        print("Executor: FourHundredWords2SixteenAlphanumbers_5.py")        
        print(f"Book's name: {a_book}")
        print(f"Book's author: {an_author}")
        print(f"Book's publisher: {a_publisher}")
        print(f"Book's location: {a_location}")
        "log: alteration"
        antwoord_CH = ""
        while not (antwoord_CH in ["y", "n"]):
            antwoord_CH = input("\nWould you like this alteration session to be logged (y/n)? ")
        if (antwoord_CH == "y"):
            "append entry in password_construction_log.txt"
            with open("password_construction_log.txt", "a") as fil_chron:
                fil_chron.write("- - - - - - - - - - - - - - - -\n")
                todays_date = date.today()
                fil_chron.write(f"Today's date: {todays_date}\n")
                fil_chron.write(f"Created through alteration: {f_ST}\n")
                fil_chron.write(f"It was modified from: {old_f_ST}\n")
            print("A brief mention has been written in password_construction_log.txt.")  

if (mode == "r"):
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
    print("Close this window down when ending the session (and delete the two")
    print("copies of the password).")
    print("If the password has just been assigned then record its metadata in")
    print("the log for the post to which the password has been assigned to guard.")    
    print("\nMETADATA")
    print(f"Filename: {f_ST}")
    print("Executor: FourHundredWords2SixteenAlphanumbers_5.py")    
    print(f"Book's name: {the_book}")
    print(f"Book's author: {the_author}")
    print(f"Books' publisher: {the_publisher}")
    print(f"Book's location: {the_location}")
    "log: reconstruction"
    antwoord_CH = ""
    while not (antwoord_CH in ["y", "n"]):
        antwoord_CH = input("\nWould you like this reconstruction episode to be logged (y/n)? ")
    if (antwoord_CH == "y"):
        "append entry in password_construction_log.txt"
        with open("password_construction_log.txt", "a") as fil_chron:
            fil_chron.write("- - - - - - - - - - - - - - - -\n")
            todays_date = date.today()
            fil_chron.write(f"Today's date: {todays_date}\n")
            fil_chron.write(f"Reconstructed: {f_ST}\n")
        print("A brief mention has been written in password_construction_log.txt.")    
    "swift alter mode"
    answer_CH = ""
    while not (answer_CH in ["y", "n"]):
        answer_CH = input("Would you like to enter \"swift alter\" mode (\"y\", \"n\")? ")
        if not (answer_CH in ["y", "n"]):
            print("Error: please enter either \"y\" or \"n\".")
    if (answer_CH == "y"):
        print("Net result = " + str(swift_alter()))  
