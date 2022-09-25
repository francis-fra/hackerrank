def transformSentence(sentence):
    # initialize
    arr = [x for x in sentence]
    is_prev_space = True
    y = ''
    for idx, x in enumerate(arr):
        if not is_prev_space:
            if ord(y.lower()) < ord(x.lower()):
                arr[idx] = x.upper()
            elif ord(y.lower()) > ord(x.lower()):
                arr[idx] = x.lower()
            else:
                arr[idx] = x
        # update state
        if x != ' ':
            is_prev_space = False
        else:
            is_prev_space = True 
        y = x
    return "".join(arr)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()
    result = transformSentence(sentence)
    print(result)

    # fptr.write(result + '\n')
    # fptr.close()