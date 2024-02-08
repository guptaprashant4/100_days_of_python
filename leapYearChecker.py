year = int(input())

is_leap = True
if year % 4 == 0:
  is_leap = True
  if year % 100 == 0:
    is_leap = False
    if year % 400 == 0:
      is_leap == True
else:
  is_leap = False
  
if is_leap:
  print("Leap year")
else:
  print("Not leap year")