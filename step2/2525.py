a, b = input().split()
c = int(input())
minute = int(b) + c

if minute > 59:
  hour = int(a) + (minute//60)
  minute = minute%60
  if hour > 23:
    hour = hour-24
  print(hour, minute)
else:
  print(a, minute)