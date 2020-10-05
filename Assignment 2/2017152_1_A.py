import gmpy2

p=gmpy2.mpz(input())
q=gmpy2.mpz(input())
m=gmpy2.mpz(input())
#p=gmpy2.mpz(13708957235651002373)
#q=gmpy2.mpz(18446743798831775747)
#m=gmpy2.mpz(88262316008826231600)

n=gmpy2.mul(p,q) # p*q
phi_n=gmpy2.mul(gmpy2.sub(p,1),gmpy2.sub(q,1)) # (p-1)*(q-1)

e=gmpy2.next_prime(q) # GCD(e,phi_n)=1
    
d=gmpy2.invert(e,phi_n) # (e*d) mod(phi_n)=1
c=gmpy2.powmod(m,e,n) # c=(m^e) mod(n)

print("c:",end=" ")
print(c)
print("e:",end=" ")
print(e)
print("d:",end=" ")
print(d)
print("n:",end=" ")
print(n)
