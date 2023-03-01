#####################
### author: asmpy ###
### problem: 266A ###
#####################

numStr = int(input())
stones = input()
stones = stones[:numStr]
StStones = "A"
numStone = 0
for char in stones:
    if char == StStones[-1]:
        numStone += 1
    else:
        StStones += char
print(numStone)
