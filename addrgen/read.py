# File that initializes and returns a list of searchable values (defined per-line)
# as an array of strings.input_strs[]

def readInputString():
    input_strs = []
    with open('addrgen\search.txt', 'r') as f:
        for line in f.readlines():
            input_strs.append(line.rstrip())
        return input_strs
