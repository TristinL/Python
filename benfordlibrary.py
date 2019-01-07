import re

DECIMAL_NUM = '123456789'
term = []
term2 = []
term3 = []

pat = re.compile('[(][)][*)][(*]')

def benford(dict_filename):
    with open('librarybooks.txt', 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            split_line = line.split()
            for elmt in split_line:
                elmt = re.sub(pat, '', elmt)
            term.append(elmt)
            for word in term:
                word = word.strip('*)')
            term2.append(word)
            for num in term2:
                num = num[:1]
            term3.append(num)
            one = 0
            two = 0
            three = 0
            four = 0
            five = 0
            six = 0
            seven = 0
            eight = 0
            nine = 0
            for number in term3[4:]:
                if number[0] == DECIMAL_NUM[0]:
                    one += 1
                elif number[0] == DECIMAL_NUM[1]:
                    two += 1
                elif number[0] == DECIMAL_NUM[2]:
                    three += 1
                elif number[0] == DECIMAL_NUM[3]:
                    four += 1
                elif number[0] == DECIMAL_NUM[4]:
                    five += 1
                elif number[0] == DECIMAL_NUM[5]:
                    six += 1
                elif number[0] == DECIMAL_NUM[6]:
                    seven += 1
                elif number[0] == DECIMAL_NUM[7]:
                    eight += 1
                elif number[0] == DECIMAL_NUM[8]:
                    nine += 1
    print(one)
    print(term3[4:])


dict_filename = 'librarybooks.txt'
benford(dict_filename)