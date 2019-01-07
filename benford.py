## Please be aware that the program takes a few moments to print the counts.


import re

DECIMAL_NUM = '123456789'
pat = re.compile('[(][)][*)][(*]')

def benford():
    with open('sunspots.txt', 'r') as infile:
        lines = infile.readlines()
        term_sun_1 = []
        term_sun_2 = []
        term_sun_3 = []
        for number in lines:
            split_line = number.split()
            for elmt in split_line:
                elmt = re.sub(pat, '', elmt)
            term_sun_1.append(elmt)
            for word in term_sun_1:
                word = word.strip('*)')
            term_sun_2.append(word)
            for num in term_sun_2:
                num = num[:1]
            term_sun_3.append(num)
            one = 0
            two = 0
            three = 0
            four = 0
            five = 0
            six = 0
            seven = 0
            eight = 0
            nine = 0
            for number in term_sun_3[3:]:
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

            result_one = 0
            result_two = 0
            result_three = 0
            result_four = 0
            result_five = 0
            result_six = 0
            result_seven = 0
            result_eight = 0
            result_nine = 0

    result_one += result_one + one
    result_two += result_two + two
    result_three += result_three + three
    result_four += result_four + four
    result_five += result_five + five
    result_six += result_six + six
    result_seven += result_seven + seven
    result_eight += result_eight + eight
    result_nine += result_nine + nine

    
    with open('livejournal.txt', 'r') as infile:
        lines = infile.readlines()
        term_live_1 = []
        term_live_2 = []
        term_live_3 = []
        for number in lines:
            split_line = number.split()
            for elmt in split_line:
                elmt = re.sub(pat, '', elmt)
            term_live_1.append(elmt)
            for word in term_live_1:
                word = word.strip('*)')
            term_live_2.append(word)
            for num in term_live_2:
                num = num[:1]
            term_live_3.append(num)
            one = 0
            two = 0
            three = 0
            four = 0
            five = 0
            six = 0
            seven = 0
            eight = 0
            nine = 0
            for number in term_live_3[6:]:
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

    result_one += result_one + one
    result_two += result_two + two
    result_three += result_three + three
    result_four += result_four + four
    result_five += result_five + five
    result_six += result_six + six
    result_seven += result_seven + seven
    result_eight += result_eight + eight
    result_nine += result_nine + nine

    with open('librarybooks.txt', 'r') as infile:
        lines = infile.readlines()
        term_library_1 = []
        term_library_2 = []
        term_library_3 = []
        for line in lines:
            split_line = line.split()
            for elmt in split_line:
                elmt = re.sub(pat, '', elmt)
            term_library_1.append(elmt)
            for word in term_library_1:
                word = word.strip('*)')
            term_library_2.append(word)
            for num in term_library_2:
                num = num[:1]
            term_library_3.append(num)
            one = 0
            two = 0
            three = 0
            four = 0
            five = 0
            six = 0
            seven = 0
            eight = 0
            nine = 0
            for number in term_library_3[4:]:
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

    result_one += result_one + one
    result_two += result_two + two
    result_three += result_three + three
    result_four += result_four + four
    result_five += result_five + five
    result_six += result_six + six
    result_seven += result_seven + seven
    result_eight += result_eight + eight
    result_nine += result_nine + nine

    print(result_one)
    print(result_two)
    print(result_three)
    print(result_four)
    print(result_five)
    print(result_six)
    print(result_seven)
    print(result_eight)
    print(result_nine)


