m = int(input())
is_prime = True
if m <= 1:
    is_prime = False
else:
    for i in range(2, int(m ** 0.5) + 1):
        if m % i == 0:
            is_prime = False
            break
if is_prime:
    print("YES")
else:
    print("NO")
