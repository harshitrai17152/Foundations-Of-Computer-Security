import random
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

k=gmpy2.mpz(random.randint(1,p-1)) # GCD(k,n)=1

c1=gmpy2.powmod(k+1,e,n) # C1 = [(k+1)^e] mod(n)
c2=gmpy2.mul(m,gmpy2.powmod(k,e,n)) # C2 = m*[(k^e) mod(n)]

print("C1:",end=" ")
print(c1)
print("C2:",end=" ")
print(c2)
print("k:",end=" ")
print(k)
print("d:",end=" ")
print(d)
print("n:",end=" ")
print(n)
