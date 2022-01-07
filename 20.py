# determines prime numbers based on the Sieve of Eratosthenes algorithm
def isPrime(n: int) -> bool:
    # declare a truth table and default every number to True
    prime = [True for i in range(n + 1)]

    p = 2

    while (p * p <= n):
        if(prime[p]):  # if the value of prime[p] is unchanged, prime[p] is a prime number
            for i in range(p * p, (n + 1), p):
                prime[i] = False  # all the multiples of p are not prime numbers

        p += 1

    # 0 and 1 are not prime numbers, manually set it to False
    prime[0] = False
    prime[1] = False

    num = [n if prime[n] else 0 for n, _ in enumerate(prime)]
    print(sum(num))

    return prime[n]


if __name__ == "__main__":
    n = int(input())
    isPrime(n)
