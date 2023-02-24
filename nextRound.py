participants=input().split()
scores=input().split()
winers=0

for i in scores[:int(participants[0])]:
   if int(i) > 0:
        if int(i) >= int(scores[int(participants[1])-1]):
            winers += 1
        else:
            continue
   else:
       continue
print(winers)