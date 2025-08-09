n = int(input())  # 몇 번 검사할지 입력 받기

for _ in range(n):
    a, b = input().split()  # 두 문자열 입력 받기
    if sorted(a) == sorted(b):  # 두 문자열을 알파벳 순서대로 정렬해서 비교
        print("Possible")  # 같으면 재배열 가능
    else:
        print("Impossible")  # 다르면 불가능
