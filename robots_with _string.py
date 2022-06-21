def move1(ray,ben):
    ben=    ben+ray[0]
    ray = ray[1:]
    return(ray,ben)
def move2(ben, kevin):
    kevin = kevin+ben[-1]
    ben = ben[:-1]
    return(ben,kevin)

ray = input()
ben = ""
kevin =""

# find smallest letter in a string
def smallest(string):
    smallest = string[0]
    for letter in string:
        if letter < smallest:
            smallest = letter
    return smallest

ray,ben= move1(ray,ben)
while(ray or ben):
    if(ray and ben):
        if(smallest(ray) < smallest(ben)):
            ray,ben = move1(ray,ben)
        else:
            ben,kevin = move2(ben,kevin)
    elif(ray):
        ray,ben = move1(ray,ben)
    else:
        ben,kevin = move2(ben,kevin)

print( kevin)