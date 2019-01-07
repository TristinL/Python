# I believe my word count came out to low due to the fact that I split '-' twice.
# In doing so I believe I got rid of a few words I would have needed.
# Otherwise my re.sub pattern is eliminating words without me realizing.
# A difficult task this was but I enjoyed it very much.






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
            words.append(word)
        for elmt in words:
            split_elmt = elmt.split('-')
        for term in split_elmt:
            words2.append(term)
        for character in words2:
            result = re.sub(pat, '', character)
        words3.append(result)
            
             
    words3.sort()
    print(set(words3))
    print(len(set(words3)))       

            
            

dict_filename = 'cat-in-the-hat(1)'
catword(dict_filename)
