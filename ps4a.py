# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # Creating a base case... Take that there is just one letter
    if len(sequence) == 1:
        list_perms = []
        list_perms.append(sequence)
        return list_perms
    # Creating second case... if there are two letters, flip
    elif len(sequence) == 2:
        list_perms = []
        for i in range(2):
            list_perms.append(sequence[1]+sequence[0])
            list_perms.append(sequence[0]+sequence[1])
        return list_perms
    # Final case... remove first letter, then reinput to function
    else:
        extra=sequence[0]
        sequence_new = sequence[1:]
        list_perms=[]
        for old_perm in get_permutations(sequence_new):
            for i in range(len(old_perm)+1):
                new_perm = old_perm[:i] + extra + old_perm[i:]
                list_perms.append(new_perm)
        list_perms = list(dict.fromkeys(list_perms).keys())
        return list_perms

print(get_permutations('str'))

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

