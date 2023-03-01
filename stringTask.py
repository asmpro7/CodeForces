#####################
### author: asmpy ###
### problem: 118A ###
#####################

string = list(input().lower())
string[:] = [char for char in string if char != "a" and char !=
             "y" and char != "o" and char != "u" and char != "i" and char != "e"]
print("."+".".join(string))
