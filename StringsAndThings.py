     
'''
Created 10/5/2021
Strings and THings
Documentation
LS-1/RS-1/OHIO
call item from main
run through first function
return item from main
run to second function and repeat

run the program until hits wordlist:-1
'''



def main():  
    try:
        functionCheck = False
        userinput = input('enter input:')
        wordlist = userinput.split('/')
        namevariable = wordlist[-1]
        size = len(namevariable)
        stringinput = wordlist[-1]
        for item in wordlist[:-1]:
            if item[0:2] == "LS":      
                numberChars = int(item[3:])
                stringinput = ls(stringinput, numberChars)
                functionCheck = True
            elif item[0:2] == "RS":      
                numberChars = int(item[3:])
                stringinput = rs(stringinput, numberChars)
                functionCheck = True
            elif item[0:2] == "RC":      
                numberChars = int(item[3:])
                stringinput = rc(stringinput, numberChars)
                functionCheck = True
            elif item[0:2] == "LC":      
                numberChars = int(item[3:])
                stringinput = lc(stringinput, numberChars)
                functionCheck = True
            elif item[0:3] == "REV":      
                numberChars = int(item[4])
                total = int(item[5])
                stringinput = rev(start, total, stringinput)
                functionCheck = True
            elif item[0:2] == "MC":      
                start = int(item[3])
                total = int(item[4])
                numberChars = int(item[5])
                direction = item[6]
                stringinput = mc(start,total,numberChars,direction, stringinput)
                functionCheck = True
            else:
                print('input error')
                break
            
        if functionCheck == True:
            print('Final Output:' , stringinput)
        else:
            print('input error')
            
    except:
        print('input error') 

def ls(stringinput, numberChars):
    size = len(stringinput)
    tot = size - int(numberChars) #takes the total size of the item - how many you want to alter
    modstring = ()
    modstring = stringinput[:tot] #takes tot amt of main varaible
    namevariable = modstring + "#" * numberChars #string + #*numberFin
    return namevariable
    
def rs(stringinput, numberChars):
    size = len(stringinput)
    tot = size - int(numberChars) #takes the total size of the item - how many you want to alter
    namevariable = "#" * numberChars + stringinput[:tot] #string + #*numberFin
    return namevariable
    
def rc(stringinput, numberChars):
    size = len(stringinput)
    tot = size - int(numberChars) #takes the total size of the item - how many you want to alter
    part = stringinput[-(int(numberChars)):]    #
    namevariable = part + stringinput[:-(int(numberChars))]
    return namevariable

def lc(stringinput, numberChars):
    size = len(stringinput)
    tot = size - int(numberChars) #takes the total size of the item - how many you want to alter
    part = stringinput[:(int(numberChars))]    #
    namevariable = stringinput[:(int(numberChars))] + part 
    return namevariable
    
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
        namevariable = stringinput[:(int(start))] + leftrotate(subString, numberChars) + stringinput[(int(total)):]
        return namevariable
    if direction == 'R':
        total = int(total) + int(start)
        subString = stringinput[(int(start)):(int(total))]
        namevariable = stringinput[:(int(start))] + rightrotate(subString, numberChars) + stringinput[(int(total)):]
        return namevariable
      
def rev(start, total, stringinput):
    start = int(start) -1
    total = int(total) -1                                                                 #Dealing with offset by subtracting 1
    end = int(total) + int(start)                                                          #This calculates the end point by adding the total amount of chars effected
    wordList = list(stringinput)                                                         #Converts desired item to list
    if (int(start)) > 0:
        revChar = wordList[end:(int(start))-1:-1]
    else:
        revChar = wordList[:end+1]
        revChar = revChar[::-1]
    del wordList[(int(start)):end+1]                                                #deletes section from original function
    wordList.insert((int(start)), revChar)                                          #This puts the reversed segment list into the wordList list
    flatList = [item for sublist in wordList for item in sublist]        #This flattens the list inside the list into one list            
    namevariable = ''.join(flatList) 
    return namevariable

if __name__ == "__main__":
    main()



