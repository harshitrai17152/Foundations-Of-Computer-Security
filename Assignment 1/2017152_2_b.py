#  Encoding Scheme
# ------------------
# A - @
# a - @
# o - 0
# O - 0
# s - 5
# S - 5
# i - !
# I - !

# The case of the character is toggled only if it is 
# at the even index(from-0) in the original password
# ------------------
# ------------------

def change(c):
    if( c=='a' or c=='A' ):
        c='@'
    elif( c=='o' or c=='O' ):
        c='0'
    elif( c=='s' or c=='S' ):
        c='5'
    elif( c=='i' or c=='I' ):
        c='!'
        
    return(c)

def toggle(c):
    if(c.isupper()):
        c=c.lower()
    else:
        c=c.upper()
        
    return(c)

def hash(s):

    n=len(s)
    ans=""
    i=0
    
    while(i<n):
        count=1
        new_c=change(s[i])    
        for j in range(i+1,n):
            if(s[j]==s[i]):
                count+=1
            else:
                break
        
        if(i%2==0):
            new_c=toggle(new_c)
        ans+=new_c
    
        if(count!=1):
            ans+=str(count)
        i+=count
        
    return(ans)
nu=0
n=int(input())
d=open("english.txt","r")
password=open(r"password.txt","w")

f1=d.readlines()
for i in f1:
    nu+=1
    word=i.strip("\n")
    if(len(word)==n):
        password.writelines(hash(word)) 
        password.write("\n")
        
password.close()
