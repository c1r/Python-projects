# --------------------------------------------
#   Name: Nidal Naseem
#   ID: 1635297
#   CMPUT 274, Fall 2020
#
#   Weekly Exercise 3: Word Frequency
# --------------------------------------------

import sys
from collections import OrderedDict


def demo_command_line():
    '''Read in command line tokens and return the filename
       to read data from and handling incorrect number of
       command line inputs

       Arguments: None

       Return:
           filename : the second element i.e. the filename
           from the list sys.argv
    '''
    error_msg = "Too few command line arguments, input as the following:\n"
    error_msg1 = "Too many command line arguments, input as the following:\n"
    error_msg_demo = "python3 freq.py <filename to read from>"
    assert len(sys.argv) > 1, error_msg + error_msg_demo
    assert len(sys.argv) < 3, error_msg1 + error_msg_demo
    filename = sys.argv[1]
    return(filename)


def read_split_data(filename):
    '''Read data from file to append each word from it to a list
       and return the list

       Arguments:
           filename: the filename to read the data from

       Return:
           new_line: the list containing all space seperated
           words from the file
    '''
    with open(filename, 'r') as f:
        new_line = []
        ''' Splitting and adding each word of a sentence to a list
            to reduce memory usage '''
        for line in f:
            new_line = new_line + line.split()
    return new_line


def sort_count_freq_words(new_line):
    ''' Adding elements of a list to a dictionary and sorting, counting
        and calculating the frequency of every word

        Arguments:
            new_line: a list containing words to be sorted and counted
            and for whose element frequency is to be calculated

        Return:
            sorted_words: the lexicographically sorted dictionary "words"
            frequency: the frequency of each word
    '''
    words = {}
    ''' Adding the elements of new_line to a dictionary "words"
        and using it to count the number of occurence of each word'''
    for char in new_line:
        if char not in words:
            words[char] = 1
        else:
            words[char] += 1
    sort_words = OrderedDict(sorted(words.items()))
    cnt = list(sort_words.values())
    ''' Multiplying each value of number of words by the count
        divided by total number of words to get frequency'''
    frequency = [round(x / len(new_line), 3) for x in cnt]
    return sort_words, frequency


def write_freq_table(filename, sort_words, frequency):
    '''Open a file "filename.out" to write a table consisting of words
       and their respective count, frequency from the dictionary and
       list of frequency passed

       Arguments:
           filename: name of file to be used to write the data into
           sort_words: the dictionary used to extract the words
                       and their count
           frequency: list frequency of each word
    '''
    with open(filename + ".out", "w") as f:
        val = list(sort_words.values())
        key = list(sort_words.keys())
        ''' Printing a line with word,with its count and frequency
            for every new word'''
        for i in range(len(sort_words)):
            table = "{} {} {}\n".format(key[i], val[i], frequency[i])
            f.write(table)


if __name__ == "__main__":
    filename = demo_command_line()
    new_line = read_split_data(filename)
    sort_words, frequency = sort_count_freq_words(new_line)
    write_freq_table(filename, sort_words, frequency)
