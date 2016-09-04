"""
Reverse a phrase.

Output:
-------
dog bites man
man bites dog

"""

if __name__ == '__main__':
    input = "dog bites man"
    print input
    word_list = input.split(' ')
    word_list.reverse()
    print ' '.join(word_list)
