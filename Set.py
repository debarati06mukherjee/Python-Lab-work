# Set of 10 fruits
fruits = {
    "apple", "banana", "orange", "mango", "pineapple",
    "grapes", "watermelon", "guava", "papaya", "strawberry"
}

# Summer fruits
summer_fruits = {
    "mango", "watermelon", "pineapple", "grapes", "papaya"
}

# Winter fruits
winter_fruits = {
    "apple", "orange", "guava", "strawberry", "banana"
}

# 1. All fruits in 3 sets
print("All fruits:", fruits | summer_fruits | winter_fruits)

# 2. Fruits present in both fruits and winter fruits
print("Common fruits:", fruits & winter_fruits)

# 3. Fruits only in summer fruits, not in fruits
print("Only summer fruits:", summer_fruits - fruits)

# 4. Fruits in summer and winter but not in fruits
print("Summer and winter but not fruits:",
      (summer_fruits & winter_fruits) - fruits)

# 5. Check whether orange is present in fruits
if "orange" in fruits:
    print("Orange is present")
else:
    print("Orange is not present")

# 6. Find which set contains pineapple
if "pineapple" in fruits:
    print("Pineapple is in fruits")
elif "pineapple" in summer_fruits:
    print("Pineapple is in summer fruits")
elif "pineapple" in winter_fruits:
    print("Pineapple is in winter fruits")