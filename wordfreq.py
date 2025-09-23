import os
import sys

def tokenize(textFile):
    """Convert a list of lines into a list of words.
    Split the words and special characters into separate words."""
    
    words = []
    for line in textFile:
        current_word = ''
        for char in line:
            #print(char)
            if char.isalnum():
                if char.isdigit() and current_word and not current_word[-1].isdigit():
                    words.append(current_word)
                    current_word = ''
                elif char.isalpha() and current_word and not current_word[-1].isalpha():
                    words.append(current_word)
                    current_word = ''
                current_word += char.lower()

            else:
                if current_word:
                    #print(current_word)
                    words.append(current_word)
                    current_word = ''
                if not char.isspace():
                    words.append(char)
        if current_word:
            words.append(current_word)
    return words


def countWords(words, stopWords):
    dict = {}
    for word in words:
        if word in stopWords: continue

        if word in dict: dict[word] += 1
        else: dict[word] = 1
    
    return dict

def printTopMost(freq_dict, numberof):
    sorted_rev = dict(sorted(freq_dict.items(), key=lambda item: item[1],reverse=True))
    #print(sorted_rev)
    for key, element in enumerate(sorted_rev):
        if key+1 > numberof:
            break
        print(element.ljust(20, ' '),str(sorted_rev[element]).rjust(4, ' '))

def main(textFilePath, stopwordsFilePath, maxCount):
    # Check if textFilePath is a valid file and ends with .txt
    if not os.path.isfile(textFilePath):
        print("ERROR: Arg 1 is not a valid path to a file.")
        return
    if not textFilePath.lower().endswith(".txt"):
        print("ERROR: Arg 1 is not a valid text file.")
        return

    # Check if stopwordsFilePath is a valid file and ends with .txt
    if not os.path.isfile(stopwordsFilePath):
        print("ERROR: Arg 2 is not a valid path to a file.")
        return
    if not stopwordsFilePath.lower().endswith("stopwords.txt"):
        print("ERROR: Arg 2 is not a valid stopwords.txt file.")
        return
    
    inp_file = open(textFilePath, encoding="utf-8")
    stopwords_File = open(stopwordsFilePath, encoding="utf-8")
    print("file Open")

    words = tokenize(inp_file)
    stopwords = tokenize(stopwords_File)
    word_count = countWords(words, stopwords)
    printTopMost(word_count, maxCount)
    
    inp_file.close()
    stopwords_File.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("ERROR: Usage: python wordfreq.py <textfile.txt> <stopwords.txt> <maxCount>")
        sys.exit(1)

    textFilePath = sys.argv[1]
    stopwordsFilePath = sys.argv[2]
    try:
        maxCount = int(sys.argv[3])
    except ValueError:
        print("ERROR: Argument 3 must be an integer.")
        sys.exit(1)

    main(textFilePath, stopwordsFilePath, maxCount)