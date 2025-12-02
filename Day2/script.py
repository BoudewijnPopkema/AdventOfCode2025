file = open("input")
filecontent = file.read()
idranges = [(range.split('-')) for range in filecontent.split(',')]

def duplicatevalidator(n):
    strn = str(n)
    length = len(strn)

    if (length % 2 == 1):
        return True
    else:
        halflen = length // 2
        for ci in range(halflen):
            if strn[ci] != strn[halflen + ci]:
                return True
        return False
        
def checkcharpositions(strn, partlen, amount):
    for ci in range(0, partlen):
        for pn in range(1, amount):
            if strn[ci] != strn[pn * partlen + ci]:
                return True
    return False

def multiplevalidator(n):
    strn = str(n)
    length = len(strn)

    for partlen in range(1, length):
        if (length % partlen != 0):
            continue
        
        amount = length // partlen
        valid = checkcharpositions(strn, partlen, amount)
        if not valid:
            return False
            
    return True

def validate(validator):
    total = 0

    for idrange in idranges:
        for n in range(int(idrange[0]), int(idrange[1]) + 1):
            if not validator(n):
                total += n
    return total

print("Part one: " + str(validate(duplicatevalidator)))
print("Part two: " + str(validate(multiplevalidator)))