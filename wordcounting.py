import io
import sys
import importlib.util
import wordfreq
import os



def tokenize(lines):
    words = []
    for line in lines:
        currentword = ""
        lastchar = ""

        for char in line:
            if(char.isalpha()):
                # a = true, 1 = false, " " = false

                if(lastchar.isdigit()):
                    words.append(currentword)
                    currentword = ""
                    currentword += char.lower()

                else:
                      currentword += char.lower()

            elif(char.isdigit()):

                if(lastchar.isdigit()):
                    currentword += char

                else:
                    if (currentword):
                        words.append(currentword)
                        currentword = ""

                    currentword += char

                
            
            else:
                if(currentword):
                    # kollar om ord existerar, aka not tom -> tryck in ord i words (från curr.)
                    words.append(currentword)
                    currentword = ""
                
                if not char.isspace():
                    # filtrerar bort space från specialtecken, ickespace. 
                    # Vi vill inte printa space, men vi vill printa spec.teck. (de är samma kategori)
                    words.append(char)
            
            lastchar = char.lower()

        if(currentword):
            words.append(currentword)

    return words
    
def countWords(words, stopWords):
    dict = {}
    
    for word in words:
        if(word in stopWords):
            continue #skippar det nuvarande elementet i for-loopen. Dvs, hittar den ett stopWord så ignorerar den det
        
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    return dict

def printTopMost(frequencies,n):

    sorted_items = sorted(frequencies.items(), key=lambda item: item[1],reverse=True)

    for k,v in sorted_items[:n]:
        print(f'{k.ljust(15)}  {v}')

def main(textFilePath, stopwordsFilePath, maxCount):
    if not os.path.isfile(textFilePath): #os.path kollar om inputen (textfilePath) är giltig
        print("Err: Arg 1 is not valid path to file")
        return
    if not textFilePath.lower().endswith(".txt"):
        print("Err: Arg 1 is not a textfile (.txt)")
        return
    
    if not os.path.isfile(stopwordsFilePath): #os.path kollar om inputen (textfilePath) är giltig
        print("Err: Arg 2 is not valid path to file")
        return
    if not stopwordsFilePath.lower().endswith("stopwords.txt"):
        print("Err: Arg 2 is not a valid stopwords.txt file")
        return
    
    inp_file = open(textFilePath, encoding='utf-8')
    stopwords_File = open(stopwordsFilePath, encoding='utf-8')
    print("file Open")

    words = tokenize(inp_file)
    stopwords = tokenize(stopwords_File)
    word_count = countWords(words,stopwords)
    printTopMost(word_count, maxCount)

    inp_file.close()
    stopwords_File.close()
    

if __name__ == "__main__": # __name__ = wordcounting.py, vi gör den main om den körs ensam
    if len(sys.argv) != 4:
        print("Err1")
        sys.exit(1)

    textFilePath = sys.argv[1]
    stopwordsFilePath = sys.argv[2]
    try:
        maxCount = int(sys.argv[3])
    except ValueError:
        print("Err2")
        sys.exit(1)

    main(textFilePath, stopwordsFilePath, maxCount)

    # lines = ["Hej, jag the heter Mio!? Jag fy11de 19 igår!", "Vi gllar pistageglass!8"]
    # a = ""
    # txt = (tokenize(lines))
    # dictionary = countWords(txt, a)

    # printTopMost(dictionary,100000000)

    


