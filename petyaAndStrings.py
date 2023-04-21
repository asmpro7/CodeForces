#####################
### author: asmpy ###
### problem: 112A ###
#####################

str1 = input()
str2 = input()

str1Lower = str1.lower()
str2Lower = str2.lower()

list1 = list(str1Lower)
list2 = list(str2Lower)

stringSum1 = 0
stringSum2 = 0

for char1 in list1:
    charOrder1 = int(ord(char1))
    stringSum1 += charOrder1

for char2 in list2:
    charOrder2 = int(ord(char2))
    stringSum2 += charOrder2

if stringSum1 == stringSum2:
    print(0)
elif stringSum1 > stringSum2:
    print(1)
elif stringSum1 < stringSum2:
    print(-1)
