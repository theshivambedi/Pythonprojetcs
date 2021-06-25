a = int(input("what's your current age?\n"))
days_left = (90*365 - a*365)
weeks_left = 90*52 - a*52
months_left = 90*12 - a*12
years_left = 90 - a
print(f"you have these many {days_left} days, {weeks_left} weeks, {months_left} months and {years_left} years left until you turn 90")