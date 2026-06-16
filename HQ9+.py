x=input()
count=0
for i in x:
    if i=="H" or i=="Q" or i=="9":
        print("YES")
        break
    else:
        count+=1
if count==len(x):
    print("NO")

    
     
