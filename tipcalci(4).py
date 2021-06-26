print("Welcome to the tip calculator\n")
a = float(input("What was the total Bill\n"))
b = int(input("What percentage tip would you like to give? 10, 12, or 15\n"))
c = int(input("How many people to split the bill?\n"))
d = round(((a+(a*(b/100)))/c),2)
print(f"Each person should pay {d}")

