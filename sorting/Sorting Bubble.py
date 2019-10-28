ele=int(input("Enter no of elem:"))
ls=[0]*ele
for c in range(ele):
    ls[c]=int(input("Number:"))
    #function for giving out list     

print (ls)


    
    
#Defining a function here 

def Bubble(ls):                                      #ls is here a list to be passed to be sorted
 
    ln=len(ls)                                       #ln is to us the length of list for loop
    for p in range(0,ln-1):
        for c in range(0,ln-p-1):                    #Two loops parent for one complete cycle and nested for comparing elements  
            if ls[c]>ls[c+1]:                         
                ls[c],ls[c+1]=ls[c+1],ls[c]          #Comparing and assigning the values here or swapping the values if satisfyes    
                
    return ls


print (Bubble(ls))        

"""
Output and Test Case

Enter no of elem:5
Number:123
Number:145
Number:5
Number:41
Number:15
[123, 145, 5, 41, 15]
[5, 15, 41, 123, 145]
>>> 
"""
    
    
