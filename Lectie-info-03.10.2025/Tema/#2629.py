n = int(input())
A = []
for i in range(n):
    A.append(int(input()))

# Sliding window
st = 0
max_len = 0
seen = set()

for dr in range(n):
    while A[dr] in seen:
        seen.remove(A[st])
        st += 1
    seen.add(A[dr])
    max_len = max(max_len, dr - st + 1)

print(max_len)
