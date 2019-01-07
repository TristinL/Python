import re

#open file to read
def catword(dict_filename):
    with open('cat-in-the-hat(1).txt', 'r') as infile:
        lines = infile.readlines()
#establish that lines is an array of many lists
    words = []
    words2 = []
    words3 = []
    pat = re.compile('[^a-z]')
#create empty lists in which to put the unique words
    for line in lines:
        split_line = line.split()
        for word in split_line:
            word.split('-')
        words.append(word)
        for elmt in words:
            split_elmt = elmt.split('-')
        for term in split_elmt:
            words2.append(term)
        for character in words2:
            result = re.sub(pat, '', character)
##            if '!' in character:
##                result = re.sub([!], '', character)
##            elif '?' in character:
##                result = re.sub('?', '', character)
##            elif ',' in character:
##                result = re.sub(',', '', character)
##            elif '"' in character:
##                result = re.sub('"', '', character)
##            elif '.' in character:
##                result = re.sub('.', '', character)
##            elif '..' in character:
##                result = re.sub('..', '', character)
##            elif '...' in character:
##                result = re.sub('...', '', character)
        words3.append(result)
            
             

    words3.sort()
    print(set(words3))
    print(len(set(words3)))
##    words2 = words2.append(words)
##    words2 = list(words2)
##    print(words2)    
##    print(len(words2))
##        

            
            

dict_filename = 'cat-in-the-hat(1)'
catword(dict_filename)
