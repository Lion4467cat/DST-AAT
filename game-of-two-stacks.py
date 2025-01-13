def two_stacks(maxSum, a, b):
    count = 0
    sum = 0
    i = 0
    j = 0
    
    while i < len(a) and sum + a[i] <= maxSum:
        sum += a[i]
        count += 1
        i += 1
        
    max_count = count
    while j < len(b) and i >= 0:
        sum += b[j]
        j += 1
        while sum > maxSum and i > 0:
            i -= 1
            sum -= a[i]
        if sum <= maxSum:
            max_count = max(max_count, i + j)
    
    return max_count

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n, m, maxSum = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        print(twoStacks(maxSum, a, b))
