def nearest_multiple(n, k):
    low = (n // k) * k
    high = low + k
    if high - n <= n - low:
        return high 
    return low

n = int(input())
k = int(input())
print(nearest_multiple(n, k))