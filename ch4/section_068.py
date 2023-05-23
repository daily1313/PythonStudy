# section_068.py

def turnNone(value):
    x = value

def turnValue(value):
    return value * 10

def turnSet(value):
    return {value, value+1, value+2}

def turnTuple(value):
    return value, value-1, value-2

print(turnNone(10))
print(turnValue(10))
print(turnSet(10))
print(turnTuple(10))