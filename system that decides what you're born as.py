import time
import random
print("destiny is deciding your fate...")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
race = random.randint(1, 4)

if race == 1:
    print("You're a Human")
elif race == 2:
    print("You're a Dwarf")
elif race == 3:
    print("You're a Witch")
else:
    print("You're a Vampire")