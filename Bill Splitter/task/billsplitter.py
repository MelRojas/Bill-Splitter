from random import choice

print("Enter the number of friends joining (including you):")
count = int(input())

if count < 1:
    print("No one is joining for the party")
    exit(1)

print("Enter the name of every friend (including you), each on a new line:")
dictionary = dict()
for i in range(count):
    name = input()
    dictionary[name] = 0

print("Enter the total bill value:")
billAmount = float(input())


print("Do you want to use the \"Who is lucky?\" feature? Write Yes/no")
useWhoIsLucky = input().strip().lower() or "yes"
luckyOne = ""

if useWhoIsLucky == "yes":
    luckyOne = choice(list(dictionary.keys()))
    print(f"{luckyOne} is the lucky one!")
    count -= 1
else:
    print("No one is going to be lucky")


splitValue = round(billAmount / count, 2)

for key in dictionary:
    if key == luckyOne:
        dictionary[key] = 0
        continue
    dictionary[key] = splitValue

print(dictionary)

