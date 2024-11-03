# LISTS
l = ["nucamp", 0, 122.5, 'tad']
print(l)

my_list = ["Alpha", "Bravo", "Charlie", "Delta"]

print(my_list)

print(len(my_list))         # 4

x = my_list.append("Echo")
print(x)                    # None
print(my_list)              # ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo']

y = my_list.pop()           # Echo
print(y)                    # ['Alpha', 'Bravo', 'Charlie', 'Delta']
print(my_list)

z = my_list.pop(2)
print(z)                    # Charlie
print(my_list)              # ['Alpha', 'Bravo', 'Delta']

for word in my_list:
    print(word)
# ↕ same, same ↕
for idx in range(0, len(my_list), 1):
    print(idx)
