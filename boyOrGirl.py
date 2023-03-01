
#####################
### author: asmpy ###
### problem: 236A ###
#####################

username = input()
user = ""
for char in username:
    if char not in user:
        user += char
    else:
        continue
if len(user) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
