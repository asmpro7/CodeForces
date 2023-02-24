numPro= int(input())
numSol=0
for i in range(numPro):
    numSug=input()
    if int(numSug[0]) + int(numSug[2])==2 or int(numSug[0]) + int(numSug[-1])==2 or int(numSug[-1]) + int(numSug[2])==2 :
        numSol = numSol + 1
    else:
        continue
        
print(numSol)
