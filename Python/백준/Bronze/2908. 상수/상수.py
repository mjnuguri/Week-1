A, B = input().split()

A_rev = int(A[::-1])
B_rev = int(B[::-1])

print(max(A_rev, B_rev))