#Define the first function, which counts the number of observed substrings of length 'k'
def count_observed_substrings(sequence, k):
    """
    This function counts the the number of observed substrings of length 'k' in a sequence, given the sequence and the desired length of k.

    Args: 
    sequence: a string of characters, must consist of only A, T, C, and G.
    k: an integer. Integers longer than the length of the sequence will return a value of 0. 
   
    Return:
    An integer, which is the number of observed substrings of the specified length 'k'. 
    """
    
    #Check that sequence is valid, meaning it only contains characters A, C, G, and/or T. Otherwise return error message.
    valid_nucleotides = set(['A', 'C', 'G', 'T'])
    if not set(sequence).issubset(valid_nucleotides):
        return "Only valid nucleotide characters can be counted (A, C, G, T)."
    
     #create an empty set to store substrings of length 'k'
    observed_substrings = set()
    
    #loop over the sequence, counting each substring of length 'k'
    for n in range(len(sequence) - k + 1):
        substring = sequence[n:n+k]
        observed_substrings.add(substring) #add the substring to the set of observed substrings
        
    #return the number of distinct substrings observed 
    return len(observed_substrings) 

#Define the second function, which counts all possible substrings of length 'k'
def count_possible_substrings(sequence, k):
    """
    This function counts the number of substrings of length 'k' that could possibly be observed in a sequence.
    
    Args:
    sequence: a string of characters consisting of only combinations of A, T, C, and G.
    k: an integer. Integers longer than the length of the sequence will return a value of 0.  
    
    Return:
    An integer, which is the number of possible substrings of specified length 'k'.
    """
    
    #Check that sequence is valid, meaning it only contains characters A, C, G, and/or T. Otherwise return error message.
    valid_nucleotides = set(['A', 'C', 'G', 'T'])
    
    if not set(sequence).issubset(valid_nucleotides):
        return "Only valid nucleotide characters can be counted (A, C, G, T)."
    
    #return the number of possible substrings of length k
    return min(len(sequence) - k + 1, 4 ** k) 

#Define the third function, which calculates linguistic complexity of a sequence using functions 1 and 2
def linguistic_complexity(sequence):
    """
    This function calculates the linguistic complexity of a sequence, which is the number of observed
    substrings of all lengths compared to the total number of substrings that are theoretically possible.
    
    Args:
    sequence: a string of characters, must consist of only combinations of A, T, C, and G. 
    
    Return:
    An integer, which is the ratio of the number of observed substrings of all lengths/the total number of possible substrings.
    """
    #Check that sequence is valid, meaning it only contains characters A, C, G, and/or T. Otherwise return error message.
    valid_nucleotides = set(['A', 'C', 'G', 'T'])
    if not set(sequence).issubset(valid_nucleotides):
        return "Only valid nucleotide characters can be counted (A, C, G, T)."
    
     #create a variable to store the total number of observed substrings
    total_observed_substrings = 0 
    #create a variable to store the total number of possible substrings
    total_possible_substrings = 0 
    
    #loop over all possible substring lengths
    for k in range(1, len(sequence) + 1):
        total_observed_substrings += count_observed_substrings(sequence, k) #add the observed substrings
        total_possible_substrings += count_possible_substrings(sequence, k) #add the possible substrings
        
    if total_possible_substrings > 0:
        return total_observed_substrings / total_possible_substrings
    else:
        return 0
        

#read in file from the terminal to test linguistic complexity 
import sys

if len(sys.argv) != 2:
    print("Please add a valid file.")
    sys.exit(1)

sequence_file = sys.argv[1]

with open(sequence_file) as file:
    for line in file:
        sequence = line.strip()
        print(linguistic_complexity(sequence))
