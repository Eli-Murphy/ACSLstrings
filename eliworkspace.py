def main():
    start=3
    total=3
    numberChars=2
    direction="R"
    word= "COMPUTER"
    #mc(start,total,numberChars,direction, word)
    rev(start,total,word)
    
    
def mc(start,total,numberChars,direction, word):
    wordlist = list(word)
    start = start - 1
    print(wordlist)
    
def rev(start, total,word):
    start = start -2
    end = start+total
    wordlist = list(word)
    i = slice(end,start,-1)
    print(wordlist[i])
    del wordlist[start+1:end+1]
    print(wordlist)
    endlist = []
    endlist[start:end] = 
    
    
if __name__ == '__main__':
    main()
