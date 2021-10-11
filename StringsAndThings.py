'''
Created 10/5/2021
Strings and THings
Documentation
'''

def main():
    '''
    User puts in the word; word=string
    word = user input that is being altered
    User puts in how many characters they want to be altered
    total = how many total characters are in the string 
    numberChars = amount of characters that will be altered 
    start = starting position
    direction = right or left, what direction are the "numberChars" amount of characters moved
    '''
    try:   
    word_string = (input('Enter word you would like altered'))
    if word_string.isalpha() == False:
        raise ValueError()
except ValueError:
    print('enter letters only')
    
try:
    numberChars = int(input('how many characters do you want altered?'))
    if not (numberChars >= 0 ):
        raise ValueError()
except ValueError:
    print ('you must enter a number')
    
try:
    start = (input('would you like to alter starting at the first or last character?'))
    if start != 'first' and start != 'last':
        raise ValueError()
except ValueError:
    print('invalid, please chose either first or last')

if start == 'first':
    word = word_string.split()
    sliced = word_string[numberChars:]
    print('your word:', sliced)

if start == 'last':
    word = word_string.split()
    sliced = word_string[:-numberChars]
    print('your word:', sliced)
     
main()

def ls(numberChars, word):
    '''
    calls word and variable "numberChars" from main
    Deletes the "numberChars" amt of characters starting with the first character (leftmost)
    Inputs "numberChars" number of # at the end of the string
    start = before first character
    return the string with "numberChars" amt of characters deleted, starting from the first character (leftmost) AND "numberChars" amt of # after the last character (rightmost)
    '''
    
def rs(numberChars, word):
    '''
    calls word and variable "numberChars" from main
    Deletes the "numberChars" amt of characters starting with the last character (rightmost)
    Inputs "numberChars" number of # at the beggining of the string
    start = after last character
    return the string with "numberChars" amt of characters deleted, starting from the last character (rightmost) AND "numberChars" amt of # before the first character (leftmost)
    '''
def lc(numberChars, word):
    '''
    calls word and variable "numberChars" from the main
    takes "numberChars" amt of characters starting with the first character (leftmost) and moves "numberChars" amt of characters to after the last character (rightmost)
    start = before first character
    return the string with the first "numberChars" amt of characters moved to after the last (rightmost) character
    '''
    
def rc(numberChars, word): 
    '''
    calls word and variable "numberChars" from the main
    takes "numberChars" amt of characters starting with the last character (rightmost)and moves "numberChars" amt of characters to before the first character (leftmost)
    start = after last character
    return the string with the last "numberChars" amt of characters moved to before the first (leftmost) character
    '''
def mc(start,total,numberChars,direction, word):
    '''
    calls word and variable "numberChars", "start", "total", "direction" from the main
    start = before position inputted (instead of leftmost and rightmost it is start position)
    start at position "start" out of "total" and move "numberChars" amt of characters in the direction "direction"
    return the string following the above arguements
    '''
    
def rev(start, total, word):
    '''
    reverse order of word 
    call word from main, start with position "start" out of "total" 
    return the string starting with the last character (rightmost) and ending with the first (leftmost)
    '''

