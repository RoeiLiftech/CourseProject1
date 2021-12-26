from collections import Counter


def most_commond_to_char():
    with open("message.txt") as txt:
        chars = txt.read()
    #print(chars)

    keys = list(chars)
    #print(keys)

    for val in chars:
        if val.isalpha():
            continue
        else:
            keys.remove(val)
    #print(keys)

    for i in range(len(keys)):

        keys[i] = keys[i].lower()

    #print(keys)
    counter = dict(Counter(keys))
    myList = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    #print(myList)

    #print(myList[:4])
    highest = dict(myList[:4])
    #print(highest)
    most_comm_char = ['e', 't', 'o', 'r']
    #print(highest.items())
    for i in most_comm_char:
        i = 0
        for key, value in highest.items():
            highest[key] = most_comm_char[i]
            i += 1
    #print(highest)
    rev = {val: key for key, val in highest.items()}
    #print(rev)
    result = highest | rev
    #print(result)
    return result

print(most_commond_to_char())
