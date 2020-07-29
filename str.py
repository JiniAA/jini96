"""
2. Accept a String input
    - Print the count of words in the String. Space is assumed to be the separator between words
    - Print all numbers that are present in the String and also if they are odd or even. Numbers which are together should be counted as one number.
"""
    
     
    import re
     
    even=list()
    odd=list()
    z=input("Enter a String : ")
    wordcount=len(z.split())
    print("Total Words - ",wordcount)
    num=re.findall("[0-9]+",z)
    num=[int(i) for i in num]
    for i in num:
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)
    even=set(even)
    odd=set(odd)
    print("Even numbers -",end=" ")
    print(*even,sep=',')
    print("Odd numbers -",end=" ")
    print(*odd,sep=',')
