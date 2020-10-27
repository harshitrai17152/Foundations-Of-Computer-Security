import gmpy2

c=gmpy2.mpz(input())
d=gmpy2.mpz(input())
n=gmpy2.mpz(input())
#c=gmpy2.mpz(133172557019266705097691345749894112534)
#d=gmpy2.mpz(230835991054122861082648710476609886249)
#n=gmpy2.mpz(252885621875195130661895700184100847631)

m=gmpy2.powmod(c,d,n) # m=(c^d) mod(n)

print("m:",end=" ")
print(m)
