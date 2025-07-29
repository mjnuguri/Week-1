month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

week_days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())
12
total_days = sum(month_days[:x-1]) + y

print(week_days[total_days % 7])