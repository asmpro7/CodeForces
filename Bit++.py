num=int(input())
x=0
for i in range(num):
    operator=input()
    if operator=="X++" or operator=="+X+" or operator=="++X":
        x+=1
    elif operator=="--X" or operator=="-X-" or operator=="X--":
        x-=1
    else:
        continue
print(x)