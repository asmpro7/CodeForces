#####################
### author: asmpy ###
### problem: 791A ###
#####################

weights = input().split()
bear = int(weights[0])
pop = int(weights[1])
years = 0
while True:
    years += 1
    bear = bear * 3
    pop = pop * 2
    if bear > pop:
        break
    else:
        continue
print(years)
