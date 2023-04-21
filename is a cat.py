######################
### author: asmpy  ###
### problem: 1800A ###
######################

numCases = int(input())
typStr = "meow"
outStr = "$"
for i in range(numCases):
    numChar = int(input())
    string = list(input().lower())
    string = string[:numChar]
    for char in string:
        if char == outStr[-1]:
            continue
        else:
            outStr += char
    if outStr[1:] == typStr:
        print("YES")
    else:
        print("NO")
    outStr = "$"
