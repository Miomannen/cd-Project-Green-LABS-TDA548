import wordfreq
import sys
import os
import urllib.request

def main(textFilePath, stopwordsFilePath, maxCount):
    """
    Run multiple functions to count words from a text file.
    Inputs two paths for text files (".txt", "stopwords.txt"), and a max count.
    """
    # Check if textFilePath is a valid file and ends with .txt
    print(type(textFilePath),textFilePath)
    if textFilePath.lower().startswith(("https:", "http:")):
        try:
            response = urllib.request.urlopen(sys.argv[1])
            print("URL Open")
        except:
            print("ERROR: Arg 1 is not a valid path to a URL.")
            return
        lines = response.read().decode("utf8").splitlines()
        words = wordfreq.tokenize(lines)

    else:
        if not os.path.isfile(textFilePath):
            print("ERROR: Arg 1 is not a valid path to a file.")
            return
        if not textFilePath.lower().endswith(".txt"):
            print("ERROR: Arg 1 is not a valid text file.")
            return
        inp_file = open(textFilePath, encoding="utf-8")
        print("file Open")
        words = wordfreq.tokenize(inp_file)
        inp_file.close()
        
    # Check if stopwordsFilePath is a valid file and ends with stopwords.txt
    if not os.path.isfile(stopwordsFilePath):
        print("ERROR: Arg 2 is not a valid path to a file.")
        return
    if not stopwordsFilePath.lower().endswith("stopwords.txt"):
        print("ERROR: Arg 2 is not a valid stopwords.txt file.")
        return
    
    # Open the stopwords.txt file
    stopwords_File = open(stopwordsFilePath, encoding="utf-8")

    # Tokenize the text file and stopwords file into lists of words
    stopwords = wordfreq.tokenize(stopwords_File)

    # Count the number of words in the text file, excluding words from stopwords.txt
    word_count = wordfreq.countWords(words, stopwords)
    wordfreq.printTopMost(word_count, maxCount)
    
    # Close files
    stopwords_File.close()


if __name__ == "__main__":                  # If this is the main file run
    if len(sys.argv) != 4:                  # If not for arguments are inputted
        print("ERROR: Usage: python wordfreq.py <textfile.txt> <stopwords.txt> <maxCount>")
        sys.exit(1)                         # Exit program

    textFilePath = sys.argv[1]
    stopwordsFilePath = sys.argv[2]
    # Try to convert the third argument to an int
    try:
        maxCount = int(sys.argv[3])
    except ValueError:
        print("ERROR: Argument 3 must be an integer.")
        sys.exit(1)                         # Exit program

    main(textFilePath, stopwordsFilePath, maxCount)