S = input().rstrip()
k = input().rstrip()

plen = len(k)
Slen = len(S)
isFound = False
for idx in range(Slen-plen+1):
    if S[idx:idx+plen] == k:
        print("({}, {})".format(idx, idx+plen-1))
        isFound = True

if isFound == False:
    print("(-1, -1)")

