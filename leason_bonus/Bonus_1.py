# Задача 1:
# Є 3 группи людей(sets) australia_blacklist, poker_blacklist, alcohol_blacklist.
# В кожній групі вказані імена. Вивести тих хто виграв джекпот(є одразу в 3х списках)

australia_blacklist = {"Den", "Alex", "Ivan"}
poker_blacklist = {"Alex", "Ivan", "Maria"}
alcohol_blacklist = {"Alex", "Maria", "Viktor"}
print(alcohol_blacklist.intersection(poker_blacklist,australia_blacklist))
