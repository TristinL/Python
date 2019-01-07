def convert_card():
    # replace pass below with your code for prompting the user,
    # reading in the input and printing out the canonical card name
    #
    # you *must* indent all your code under this convert_card function for
    # the testing code to work

    card = input('Enter abbriviated card format: ')
    if card[0] in '23456789AKQJ':
        second_ind = 1
    elif card[0] == '1' and card[1] == '0':
        second_ind = 2
    else:
        print('Unknown')
        return
    rank = ''
    suit = ''

    if card[0] == '2':
        rank = 'Two'
    elif card[0] == '3':
        rank = 'Three'
    elif card[0] == '4':
        rank = 'Four'
    elif card[0] == '5':
        rank = 'Five'
    elif card[0] == '6':
        rank = 'Six'
    elif card[0] == '7':
        rank = 'Seven'
    elif card[0] == '8':
        rank = 'Eight'
    elif card[0] == '9':
        rank = 'Nine'
    elif card[0] == 'A':
        rank = 'Ace'
    elif card[0] == 'K':
        rank = 'King'
    elif card[0] == 'Q':
        rank = 'Queen'
    elif card[0] == 'J':
        rank = 'Jack'
    elif card[0] == '1' and card[1] == '0':
        rank = 'Ten'

    if card[1] == 'S':
        suit = 'Spades'
    elif card[1] == 'D':
        suit = 'Diamonds'
    elif card[1] == 'C':
        suit = 'Clubs'
    elif card[1] == 'H':
        suit = 'Hearts'
    elif card[1] == '0' and card[2] == 'S':
        suit = 'Spades'
    elif card[1] == '0' and card[2] == 'D':
        suit = 'Diamonds'
    elif card[1] == '0' and card[2] == 'C':
        suit = 'Clubs'
    elif card[1] == '0' and card[2] == 'H':
        suit = 'Hearts'

    print(rank + " of " + suit)


#===============================================================================
# DO NOT CHANGE BELOW THIS LINE
# It will automatically run your convert_card function when you run your code
if __name__ == '__main__':
    convert_card()
