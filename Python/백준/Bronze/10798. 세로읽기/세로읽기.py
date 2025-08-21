words = [input() for _ in range(5)]

max_len = max(len(word) for word in words)

result = ''
for i in range(max_len):  
    for word in words:    
        if i < len(word): 
            result += word[i] 

print(result)