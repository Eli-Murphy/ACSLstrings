     
'''
Created 10/5/2021
Strings and THings
Documentation
LS-1/RS-1/OHIO
'''

'''
try:
    functionCheck = False
    userInput = input("Input Here > ")
    listInput = userInput.split("/")
    stringInput = listInput[-1]
    newList = listinput[0:inputlength -1]
    for item in newlist:
        if item[0:2] == "LS"
            shiftDistance = int(item[3:1])
            stringInput = LS_X(stringInput, shiftDistance)
            functionCheck = True
        elif item[0:2] == "RS":
            shiftDistance = int(item[3:1])
            stringInput = RS_X(stringInput, shiftDistance)
            functionCheck = True
        elif item[0:2] == "LC"
'''

#def ls(numberChars, word):
'''
    calls word and variable 'numberChars' from main
    Deletes the 'numberChars' amt of characters starting with the first character (leftmost)
    Inputs 'numberChars' number of # at the end of the string
    start = before first character
    return the string with 'numberChars' amt of characters deleted, starting from the first character (leftmost) AND 'numberChars' amt of # after the last character (rightmost)
    
    part = 0
    final = 0
    part = word[0:numberChars] 
    final = 'lc version:' , word[numberChars:] + part
    return final
'''


def main():  
    numberChars = 0
    final = 0
    newfinal = 0
    secondfunction = 0
    namevariable = 0
    wordlist = 0  
    thirdfunction = 0
    word = input('enter word you would like altered')
    wordlist = word.split('/')
    namevariable = wordlist[-1]
    secondfunction = wordlist[1]
    thirdfunction = wordlist[2]
    
    if word[0:2] == "LS":       #isolates spots in list
        numberChars = word[3:4]
        size = len(namevariable)
        numberFin = int(float(numberChars)) #turns numberChars into an integer float value
        tot = size - numberFin #takes the total size of the word - how many you want to alter
        modstring = ()
        modstring = namevariable[:tot] #takes tot amt of main varaible
        final = modstring + "#" * numberFin #string + #*numberFin
    
    elif word[0:2] == "RS":
        finalstring = ()
        numberChars = word[3:4] #spots in list
        size = len(namevariable) #how many characters in the name
        numberFin = int(float(numberChars)) #turns numberChars into an integer float value
        tot = size - numberFin #takes the total size of the word - how many you want to alter
        final = "#" * numberFin + namevariable[:tot] #*numberFin + string
    
    elif word[0:2] == "LC":
        numberChars = word[3:4] #spots in list
        size = len(namevariable)    #characters in word
        numberFin = int(float(numberChars)) #turns numberChars into an integer float value
        part = namevariable[0:numberFin]    #isolates numberFin amt of characters from namevariable
        final = namevariable[numberFin:] + part 
    
    elif word[0:2] == "RC":
        numberChars = word[3:4] #isolates spot in list
        size = len(namevariable)    #amt of characters in list
        numberFin = int(float(numberChars)) #turns numberChars into an integer float value
        part = namevariable[-numberFin:]    #
        final = part + namevariable[:-numberFin]
        
    elif word[0:2] == "MC":
        start = word[3:4]
        total = word[4:5]
        numberChars = word[5:6]
        direction = word[6:7]
        startFin = int(float(start))
        size = len(namevariable)
        numberFin = int(float(numberChars))
        totalFin = int(float(total))
        def rightrotate(subString, numberFin):
            return leftrotate(subString, len(subString) - numberFin)
        def leftrotate(subString, numberFin):
            return subString[numberFin : ] + subString[0 : numberFin]
        if direction == 'L':
            startFin = startFin -1
            totalFin = totalFin + startFin
            subString = namevariable[startFin:totalFin]
            final = namevariable[:startFin] + leftrotate(subString, numberFin) + namevariable[totalFin:]
            return final
        if direction == 'R':
            totalFin = totalFin + startFin
            subString = namevariable[startFin:totalFin]
            final = namevariable[:startFin] + rightrotate(subString, numberFin) + namevariable[totalFin:]
            
    elif word[0:3] == "REV":
        start = word[4:5]
        total = word[5:6]
        startFin = int(float(start))
        size = len(namevariable)
        numberFin = int(float(numberChars))
        totalFin = int(float(total))
        startFin = startFin -1
        totalFin = totalFin -1                                                                 #Dealing with offset by subtracting 1
        end = startFin + totalFin                                                             #This calculates the end point by adding the total amount of chars effected
        wordList = list(namevariable)                                                         #Converts desired word to list
        if startFin > 0:
            revChar = wordList[end:startFin-1:-1]
        else:
            revChar = wordList[:end+1]
            revChar = revChar[::-1]
        del wordList[startFin:end+1]                                                #deletes section from original function
        wordList.insert(startFin, revChar)                                          #This puts the reversed segment list into the wordList list
        flatList = [item for sublist in wordList for item in sublist]        #This flattens the list inside the list into one list            
        final = ''.join(flatList)                                                          #This converts the list into a strin
    else:
        print('try again')
        
    if secondfunction[0:2] == "LS":
        numberChars = secondfunction[3:4]
        size = len(final)
        numberFin = int(float(numberChars))
        tot = size - numberFin
        modstring = ()
        modstring = final[tot:]
        newfinal = modstring + "#" * numberFin
        
    elif secondfunction[0:2] == "LC":
        numberChars = secondfunction[3:4]
        size = len(final)
        numberFin = int(float(numberChars))
        part = final[0:numberFin] 
        newfinal = final[numberFin:] + part
    
    elif secondfunction[0:2] == "RS":
        finalstring = ()
        numberChars = secondfunction[3:4]
        size = len(final)
        numberFin = int(float(numberChars))
        tot = size - numberFin
        newfinal = "#" * numberFin + final[-tot:]
        
    
    elif secondfunction[0:2] == "RC":
        numberChars = secondfunction[3:4]
        size = len(final)
        numberFin = int(float(numberChars))
        part = final[-numberFin:]
        newfinal = part + final[:-numberFin]
    
    elif secondfunction[0:2] == "MC":
        start = secondfunction[3:4]
        total = secondfunction[4:5]
        numberChars = secondfunction[5:6]
        direction = secondfunction[6:7]
        startFin = int(float(start))
        size = len(final)
        numberFin = int(float(numberChars))
        totalFin = int(float(total))
        def rightrotate(subString, numberFin):
            return leftrotate(subString, len(subString) - numberFin)
        def leftrotate(subString, numberFin):
            return subString[numberFin : ] + subString[0 : numberFin]
        if direction == 'L':
            startFin = startFin -1
            totalFin = totalFin + startFin
            subString = final[startFin:totalFin]
            newfinal = final[:startFin] + leftrotate(subString, numberFin) + final[totalFin:]
            return newfinal
        if direction == 'R':
            totalFin = totalFin + startFin
            subString = final[startFin:totalFin]
            newfinal = final[:startFin] + rightrotate(subString, numberFin) + final[totalFin:]
    
    elif secondfunction[0:3] == "REV":
        start = secondfunction[4:5]
        total = secondfunction[5:6]
        startFin = int(float(start))
        size = len(final)
        numberFin = int(float(numberChars))
        totalFin = int(float(total))
        startFin = startFin -1
        totalFin = totalFin -1                                                                 #Dealing with offset by subtracting 1
        end = startFin + totalFin                                                             #This calculates the end point by adding the total amount of chars effected
        wordList = list(final)                                                         #Converts desired word to list
        if startFin > 0:
            revChar = wordList[end:startFin-1:-1]
        else:
            revChar = wordList[:end+1]
            revChar = revChar[::-1]
        del wordList[startFin:end+1]                                                #deletes section from original function
        wordList.insert(startFin, revChar)                                          #This puts the reversed segment list into the wordList list
        flatList = [item for sublist in wordList for item in sublist]        #This flattens the list inside the list into one list            
        newfinal = ''.join(flatList) 
    else:
        print('try again')    
        
    '''
    if thirdfunction[0:2] == "MC":
        newinput = ()
        newfinal = newinput
        start = thirdfunction[3:4]
        total = thirdfunction[4:5]
        numberChars = thirdfunction[5:6]
        direction = thirdfunction[6:7]
        startFin = int(float(start))
        size = len(newinput)
        numberFin = int(float(numberChars))
        totalFin = int(float(total))
        def rightrotate(subString, numberFin):
            return leftrotate(subString, len(subString) - numberFin)
        def leftrotate(subString, numberFin):
            return subString[numberFin : ] + subString[0 : numberFin]
        if direction == 'L':
            startFin = startFin -1
            totalFin = totalFin + startFin
            subString = newinput[startFin:totalFin]
            newfinal = newinput[:startFin] + leftrotate(subString, numberFin) + newinput[totalFin:]
            return newinput
        if direction == 'R':
            totalFin = totalFin + startFin
            subString = newinput[startFin:totalFin]
            newfinal = newfinal[:startFin] + rightrotate(subString, numberFin) + newinput[totalFin:]
    '''#1
    print(newfinal)
        
if __name__ == "__main__":
    main()

    '''
    except ValueError:
        print('enter letters only')

    try:
        numberChars = int(input('how many times do you want the characters to be rotated?'))
        if not (numberChars >= 0 ):
            raise ValueError()
    except ValueError:
        print ('you must enter a number')

    try:
        start = int(input('where would you like to start altering the string?'))
        if not (start >= 0 ):
            raise ValueError()
    except ValueError:
        print ('you must enter a number')
    
    try:
        total = int(input('how many  characters do you want to select'))
        if not (numberChars >= 0 ):
            raise ValueError()
    except ValueError:
        print ('you must enter a number')

    try:
        direction = input('what direction would you like to alter towards, L or R?')    
        if not  direction == 'L' or direction == 'l' or direction == 'r' or direction == 'R':
            raise ValueError()
    except ValueError:
        print ('you must enter either L or R')
    '''
