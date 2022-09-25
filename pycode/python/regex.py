regex_integer_in_range = r"[1-9]\d{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=(\d).\1)"

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) and \
    len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


P = "110000"
P = "542361"
bool(re.match(regex_integer_in_range, P))
re.findall(regex_alternating_repetitive_digit_pair, P)