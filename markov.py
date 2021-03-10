"""Generate Markov text from text files."""

from random import choice
import random

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    
    # your code goes here
    f = open (file_path)
    
    'Contents of your file as one long string'
    return f.read()


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    """ Pseudocode
    start at index 0 and 1 >> forms a tuple, which is a key in our dictionary
    the value for this key, is a list: index 2, which is added to this list (iteration 1)
    index 1 and 2 will form a tuple, that is a key, and its value is a list, which is index 3 (iteration 2)
    """

    chains = {}

    # .replace('\n', ' ,')
    # .strip('\r\n')
    # your code goes here
    list_of_strings = text_string.split(" ")        #splits input text by spaces and sets it equal to list_of_strings
    for text in range(len(list_of_strings) - 2):    #iterates through the range of the length of lists_of strings           
        tuple_key = (list_of_strings[text], list_of_strings[text + 1])  #creates a tuple that contains 2 elements, this is our key in the chains dictionary
        value_list = []                                                 #creates an empty list
        value_list.append(list_of_strings[text + 2])                    #appends one item to value_list
        chains[tuple_key] = value_list                                  #sets tuple_key as a key in the chains dictionary, and sets value_list as tuple_key's value in the chains dictionary

    return chains                                    #returns the entire dictionary

    

def make_text(chains):
    """Return text from chains.
    To make a chain of fake text, start with/create a link.
    A link is a key, tuple_key, and a random word from the list that follows it (its value), value_list
    Put this link inside a container/list
    Join the list into a string at the end (halfway done)

    repeat this process to continue adding more:
    make a new key from the SECOND word 
    """

    words = []
    # .choice()

    chains_keys = chains.keys()
    random_key = random.choice(list(chains_keys))
    words.append(random_key)
    
    # while i in chains_keys:
        

    # your code goes here
    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
