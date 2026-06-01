s = "hello world"
s1 = " " + s + " "
s2=""
for i in range(0,len(s1)):
    if s1[i] == " ":
        s2 += s1[i+1].upper()
    else:
        s2+=s1




