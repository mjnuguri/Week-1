n = int(input()) 
count = {}        

for _ in range(n):
    name = input()
    first_char = name[0]
    if first_char in count:
        count[first_char] += 1
    else:
        count[first_char] = 1

result = []
for char, cnt in count.items():
    if cnt >= 5:
        result.append(char)

if result:
    print(''.join(sorted(result))) 
else:
    print("PREDAJA")
