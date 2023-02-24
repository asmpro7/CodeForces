#####################
### author: asmpy ###
### problem: 71A  ###
#####################

numTry=int(input())
for i in range(numTry):
    word = input()
 
    if len(word) > 10:
        print(f"{word[0]}{str(len(word)-     2)}{word[-1]}")
    else:
        print(word) 
    
