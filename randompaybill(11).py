import random
asknames_string = input("Enter the names of all the people, separated by a comma\n")
asknames = asknames_string.split(",")
#lennames = len(asknames)
random_choice = random.randint(0, len(asknames) -1)
billpayer = (asknames[random_choice])
print(f"Person who will be paying the bill is {billpayer}")
