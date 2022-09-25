import re
numlines = int(input().rstrip())

m01 = lambda x: bool(re.match(r"^[4|5|6]\d{15}$", x))
m02 = lambda x: bool(re.match(r"^[4|5|6]\d{3}-\d{4}-\d{4}-\d{4}$", x))
pattern = r'(\d)\1{3}'
m03 = lambda x: bool(re.search(pattern, x.replace('-', '')))

for idx in range(numlines):
    card_number = input().rstrip()
    if (m01(card_number) or (m02(card_number))) and not (m03(card_number)):
        print('Valid')
    else:
        print('Invalid')

