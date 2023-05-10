from sequence_analysis import count_observed_substrings
from sequence_analysis import count_possible_substrings
from sequence_analysis import linguistic_complexity

#Test the first function
def test_count_observed_substrings():
    assert count_observed_substrings ("ATTTGGATT", 1) == 3
    assert count_observed_substrings ("ATTTGGATT", 2) == 5
    assert count_observed_substrings ("ILOVEDATA", 3) == "Only valid nucleotide characters can be counted (A, C, G, T)." 
    assert count_observed_substrings ("ATTTGGATT", 18) == 0

#Test the second function
def test_count_possible_substrings():
    assert count_possible_substrings ("1282398W37", 1) == "Only valid nucleotide characters can be counted (A, C, G, T)."
    assert count_possible_substrings ("ATTTGGATT", 2) == 8
    assert count_possible_substrings ("ATTTGGATT", 3) == 7
    assert count_possible_substrings ("ATTTGGATT", 4) == 6

#Test the third function
def test_linguistic_complexity():
                                      
    assert linguistic_complexity("ATTTGGATT") == 0.875
    assert linguistic_complexity("SARAHISTHECOOLEST") == "Only valid nucleotide characters can be counted (A, C, G, T)."
