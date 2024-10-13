"""
Given a list of names, prompt the user to remove the names until they enter an empty string.
Ensure the program does not crash when the name is not in the list.
Then get them to input the name again.
"""
# names = ["Ada", "Bob", "Cathy", "Don"]
#
# print(",".join(names))
#
# name_to_remove = input("Name to remove: ")
#
# while name_to_remove != "":
#     try:
#         names.remove(name_to_remove) # Removes the name entered
#     except ValueError:
#         print("Invalid name.")
#     print(names)
#     name_to_remove = input("Name to remove: ")

"""
things = [True, 1.2, "Good", [1, 10]]
print(things [-2]) # Good
print("%".join([things[2][1:-1]])) # oo
print([str(t)[0] for t in things]) # T, 1, G, [
print([len(str(t)) for t in things]) # 4, 3, 4, 7
print([t for t in things if type(t) in (float, int)]) # 1.2
print([t for t in things if isinstance(t, int)]) # True
"""

"""
values = [[3, 4, 5, 1], [33, 6, 1, 2]]

v = values[0][0] # 3
for row in range(0, len(values)): # range(0, 2)
    for column in range(0, len(values[row])): # range(0, 4)
        if v < values[row][column]:
            v = values[row][column]
                
print(v) # 33
"""

"""

"""

data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]

for i in range(len(data)):
    print(f"{data[i][0]} = {data[i][1]}")