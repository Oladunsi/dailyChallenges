def wordcount(board, word):

    for row in range(len(board)):
        currentArray = board[row]
        for col in range(len(currentArray)):
            
            if currentArray[col] != word[0]:
                continue             
            elif currentArray[col] == word[0] and len(word) < len(currentArray[col:]):
                print("checking")
                
                break
        
                #rigthcheck(i,word)

def rightcheck(index, Array, word):
    currentIndex = index + 1
    if currentIndex > len(word):
        currentIndex = 0
        if Array[currentIndex] == word[currentIndex]:
            rigthcheck(currentIndex, Array, word)
    elif Array[currentIndex] == word[currentIndex] and :

        

board = [["s","o","s","o"],
        ["s","o","o","s"],
        ["s","s","s","s"]]

count = 0
word = "sos"
wordcount(board,word)


    #first_letter = Array[index]
    #possible_word_found = Array[index:len]
    #if "".join(possible_word_found) == word
    #index += 1
    
    #if word[index] == Array[index] and lastItem(item,word):

        #return rightcheck(n, board, word)
    #else: 
        #break


#def lastItem(index,word):
    #if index == len(word):
        #return True 
        