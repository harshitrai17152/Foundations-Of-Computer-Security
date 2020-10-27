import gmpy2

c1=gmpy2.mpz(input())
c2=gmpy2.mpz(input())
e=gmpy2.mpz(input())
d=gmpy2.mpz(input())
n=gmpy2.mpz(input())
#c1=gmpy2.mpz(181348525620577621096567818397949628270)
#c2=gmpy2.mpz(6992129207362869598663367037937112257496250848048250963600)
#e=gmpy2.mpz(18446743798831775761)
#d=gmpy2.mpz(230835991054122861082648710476609886249)
#n=gmpy2.mpz(252885621875195130661895700184100847631)

k=gmpy2.powmod(c1,d,n)-1 # k = [(C1^d) mod(n)] - 1
m=gmpy2.powmod(gmpy2.powmod(c2,1,n)*gmpy2.powmod(k,-e,n),1,n) # m = C2 / [(k^e) mod(n)]

print("m:",end=" ")
print(m)
print("k:",end=" ")
print(k)
