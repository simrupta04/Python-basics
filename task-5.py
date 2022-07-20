#5.Swap Case
str=input("Enter the string::")
n_str=""
for i in range(0,len(str)):
        if str[i].isalpha():
            if str[i].isupper():
                n_str=n_str+str[i].lower()
            else:
                n_str=n_str+str[i].upper()
        else:
            n_str=n_str+str[i]
print("The Swap Case::",n_str)