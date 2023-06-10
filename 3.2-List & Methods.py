# ----------------------------
#       Assignment 1
# ----------------------------

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0])
print(friends[-5])
print(friends[-1])
print(friends[4])

# ----------------------------
#       Assignment 2
print("="*90)
# ----------------------------

print(friends[::2])
print(friends[1::2])

# ----------------------------
#       Assignment 3
print("="*90)
# ----------------------------

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[1:4])
print(friends[-2:])

# ----------------------------
#       Assignment 4
print("="*90)
# ----------------------------

friends[-1] = "Elzero"
friends[-2] = "Elzero"
print(friends)

# ----------------------------
#       Assignment 5
print("="*90)
# ----------------------------

friends = ["Osama", "Ahmed", "Sayed"]

friends.insert(0, "Nasser")
print(friends)
friends.insert(4, "Salem")
print(friends)

# ----------------------------
#       Assignment 6
print("="*90)
# ----------------------------

friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends[0:2] = []
print(friends)
friends[-1:] = []
print(friends)

# ----------------------------
#       Assignment 7
print("="*90)
# ----------------------------

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends.extend(employees+school)
print(friends)

# ----------------------------
#       Assignment 8
print("="*90)
# ----------------------------

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)

# ----------------------------
#       Assignment 9
print("="*90)
# ----------------------------

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

print(len(friends))

# ----------------------------
#       Assignment 10
print("="*90)
# ----------------------------

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[-1][0])
print(technologies[-1][-1])
