ages = [5, 12, 17, 18, 24, 32]

def adulting(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(adulting, ages)

for x in adults:
  print(x)


def years_to_months(x):
  return x*12

age_months = map(years_to_months, ages)

for x in age_months:
  print(x)