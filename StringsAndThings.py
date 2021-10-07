'''
Created 10/5/2021
Strings and THings
Documentation
'''

def main():
    '''
    User puts in the word; word=string
    User puts in how many characters they want to be altered
    total = how many total characters are in the string 
    numberChars = amount of characters that will be altered 
    start = starting position
    direction = right or left, what direction are the "numberChars" amount of characters moved
    '''

def ls(numberChars):
    '''
    calls string and variable "numberChars" from main
    Deletes the "numberChars" amt of characters starting with the first character (leftmost)
    Inputs "numberChars" number of # at the end of the string
    return the string with "numberChars" amt of characters deleted, starting from the first character (leftmost) AND "numberChars" amt of # after the last character (rightmost)
    '''
    
def rs(numberChars):
    '''
    calls string and variable "numberChars" from main
    Deletes the "numberChars" amt of characters starting with the last character (rightmost)
    Inputs "numberChars" number of # at the beggining of the string
    return the string with "numberChars" amt of characters deleted, starting from the last character (rightmost) AND "numberChars" amt of # before the first character (leftmost)
    '''
def lc(numberChars):
    '''
    calls string and variable "numberChars" from the main
    takes "numberChars" amt of characters starting with the first character (leftmost) and moves "numberChars" amt of characters to after the last character (rightmost)
    return the string with the first "numberChars" amt of characters moved to after the last (rightmost) character
    '''
    
def rc(numberChars): 
    '''
    calls string and variable "numberChars" from the main
    takes "numberChars" amt of characters starting with the last character (rightmost)and moves "numberChars" amt of characters to before the first character (leftmost)
    return the string with the last "numberChars" amt of characters moved to before the first (leftmost) character
    '''
def mc(start,total,numberChars,direction):
    '''
    calls string and variable "numberChars", "start", "total", "direction" from the main
    starting with position start (instead of leftmost and rightmost it is start position)
    start at position "start" out of "total" and move "numberChars" amt of characters in the direction "direction"
    return the string following the above arguements
    '''
    
def rev(start,total):
    '''
    reverse order of string 
    call "start" from main, start with position "start" out of "total" 
    return the string starting with the last character (rightmost) and ending with the first (leftmost)
    '''

