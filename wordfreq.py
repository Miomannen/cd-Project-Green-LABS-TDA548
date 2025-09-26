import os
import sys

def tokenize(textFile):
    """
    Convert a list of lines into a list of words.
    Split words and special characters into separate words.
    """
    
    words = []
    # Loop through each line of text and each character in the line.
    for line in textFile:
        current_word = ''
        for char in line:
            if char.isalnum():              # If char is an alphanumeric
                # If char is a digit, current word is not empty, and the previous char
                # was not a digit, add the current word to words and start building a new number.
                if char.isdigit() and current_word and not current_word[-1].isdigit():
                    words.append(current_word)
                    current_word = ''
                # If char is a letter, current word is not empty, and the previous char
                # was not a letter, add the current word to words and start building a new word.
                elif char.isalpha() and current_word and not current_word[-1].isalpha():
                    words.append(current_word)
                    current_word = ''
                # Add the current char to start building a word or number
                current_word += char.lower()

            else:                           # If char is a special character (e.g., "!,&?") or a space
                if current_word:            # If current word is not empty, add it to words
                    words.append(current_word)
                    current_word = ''
                if not char.isspace():      # If char is not a space, add char directly to words
                    words.append(char)
        if current_word:                    # If word not empty, add the last word or number to words
            words.append(current_word)
    return words


def countWords(words, stopWords):
    """
    Count the number of times each word appears in a list of words,
    excluding words from another list.
    Return a dictionary with key: word, value: count.
    """
    dict = {}
    for word in words:
        if word in stopWords: continue      # If word in stopWords, skip this element.
        
        if word in dict: dict[word] += 1    # If word exists in dict, increment it's count
        else: dict[word] = 1                # If word doesn't exist, add it with count 1
    
    return dict


def printTopMost(freq_dict, numberof):
    """
    Print a dictionary's key and value pairs with basic formatting.
    Inputs a frequency dictionary and the number of words to print out.
    Key1 ______________________ Value1
    Key2 ______________________ Value2
    """
    # Sort the input dictionary based on the value for each key, in descending order.
    sorted_rev = dict(sorted(freq_dict.items(), key=lambda item: item[1],reverse=True))
    
    # Enumerate gives current index and the current key.
    for index, key in enumerate(sorted_rev):
        if index+1 > numberof:
            break
        print(key.ljust(20, ' '),str(sorted_rev[key]).rjust(4, ' '))
