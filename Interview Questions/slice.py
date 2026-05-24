s = input("Enter a sentence: ")

l = s.split()

l = l[::-1]#reverse the list 

l = ' '.join(l)
print(l)

str1 = "/*apples are and foubd% only @red & green"
s = ''
for i in str1:
    if((i>='A' and i<='Z')| (i>='a' and i<='z') | (i==' ')):
        s = s+i
print(s)