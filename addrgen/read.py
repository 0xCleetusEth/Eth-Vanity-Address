def readInputString():
    input_strs = []
    with open('addrgen\search.txt', 'r') as f:
        for line in f.readlines():
            input_strs.append(line.rstrip())
        return input_strs
