s = input("enter string")
#first 5
print(s[:5:])
#ninth char 
print("Ninth character of string is ", s[8])
#reversed
print(s[::-1])
#alt reversed
for i in range(len(s)-1,-1,-1):
    print(s[i])
