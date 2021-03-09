"""Generate Markov text from text files."""

from random import choice


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

    chains = {}

    # your code goes here
    list_of_strings = text_string.split(" ")
    for text in range(len(list_of_strings) - 2):                
        tuple_key = (list_of_strings[text], list_of_strings[text + 1])
        value_list = []
        value_list.append(list_of_strings[text + 2])
        chains[tuple_key] = value_list

    return chains

    #start at index 0 and 1 >> forms a tuple, which is a key in our dictionary
    #the value for this key, is a list: index 2, which is added to this list (iteration 1)
    #index 1 and 2 will form a tuple, that is a key, and its value is a list, which is index 3 (iteration 2)
    

def make_text(chains):
    """Return text from chains."""

    words = []

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
