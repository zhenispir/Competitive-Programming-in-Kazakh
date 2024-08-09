MOD = 10**9 + 7

def mod_inverse(a, p):
    # Fermat's little theorem for computing a^(p-2) % p
    return pow(a, p - 2, p)

def precompute_factorials_and_inverses(max_n, mod):
    factorial = [1] * (max_n + 1)
    inv_factorial = [1] * (max_n + 1)
    for i in range(2, max_n + 1):
        factorial[i] = factorial[i - 1] * i % mod
    inv_factorial[max_n] = mod_inverse(factorial[max_n], mod)
    for i in range(max_n - 1, 0, -1):
        inv_factorial[i] = inv_factorial[i + 1] * (i + 1) % mod
    return factorial, inv_factorial

def binomial_coefficient(n, k, factorial, inv_factorial, mod):
    if k > n or k < 0:
        return 0
    return factorial[n] * inv_factorial[k] % mod * inv_factorial[n - k] % mod

def solve(t, cases):
    max_n = max(c[0] for c in cases)
    factorial, inv_factorial = precompute_factorials_and_inverses(max_n, MOD)
    
    results = []
    
    for n, k, array in cases:
        total_sum = 0
        half_k = (k - 1) // 2
        for i in range(n):
            left_count = binomial_coefficient(i, half_k, factorial, inv_factorial, MOD)
            right_count = binomial_coefficient(n - i - 1, half_k, factorial, inv_factorial, MOD)
            total_contributions = left_count * right_count % MOD
            total_sum = (total_sum + array[i] * total_contributions % MOD) % MOD
        
        results.append(total_sum)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
cases = []

for _ in range(t):
    n = int(data[index])
    k = int(data[index + 1])
    array = list(map(int, data[index + 2:index + 2 + n]))
    cases.append((n, k, array))
    index += 2 + n

# Solve the problem
results = solve(t, cases)

# Output the results
for result in results:
    print(result)
