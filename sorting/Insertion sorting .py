
ele=int(input("Enter no of elem:"))
ls=[0]*ele
for c in range(ele):
    ls[c]=int(input("Number:"))
    #function for giving out list     

print (ls)




#Insertion Sorting
def Is(ls):                                            #ls is here a list to be passed to be sorted                                  
    for p in range(1,len(ls)):                         #ln is to us the length of list for loop
        c=p-1
        T=ls[p]
        while T<ls[c] and c>=0:                         #Here sorts the element and the elements before the current one 
            ls[c+1]=ls[c]
            c=c-1
        ls[c+1]=T
    return ls

print (Is(ls))


"""

Out put and Test run

Enter no of elem:5
Number:11
Number:5
Number:45
Number:94
Number:412
[11, 5, 45, 94, 412]
[5, 11, 45, 94, 412]

"""
