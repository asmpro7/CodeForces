#####################
### author: asmpy ###
### problem: 263A ###
#####################

one_row = ""
one_col = ""

row1 = input().split()
row2 = input().split()
row3 = input().split()
row4 = input().split()
row5 = input().split()

main_list = [
    row1,
    row2,
    row3,
    row4,
    row5
]

for sub_list in main_list:
    if "1" in sub_list:
        one_row = main_list.index(sub_list) + 1
        one_col = sub_list.index("1") + 1
        break

one_move = abs(3-one_col) + abs(3-one_row)
print(one_move)
