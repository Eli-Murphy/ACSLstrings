     
'''
Created 10/5/2021
Strings and THings
Documentation
LS-1/RS-1/OHIO
call word from main
run through first function
return word from main
run to second function and repeat

run the program until hits wordlist:-1
'''



def ls(stringinput, numberChars):
        size = len(stringinput)
        tot = size - int(numberChars) #takes the total size of the word - how many you want to alter
        modstring = ()
        modstring = stringinput[:tot] #takes tot amt of main varaible
        stringinput = modstring + "#" * numberChars #string + #*numberFin
        return stringinput

def rs(stringinput, numberChars):
        size = len(stringinput)
        tot = size - int(numberChars) #takes the total size of the word - how many you want to alter
        stringinput = "#" * numberChars + stringinput[:tot] #string + #*numberFin
        return stringinput

def rc(stringinput, numberChars):
        size = len(stringinput)
        tot = size - int(numberChars) #takes the total size of the word - how many you want to alter
        part = stringinput[-(int(numberChars)):]    #
        stringinput = part + stringinput[:-(int(numberChars))]
        return stringinput

def lc(stringinput, numberChars):
    size = len(stringinput)
    tot = size - int(numberChars) #takes the total size of the word - how many you want to alter
    part = stringinput[:(int(numberChars))]    #
    stringinput = stringinput[:(int(numberChars))] + part 
    return stringinput
   
def mc(start,total,numberChars,direction, stringinput):
    size = len(stringinput)
    def rightrotate(subString, numberChars):
        return leftrotate(subString, len(subString) - int(numberChars))
    def leftrotate(subString, numberChars):
        return subString[(int(numberChars)) : ] + subString[0 : (int(numberChars))]
    if direction == 'L':
        start = int(start) -1
        total = int(total) + int(start)
        subString = stringinput[(int(start)):(int(total))]
        stringinput = stringinput[:(int(start))] + leftrotate(subString, numberChars) + stringinput[(int(total)):]
        return stringinput
    if direction == 'R':
        total = int(total) + int(start)
        subString = stringinput[(int(start)):(int(total))]
        stringinput = stringinput[:(int(start))] + rightrotate(subString, numberChars) + stringinput[(int(total)):]
        return stringinput
      
def rev(start, total, stringinput):
    start = int(start) -1
    total = int(total) -1                                                                 #Dealing with offset by subtracting 1
    end = int(total) + int(start)                                                          #This calculates the end point by adding the total amount of chars effected
    wordList = list(stringinput)                                                         #Converts desired word to list
    if (int(start)) > 0:
        revChar = wordList[end:(int(start))-1:-1]
    else:
        revChar = wordList[:end+1]
        revChar = revChar[::-1]
    del wordList[(int(start)):end+1]                                                #deletes section from original function
    wordList.insert((int(start)), revChar)                                          #This puts the reversed segment list into the wordList list
    flatList = [item for sublist in wordList for item in sublist]        #This flattens the list inside the list into one list            
    stringinput = ''.join(flatList) 
    return stringinput

def main():  
    try:
        functionCheck = False
        userinput = input('enter input:')
        wordlist = userinput.split('/')
        namevariable = wordlist[-1]
        size = len(namevariable)
        stringinput = wordlist[-1]
        newlist = wordlist[0:size -1]
        for word in newlist:
            if word[0:2] == "LS":      
                numberChars = int(word[3:])
                stringinput = ls(stringinput, numberChars)
                functionCheck = True
            elif word[0:2] == "RS":      
                numberChars = int(word[3:])
                stringinput = rs(stringinput, numberChars)
                functionCheck = True
            elif word[0:2] == "RC":      
                numberChars = int(word[3:])
                stringinput = rc(stringinput, numberChars)
                functionCheck = True
            elif word[0:2] == "LC":      
                numberChars = int(word[3:])
                stringinput = lc(stringinput, numberChars)
                functionCheck = True
            elif word[0:3] == "REV":      
                numberChars = int(word[4])
                total = int(word[5])
                stringinput = rev(start, total, stringinput)
                functionCheck = True
            elif word[0:2] == "MC":      
                start = int(word[3])
                total = int(word[4])
                numberChars = int(word[5])
                direction = word[6]
                stringinput = mc(start,total,numberChars,direction, stringinput)
                functionCheck = True
            else: 
                print('input error')
                break
            if functionCheck == True:
                print('Final Output:' , stringinput)
            
    except:
        print('input error')
            

if __name__ == "__main__":
    main()



