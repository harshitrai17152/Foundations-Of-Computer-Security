
def cipher(m,n):
    ciph=""

    l=len(m)
    for i in range(l):
        letter=m[i]

        # if letter is a whitespace
        if(letter==' '):
            ciph+=letter
            
        # if letter is lowercase
        elif(letter.islower()):
            ciph+=chr( ((ord(letter)-97+n)%26) + 97 )
            
        # if letter is uppercase
        else:
            ciph+=chr( ((ord(letter)-65+n)%26) + 65 ) 

    return(ciph)


m=input() # text message
n=int(input()) # key

c=cipher(m,n) # ciphered message
print(c)
