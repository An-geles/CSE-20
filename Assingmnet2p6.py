change = int(input())

if change <= 0:
    print("No Change")

if change > 0:
    print(change//25, "Quarters")
    change = change%25
    print(change//10, "dimes")
    change = change%10
    print(change//5, "nickles")
    change = change%5
    print(change//1, "pennies")


