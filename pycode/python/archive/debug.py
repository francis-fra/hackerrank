



# DEBUG # matrix = ['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!']
# # "".join([wrd[0] for wrd in matrix])
# # join strings 
# # "".join([wrd[0] for wrd in matrix])
# # "".join([wrd[0] for wrd in matrix])
# m = 3
# s = "".join([ "".join([wrd[idx] for wrd in matrix]) for idx in range(m)])

# find things between /w
s = 'This$#is% Matrix#  %!'
# regex_code = r"[a-zA-Z0-9]([^a-zA-Z0-9]+\s?)[a-zA-Z0-9]"
regex_code = r"([a-zA-Z0-9])([^a-zA-Z0-9]+\s?)([a-zA-Z0-9])"
regex_replace = r"\1 \3"
re.sub(regex_code, regex_replace, s)



matches = re.findall(regex_code, s)
matches
re.search(regex_code, s).group()
re.sub(regex_code, '*', s)




regex_code = r"([a-zA-Z0-9])([^a-zA-Z0-9]+\s?)([a-zA-Z0-9])"
re.findall(regex_code, s)

# regex_ref = r"[a-zA-Z0-9]\1[a-zA-Z0-9]"
s.replace(matches[0], ' ')
s
re.sub(regex_code, ' ', s)


# for pattern in matches:
    # s = s.replace(pattern, ' ')

# re.match(regex_code, s)
# s