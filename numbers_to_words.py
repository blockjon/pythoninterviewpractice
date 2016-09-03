"""
Convert integers into english language phrases.

Output:
-------
-3 = negative three
-2 = negative two
-1 = negative one
0 = zero
1 = one
2 = two
3 = three
4 = four
5 = five
6 = six
7 = seven
8 = eight
9 = nine
10 = ten
11 = eleven
12 = twelve
13 = thirteen
14 = fourteen
15 = fifteen
16 = sixteen
17 = seventeen
18 = eighteen
19 = nineteen
20 = twenty
21 = twenty one
22 = twenty two
23 = twenty three
24 = twenty four
25 = twenty five
26 = twenty six
27 = twenty seven
28 = twenty eight
29 = twenty nine
30 = thirty
31 = thirty one
32 = thirty two
33 = thirty three
34 = thirty four
35 = thirty five
36 = thirty six
37 = thirty seven
38 = thirty eight
39 = thirty nine
40 = fourty
41 = fourty one
42 = fourty two
43 = fourty three
44 = fourty four
45 = fourty five
46 = fourty six
47 = fourty seven
48 = fourty eight
49 = fourty nine
50 = fifty
51 = fifty one
52 = fifty two
53 = fifty three
54 = fifty four
55 = fifty five
56 = fifty six
57 = fifty seven
58 = fifty eight
59 = fifty nine
60 = sixty
61 = sixty one
62 = sixty two
63 = sixty three
64 = sixty four
65 = sixty five
66 = sixty six
67 = sixty seven
68 = sixty eight
69 = sixty nine
70 = seventy
71 = seventy one
72 = seventy two
73 = seventy three
74 = seventy four
75 = seventy five
76 = seventy six
77 = seventy seven
78 = seventy eight
79 = seventy nine
80 = eighty
81 = eighty one
82 = eighty two
83 = eighty three
84 = eighty four
85 = eighty five
86 = eighty six
87 = eighty seven
88 = eighty eight
89 = eighty nine
90 = ninety
91 = ninety one
92 = ninety two
93 = ninety three
94 = ninety four
95 = ninety five
96 = ninety six
97 = ninety seven
98 = ninety eight
99 = ninety nine
100 = one hundred
101 = one hundred and one
102 = one hundred and two
103 = one hundred and three
104 = one hundred and four
105 = one hundred and five
106 = one hundred and six
107 = one hundred and seven
108 = one hundred and eight
109 = one hundred and nine
110 = one hundred and ten
111 = one hundred and eleven
112 = one hundred and twelve
113 = one hundred and thirteen
114 = one hundred and fourteen
115 = one hundred and fifteen
116 = one hundred and sixteen
117 = one hundred and seventeen
118 = one hundred and eighteen
119 = one hundred and nineteen
120 = one hundred and twenty
121 = one hundred and twenty one
122 = one hundred and twenty two
123 = one hundred and twenty three
124 = one hundred and twenty four
"""

import math

GROUP_NAMES = [None, 'thousand', 'million', 'billion']
TENS_NAMES = [None, None, 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
ONE_TO_NINETEEN_MAP = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}


def digit_to_word(digit):
    return ONE_TO_NINETEEN_MAP.get(digit, '')


def get_tens_result(number):
    """ Gets the full english name for numbers between zero and 99. """

    # Ensure we are dealing with numbers below 100
    number %= 100
    if number == 0:
        return None
    if number > 19:
        result = TENS_NAMES[int(math.floor(number / 10))]
        single_digit_name = digit_to_word(number % 10)
        if single_digit_name:
            result = result + " " + single_digit_name
        return result
    else:
        return digit_to_word(number)


def add_to_answer(three_digit_sequence, solution, group_index):
    """ Prepend the current answer with more language. """
    if three_digit_sequence / 100 >= 1:
        hundreds_digit = int(math.floor(three_digit_sequence/100))
        result = digit_to_word(hundreds_digit) + " hundred"
        sub_100_result = get_tens_result(three_digit_sequence)
        if sub_100_result:
            result = "{} and {}".format(result, sub_100_result)
    elif three_digit_sequence > 19:
        result = get_tens_result(three_digit_sequence)
    else:
        result = digit_to_word(three_digit_sequence)
    if group_index > 0:
        if len(GROUP_NAMES)-1 > group_index:
            raise Exception("Unsupported number - number out of range")
        group_name = GROUP_NAMES[group_index]
        result = result + " " + group_name + " "
    return result + solution


def say_number(input):
    """ Convert an integer into an english language phrase. """
    is_positive = input > -1
    # Normalize.
    input = abs(input)
    if input == 0:
        solution = 'zero'
    else:
        solution = ''
        loop_counter = 0
        while input > 0:
            three_digit_group = int(input % 1000)
            input = math.floor(input / 1000)
            solution = add_to_answer(three_digit_group, solution, loop_counter)
            loop_counter += 1
        if not is_positive:
            solution = "negative " + solution
    return solution


if __name__ == '__main__':
    for i in range(-3, 125):
        print "{} = {}".format(i, say_number(i))
