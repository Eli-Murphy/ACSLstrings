def main():
    start=3
    total=3
    numberChars=2
    direction="R"
    word= "COMPUTER"
    #mc(start,total,numberChars,direction, word)
    rev(start,total,word)
    
    
def mc(start,total,numberChars,direction, word):
    wordList = list(word)
    start = start - 1
    print(wordList)
    
def rev(start, total,word):
    start = start -2                                                                 #I have no idea why this works it just does
    end = start+total                                                             #This calculates the end point by adding the total amount of chars effected
    wordList = list(word)                                                         #Converts desired word to list
    i = slice(end,start,-1)                                                         #Creates index var that splits wordList into desired section and reverses the section
    revChar = wordList[i]                                                         #Assigns split to variable
    del wordList[start+1:end+1]                                                #deletes section from original function
    wordList.insert(start+1, revChar)                                          #This puts the reversed segment list into the wordList list
    flatList = [item for sublist in wordList for item in sublist]        #This flattens the list inside the list into one list            
    output = ''.join(flatList)                                                          #This converts the list into a string
    print("Output: " + output)
    return output
    
    
    
if __name__ == '__main__':
    main()
