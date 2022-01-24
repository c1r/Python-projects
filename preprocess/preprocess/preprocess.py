# --------------------------------------------
#   Name: Nidal Naseem
#   ID: 1635297
#   CMPUT 274, Fall 2020
#
#   Weekly Exercise #4: Text Preprocessor
# --------------------------------------------

import sys


def demo_command_line():
    '''Read in command line tokens and return the mode of
       processing the words from the user

       Arguments: None

       Return:
           mode : the second element i.e. the mode
           from the list sys.argv
    '''
    error_msg1 = "Too many command line arguments, input as the following:\n"\
                 "python3 preprocess.py <mode>\n"
    assert len(sys.argv) < 3, error_msg1
    error = "Mode not found. Please enter mode of"\
            "one of the following:\n"\
            "“keep-digits”: to not remove numbers in words,"\
            "but perform all other steps\n"\
            "“keep-stops”: to not remove stopwords,"\
            "but perform all other steps\n"\
            "“keep-symbols”: to not remove punctuation or symbols,"\
            "but perform all other steps\n"\
            "Please enter in the following format:\n"\
            "python3 preprocess.py <mode>\n"
    try:
        mode = sys.argv[1]
        assert mode in ("keep-digits", "keep-stopwords", "keep-symbols"), error
    except IndexError:
        mode = ""
    return mode


def lowercase_input():
    '''Read from input and convert all the words to lowercase

       Arguments: None

       Return:
           text : the words converted to lowercase
    '''
    lines = []
    # to take input from user till an empty line is encountered
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = ' '.join(lines)
    text = text.lower()
    return text


def rm_punc_symbols(text):
    '''Removes all punctutation marks and symbols from the words passed

       Arguments:
           text : the string to remove all the punctuation and
                  symbols from.

       Return:
           corrected_text: string with no punctuatuion and symbols
    '''
    newtext = []
    '''Going through each character in string to
       check if it is alphanumeric or space and
       appending alphanumeric character to a new list'''
    for i in range(len(text)):
        if text[i].isalnum() or text[i] == " ":
            newtext.append(text[i])
    corrected_text = "".join(newtext)
    return corrected_text


def rm_digits(text):
    '''Removes all digits from a word but not if the word/token is a number

       Arguments:
           text: the string with words containing digits as suffix/prefix

       Return:
           corrected_text: the string with words that doesn't contain digits
    '''
    text = list(text.split())
    correct_text = []
    ''' Checking if element in list is number or word,
        then proceeding to remove digits from the words and
        keeping seperate numbers as it is'''
    for char in text:
        if not char.isdigit():
            letters = list(char)
            # Appending all non digits to a new list
            for i in letters:
                if not i.isdigit():
                    correct_text.append(i)
            correct_text.append(" ")
        else:
            correct_text.append(char + " ")
    corrected_text = "".join(correct_text)
    return corrected_text


def rm_stopwords(text):
    '''Removes all stopwords (given list of words) from a string

       Arguments:
           text: the string which contains stopwords

       Return:
           corrected_text: the string that does not contain any of the
                           stopwords
    '''
    text = list(text.split())
    correct_text = []
    txt_without_stop = []
    stopwords = [
        "i", "me", "my", "myself", "we", "our", "ours", "ourselves",
        "you", "your", "yours", "yourself", "yourselves",
        "he", "him", "his", "himself", "she", "her",
        "hers", "herself", "it", "its", "itself", "they",
        "them", "their", "theirs", "themselves", "what",
        "which", "who", "whom", "this", "that", "these",
        "those", "am", "is", "are", "was", "were", "be", "been",
        "being", "have", "has", "had", "having", "do", "does",
        "did", "doing", "a", "an", "the", "and", "but", "if",
        "or", "because", "as", "until", "while", "of", "at",
        "by", "for", "with", "about", "against", "between",
        "into", "through", "during", "before", "after", "above",
        "below", "to", "from", "up", "down", "in", "out", "on",
        "off", "over", "under", "again", "further", "then", "once",
        "here", "there", "when", "where", "why", "how", "all",
        "any", "both", "each", "few", "more", "most", "other",
        "some", "such", "no", "nor", "not", "only", "own", "same",
        "so", "than", "too", "very", "s", "t", "can", "will",
        "just", "don", "should", "now"
        ]
    ''' Removing stopwords by appending non-stopwords
        to a new list'''
    for char in text:
        if char not in stopwords:
            txt_without_stop.append(char)
    corrected_text = " ".join(txt_without_stop)
    return corrected_text


if __name__ == "__main__":
    mode = demo_command_line()
    words = lowercase_input()
    if mode == "keep-digits":
        processed_words = rm_stopwords(rm_punc_symbols(words))
    elif mode == "keep-stops":
        processed_words = rm_digits(rm_punc_symbols(words))
    elif mode == "keep-symbols":
        processed_words = rm_stopwords(rm_digits(words))
    else:
        processed_words = rm_stopwords(rm_digits((rm_punc_symbols(words))))
    print(processed_words)
