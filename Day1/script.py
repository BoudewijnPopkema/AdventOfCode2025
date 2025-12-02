file = open("input")
with open("input") as file:
    rotations = [line.rstrip() for line in file]
    
current = 50
passwordone = 0
passwordtwo = 0

for rotation in rotations:
    direction = rotation[0]
    movesize = int(rotation[1:])

    fullrotations = abs(movesize) // 100
    remainder = abs(movesize) % 100
    
    directedremainder = remainder if direction == 'R' else -remainder
    
    past = current
    current += directedremainder
    if (current < 0 or current > 100) and not past == 0:
        passwordtwo += 1
    
    current = current % 100
    
    passwordtwo += fullrotations
    
    if current == 0:
        passwordone += 1
        passwordtwo += 1
    
    print(rotation + " rotated to " + str(current) + " so we went to " + str(passwordone) + " " + str(passwordtwo))

print(passwordone)
print(passwordtwo)