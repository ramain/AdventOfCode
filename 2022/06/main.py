def unique(s):
    return len(set(s)) == len(s)

def find_unique_string(text, L=4):
    for i in range(len(text)):
        s = text[i:i+L]
        if unique(s):
            print(s)
            print(i+L)
            break

input = open('input', 'r')
text = input.read()
#text = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

find_unique_string(text, 4)
find_unique_string(text, 14)