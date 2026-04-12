# file = open('q1_input.txt')

# def sieve_of_eratosthenes(limit):
#     is_prime = [True] * (limit + 1)
#     is_prime[0] = is_prime[1] = False
    
#     for i in range(2, int(limit**0.5) + 1):
#         if is_prime[i]:
#             for j in range(i * i, limit + 1, i):
#                 is_prime[j] = False
                
#     return [i for i in range(2, limit + 1) if is_prime[i]]

# def n_subtractorizations(N):
#     primes = sieve_of_eratosthenes(N)
#     subtractorizations = set()
    
    
#     for p1 in primes:
#         for p2 in primes:
#             if p1 != p2:
#                 diff = abs(p1 - p2)
#                 if diff > 0 and diff in primes:
#                     subtractorizations.add(diff)
                    
#     return len(subtractorizations)

# def solve():
#     # Read input value for N
#     N = int(file.readline().strip())
#     return n_subtractorizations(N)

# noOfTestCases = int(file.readline().strip())


# with open('output.txt', 'w') as file2:
#     for i in range(1, noOfTestCases + 1):
#         result = solve()
#         print(result)
#         file2.write(f"Case #{i}: {result}\n")
#         file2.flush()  

# file.close()
file = open('q1_input.txt')

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
                
    return [i for i in range(2, limit + 1) if is_prime[i]], set(range(2, limit + 1)) - set(i for i in range(2, limit + 1) if not is_prime[i])

def n_subtractorizations(N):
    primes, prime_set = sieve_of_eratosthenes(N)
    subtractorizations = set()
    
    # Iterate over each unique pair of primes
    for i in range(len(primes)):
        for j in range(len(primes)):
            if i != j:  # Ensure we are not subtracting the same prime
                diff = abs(primes[i] - primes[j])
                if diff > 0 and diff <= N and diff in prime_set:  # Ensure diff is in bounds and is prime
                    subtractorizations.add(diff)
                    
    return len(subtractorizations)

def solve():
    # Read input value for N
    N = int(file.readline().strip())
    return n_subtractorizations(N)

noOfTestCases = int(file.readline().strip())

with open('output.txt', 'w') as file2:
    for i in range(1, noOfTestCases + 1):
        result = solve()
        print(f"Case #{i}: {result}")  # Debugging output; can be removed if not needed
        file2.write(f"Case #{i}: {result}\n")
        file2.flush()

file.close()

