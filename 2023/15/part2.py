def ascii_score(string):
    val = 0
    for s in string:
        val += ord(s)
        val *= 17
        val = val % 256

    return val

fname = "input.txt"
#fname = "test.txt"
infile = open(fname, "r")
sequence = infile.read().strip()
sequence = sequence.split(",")

boxes = [None] * 256
focals = [None] * 256

for string in sequence:
    # break by - or =

    if "-" in string:
        string = string.split("-")
        operation = '-'
    if "=" in string:
        string = string.split("=")
        operation = '='
    
    label = string[0]
    focal_length = string[-1]
    val = ascii_score(label)

    print(label, operation, focal_length, val)


    if operation == '=':
        if not boxes[val]:
            boxes[val] = [label]
            focals[val] = [focal_length]
        else:
            if label in boxes[val]:
                i = boxes[val].index(label)
                focals[val][i] = focal_length
            
            else:
                boxes[val].append(label)
                focals[val].append(focal_length)

    if operation == '-':
        if not boxes[val]:
            continue
        if label in boxes[val]:
            i = boxes[val].index(label)
            #boxes[val].remove(boxes[val][i])
            #focals[val].remove(focals[val][i])
            del boxes[val][i]
            del focals[val][i]

total_power = 0
for i in range(len(boxes)):
    if boxes[i]:
        for j in range(len(boxes[i])):
            boxpow = (i + 1)
            slotpow = (j + 1)
            focuspow = int(focals[i][j])
            focus_power = boxpow * slotpow * focuspow
            print(focus_power)
            total_power += focus_power

print(total_power)
