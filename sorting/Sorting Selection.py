#Selection Sort 

ele=int(input("Enter no of elem:"))
ls=[0]*ele
for c in range(ele):
    ls[c]=int(input("Number:"))
    #function for giving out list     

print (ls)


def ss(ls):                              #ls is here a list to be passed to be sorted
    ln=len(ls)                           #ln is to us the length of list for loop
    for p in range(0,ln):
        s=ls[p]
        i=p
        for c in range(p+1,ln):              #Compares value and ointerchanges with the samller one present 
            if ls[c]<s:
                s=ls[c]
                i=c
        ls[i],ls[p]=ls[p],ls[i]
    return ls    


print (ss(ls))



"""


Output and Test Case

Enter no of elem:5
Number:454
Number:4545
Number:54
Number:1
Number:161664
[454, 4545, 54, 1, 161664]
[1, 54, 454, 4545, 161664]



"""
