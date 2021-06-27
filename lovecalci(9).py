#This is a love calculator about which we all have heard about. But for some reason if you don't know how we arrived at this stage, please check out article on it by Buzzfeed. 

name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
a = name1.lower()
b = name2.lower()
combination1 = a.count("t") + a.count("r") + a.count("u") + a.count("e") + b.count("t") + b.count("r") + b.count("u") + b.count("e")
combination2 = a.count("l") + a.count("o") + a.count("v") + a.count("e") + b.count("l") + b.count("o") + b.count("v") + b.count("e")
lovescore = int(str(combination1) + str(combination2))
if lovescore < 10 or lovescore >90:
    print(f"Your score is {lovescore}, you get together like coke and mentos.")
elif lovescore in range(40,51):
    print(f"your score is {lovescore}, you are alright together")
else:
    print(f"Your score is {lovescore}")   
print(lovescore)         