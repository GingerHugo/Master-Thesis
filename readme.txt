Based on the Chinese discourse connectives listed by Cheng and Tian (1989), Cheng (2006), and Lu (2007), we apply our semi-supervised learning algorithm to estimate the probability distributions of discourse relations of the connectives with 302,293 unlabeled sentences.

The lexicon is a comma-separeted value (CSV) file encoded in UTF-8.

Each row presents either a pair-wise connective that its first word appears in arg1 and its second word appears in arg2, or a single word connective that appears in arg1 or in arg2 mutually exclusive.

Seven columns are separated by commas in each row. The data in each columns is described as follows. 

The first column is the word appearing in arg1.
The second column is the word appearing in arg2.
The third column is number of sentences of this connective in the 302,293 sentences.
The fourth column is probability of this connective to be occur in the Temporal relation.
The fifth column is probability of this connective to be occur in the Contingency relation.
The sixth column is probability of this connective to be occur in the Comparison relation.
The seventh column is probability of this connective to be occur in the Expansion relation.
