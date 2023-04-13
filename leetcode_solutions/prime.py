def gen_primes(N):
    """Generate primes up to N"""
    primes = set()
    for n in range(2, N):
        print(primes)
        if all(n % p > 0 for p in primes):
            primes.add(n)
            yield n

print(*gen_primes(50))