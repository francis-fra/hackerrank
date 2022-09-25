def minion_game(string):
    word_len = len(string)
    # stuart
    result = [ word_len - idx for idx, s in enumerate(string) if not is_vowel(s)]
    print (result)

def is_vowel(s):
    return s in "AEIOU"
    
if __name__ == '__main__':
    # s = input()
    s = "BANANA"
    minion_game(s)