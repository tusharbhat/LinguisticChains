### LinguisticChains

### Solution for Coding challenge

### Concept

Concept: Create a set of dictionaries where the words are in different dictionaries by length. 
Considering each word, in descending order of lengths, find a word as its 'child' where the child is the next word in a possible chain.
Process the chain recursively if the child has possible children of its own.
Store the length of the largest possible chain for a word and its best child.
Processing is halted when the maximum length of remaining words is smaller than the length of the largest chain found so far.
Result of processing a word while checking a chain is stored for each word.
Processing a chain halts either when a word that has been processed already is found or the current chain can no longer be extended.

### Runtime Complexity Analysis

Each word in the dictionary will be processed at most once giving the solution an O(k) runtime where k is the number of words in the dictionary.
As processing is halted when the size of words is too small for finding viable solutions, in practice, runtime is greatly reduced.
However, O(k * length of k) lookups are performed, where for each word, all its possible 'children' words are looked to see whether or not they exist.

### Space Complexity Analysis

N dictionaries are used, where N is the length of the largest word. The input was split by size to make it easier to perform checks which lead to better runtime.
Dictionaries are expected to be of O(1) space complexity but the actual size of dictionaries vary with number of elements input in practice.
Thus, space complexity can be treated as O(N) or O(k) where k is the number of words in a dictionary.

### How To:

`python ling_chains.py <input file location>` will run the program.

### Time taken:
Started at: 6:09 pm 11/22/15
Working version of code at: 7:49 pm
Challenge complete with comments and readme at : 8:29 pm