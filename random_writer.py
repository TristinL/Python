import random
from urllib.request import urlopen

def random_seed(level, text):
    '''Returns a random seed string that is the same length as level from text.
       If level >= the length of text an error is raised (hint see assert).
       Example:
          random_seed(2, 'carp') would return ONE of the following: 'ca', 'ar', or 'rp'
    '''
    # TODO: replace pass below with your code
    start = random.randint(0, len(text)-level)
    stop = start + level
    seed = text[start:stop]
    return seed


def get_chars_following(seed, text):
    '''Given a seed and the text, return a list of all the characters that directly
       follow the seed in text.  If there are none, then an empty list is returned.
       If using regular expressions for this be careful about characters in the seed
       that are special in regular expressions.
       Example usage:
          get_chars_following('th', 'We hold these truths to be self-evident: that all men are created equal.') returns ['e', 's', 'a']
    '''
    # TODO: replace pass below with your code
    import re
##    pat = re.compile(r'([t]+[h])')
##    for word in text:
##        pattern = re.search(pat, text).start()
        
##        new_text = text.split()
##        for s in new_text:
##            pattern = re.search(pat, s)
    #print(text[pattern + len(seed)])
    follow_chars = []
    start = 0
    while start < (len(text)-len(seed)):
        start2 = text.find(seed, start)
        follow_chars.append(text[start2 + len(seed)])
        start += (start2 + len(seed))
    return follow_chars
        
##            follow_chars.append(text[start2 + len(seed)
##    print(follow_chars)
            
     
                       

def random_write(level, text, max_num_chars=40):
    '''Returns (does NOT print) max_num_chars number of randomly generated
       characters using the specified level analysis from text as follows:
       1) Create a result string that is the empty string
       2) Your program should pick level consecutive characters at random
          from text and use them as the initial seed.
       3) Repeat the following max_num_chars times:
          3.1) Make a list of every character that follows the seed in the text
               If that list is empty, then pick another random seed as described
               in Step 2 above
          3.2) Randomly pick a character c from the text
          3.3) Add c to the result string
          3.4) Remove the first character from the seed and append c to seed
    '''
    # TODO: replace pass below with your code
    import random
    import string
    
    result_string = ''
    
    rand_int_text = random.randint(0, (len(text)-level))
    initial_seed = text[rand_int_text: rand_int_text + level]
    chars_following = get_chars_following(initial_seed, text)
    while len(result_string) < max_num_chars:
        if string.ascii_letters or string.digits or ' ' not in chars_following:
            rand_int_text = random.randint(0, (len(text)-level))
            initial_seed = text[rand_int_text: rand_int_text + level]
            chars_following = get_chars_following(initial_seed, text)
        else:
            next_text_char = text[random.randint(0, len(text))]
            result_string += ''.join(next_text_char)
            initial_seed += initial_seed[1:]
            initial_seed += next_text_char
    ##        rand_next_letter = random.choice(chars_following)
            return initial_seed

def get_from_file(filename):
    '''Returns as a string the entire contents of the specified file.
       You need not handle the case of the file not existing.
    '''
    # TODO: replace pass below with your code
    with open(filename, 'r') as infile:
        lines = infile.read()
        return lines

def get_from_url(url):
    '''Fetches the page at the specified url and returns its contents
       as a plain (non-bytes) string.
       You need not handle the case of the url not existing or being invalid.
    '''
    # TODO: replace pass below with your code
    from urllib.request import urlopen
    with urlopen(url) as req:
        data = req.read()
        new_data = data.decode()
    return new_data

def merge_texts(text_specs_list):
    '''Takes a list of lists (of size 2).  The nested lists are of the
       format [string, TextType]. See below for class TextType.
       If the TextType is raw, then the string is the text.
       If the TextType is file, then the string is the name of a file to read.
       If the TextType is url, then the string is a url to read from.
       This function will combine all the texts into a single string and return it.
       Examples:
           merge_texts([["Fee fi fo fum", TextType.raw]]) returns 'Fee fi fo fum'
           merge_texts([["One fish, ", TextType.raw], ["Two fish", TextType.raw]]) returns 'One fish, Two fish'
           merge_texts([['Mitch Hedberg Jokes\n', TextType.raw], ['http://www.palmbeachstate.edu/faculty/venturap/hedberg.txt', TextType.url]])
              returns 'Mitch Hedberg Jokes\nMy fake plants died because I did not pretend to water them.\r\n\r\nFettucini alfredo is macaroni and cheese for adults.\r\n'           
    '''
    # TODO: replace pass below with your code
    result_s = ""
    for lst in text_specs_list:
        for elmt in lst[0]:
            part1 = elmt[0]
        if TextType['raw']:
            result_s += part1
        elif TextType['file']:
            filetext = get_from_file(part1)
        elif TextType['url']:
            urltext = get_from_url(part1)
        return result_s
### ============================================================================
### DO NOT CHANGE ANY CODE BELOW HERE
from enum import Enum
### Here we are simply creating an enumerated type.
### That is, we can now use TextType.raw and TextType.url as values in our program.
### This is used by the merge_texts function above.
### See https://docs.python.org/3/library/enum.html for the Python docs on enumerated types.
class TextType(Enum):
    raw  = 1
    file = 2
    url  = 3
### end class TextType
### ============================================================================
