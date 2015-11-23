# Linguistic Chains Main Code
# Author: Tushar Bhat

import sys


# Recursive function to process a word and return its attributes.
def process_word(word, i):

    best_child = None
    best_child_len = 0

    if not input_set[i][word]['processed']:
        for j in range(len(word)):
            new_word = word[:j] + word[j + 1:]
            if (i - 1) in input_set and new_word in input_set[i - 1]:
                temp_res = process_word(new_word, i - 1)
                if temp_res['chain'] > best_child_len:
                    best_child_len = temp_res['chain']
                    best_child = new_word

        input_set[i][word]['processed'] = True
        input_set[i][word]['child'] = best_child
        input_set[i][word]['chain'] = best_child_len + 1

    return input_set[i][word]

# Main script starts here, calls process_word() as required.

# Accepting dictionary file name as an argument.
input_file = sys.argv[1]

# Initializing local dictionary with dictionary file input.
input_set = dict()

with open(input_file, 'r') as inFile:
    for read_line in inFile:
        line = read_line.strip()
        temp_len = len(line)
        if temp_len not in input_set:
            input_set[temp_len] = dict()
        input_set[temp_len][line] = dict()
        input_set[temp_len][line]['processed'] = False
        input_set[temp_len][line]['child'] = None
        input_set[temp_len][line]['chain'] = 1

# Beginning loop to find longest chains.
max_chain_len = 0
chain_lists = list()

i = max(input_set.iterkeys())

while i >= max_chain_len and i > 0:
    # while i > 0:
    if i in input_set and i - 1 in input_set:
        for word in input_set[i]:
            temp_res = process_word(word, i)
            if temp_res['chain'] > max_chain_len:
                max_chain_len = temp_res['chain']
                chain_lists = list()
                chain_lists.append(word)
            elif temp_res['chain'] == max_chain_len:
                chain_lists.append(word)
    i -= 1

if len(chain_lists) == 0:
    print "Empty Input"
else:
    for word in chain_lists:
        sentence = word
        this_word = word
        while input_set[len(this_word)][this_word]['child'] is not None:
            sentence += ' => '
            this_word = input_set[len(this_word)][this_word]['child']
            sentence += this_word
        print sentence
