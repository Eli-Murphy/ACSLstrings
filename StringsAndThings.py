     
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
        userinput = input('enter input:')
        wordlist = userinput.split('/')
        stringinput = wordlist[-1]
        size = len(stringinput)
        for item in wordlist[:-1]:
            if item[0:2] == "LS":      
                numberChars = int(item[3:4])
                stringinput = ls(stringinput, numberChars)
                functionCheck = True
            elif item[0:2] == "RS":      
                numberChars = int(item[3:4])
                stringinput = rs(stringinput, numberChars)
            elif item[0:2] == "RC":      
                numberChars = int(item[3:4])
                stringinput = rc(stringinput, numberChars)
            elif item[0:2] == "LC":      
                numberChars = int(item[3:4])
                stringinput = lc(stringinput, numberChars)
            elif item[0:3] == "REV":      
                start = int(item[4:5])
                total = int(item[5:6])
                stringinput = rev(start, total, stringinput)
            elif item[0:2] == "MC":      
                start = int(item[3:4])
                total = int(item[4:5])
                numberChars = int(item[5:6])
                direction = item[6:7]
                stringinput = mc(start,total,numberChars,direction, stringinput)
            else:
                print('input error')
                break
        print('Final Output:' , stringinput)

    except:
        print('1input error') 

def ls(stringinput, numberChars):
    finalstring = ""
    tot = len(stringinput) - int(numberChars)
    finalstring = stringinput 
    stringinput = stringinput.split()
    stringinput = finalstring[-tot:] + "#" * numberChars 
    return stringinput
    
def rs(stringinput, numberChars):
    tot = len(stringinput) - int(numberChars)
    modstring = ()
    size = len(stringinput)
    modstring = stringinput[:tot]
    stringinput = "#" * numberChars + modstring     
    return stringinput
 
def rc(stringinput, numberChars):
    size = len(stringinput)
    tot = size - int(numberChars) #takes the total size of the item - how many you want to alter
    part = stringinput[-(int(numberChars)):]    #
    stringinput = part + stringinput[:-(int(numberChars))]
    return stringinput

def lc(stringinput, numberChars):
    part = stringinput[0:int(numberChars)] 
    stringinput = stringinput[int(numberChars):] + part    
    return stringinput

    
def mc(start,total,numberChars,direction, stringinput):
    start = start -1
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
    start = start - 1
    total = total - 1                                                                 #Dealing with offset by subtracting 1
    end = int(start) + int(total)                                                    #This calculates the end point by adding the total amount of chars effected
    wordList = list(stringinput)                                                         #Converts desired item to list
    if int(start) > 0:
        revChar = wordList[int(end):int(start - 1):-1]
    else:
        revChar = wordList[:int(end + 1)]
        revChar = revChar[::-1]
    del wordList[int(start):int(end + 1)]                                                #deletes section from original function
    wordList.insert(int(start), revChar)                                          #This puts the reversed segment list into the wordList list
    flatList = [item for sublist in wordList for item in sublist]        #This flattens the list inside the list into one list            
    stringinput = ''.join(flatList) 
    return stringinput

if __name__ == "__main__":
    main()



