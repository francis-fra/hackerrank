def merge_the_tools(string, k):
    num_lines = int(len(string) / k)
    for idx in range(num_lines):
        word = string[idx*k:(idx+1)*k]
        word = dedup(word)
        print(word)

def dedup(string):
    result = ""
    d = {}
    for s in string:
        if s not in d.keys():
            result += s
            d[s] = 1
    return result


if __name__ == '__main__':
    s = 'AABCAAADA'
    k = 3
    merge_the_tools(s, k)