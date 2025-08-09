n = int(input()) 
original = n      
count = 0         

while True:
    a = n // 10           # 앞자리 숫자
    b = n % 10            # 뒷자리 숫자
    new_num = (b * 10) + ((a + b) % 10) 
    count += 1          
    n = new_num          
    if n == original:    
        break

print(count) 
