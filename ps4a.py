# Problem Set 4A
# Name: Nicholas Pan
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
# See below for 3 test cases

    test_input1 = 'nic'
    print('Input: ', test_input1)
    print('Expected Output:', ['nic', 'inc', 'icn', 'cin', 'cni', 'nci'])
    print('Actual Output:', get_permutations(test_input1))

    test_input2 = 'ang'
    print('Input: ', test_input2)
    print('Expected Output:', ['ang', 'nag', 'nga', 'gna', 'gan', 'agn'])
    print('Actual Output:', get_permutations(test_input2))

    test_input3 = 'abc'
    print('Input:', test_input3)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(test_input3))


