T = int(input())  # 테스트 케이스 수

for _ in range(T):
    k = int(input())  # 층 수 입력 (0층부터 시작)
    n = int(input())  # 호 수 입력 (1호부터 시작)

    # 0층 사람 수: 1호에는 1명, 2호에는 2명, ..., n호에는 n명
    people = [i for i in range(1, n + 1)]

    # 1층부터 k층까지 위 규칙에 따라 사람 수 계산
    for _ in range(k):
        for i in range(1, n):
            people[i] += people[i - 1]  # 바로 아래층 1호부터 현재 호까지 합

    # k층 n호에 사는 사람 수 출력
    print(people[n - 1])
