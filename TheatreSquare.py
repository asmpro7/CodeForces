from math import ceil
lenths=input().split()
print(ceil(int(lenths[0])/int(lenths[-1]))*ceil(int(lenths[1])/int(lenths[-1])))