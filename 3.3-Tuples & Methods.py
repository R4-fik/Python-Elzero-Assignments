# ----------------------------
#       Assignment 1
# ----------------------------

name = "Madara",
print(name)
print(type(name))
# ----------------------------
#       Assignment 2
print("="*90)
# ----------------------------

friends = ("Osama", "Ahmed", "Sayed")

new_friend = friends[1:]
print(new_friend)
friends = ("Elzero",) + new_friend
print(friends)
print(type(friends))
print(str(len(friends)) + " Elements")

# ----------------------------
#       Assignment 3
print("="*90)
# ----------------------------

nums = (1, 2, 3)
letters = ("A", "B", "C")

nums_and_letters_one = nums + letters
print(nums_and_letters_one)
print(str(len(nums_and_letters_one)) + " Elements")

# ----------------------------
#       Assignment 4
print("="*90)
# ----------------------------

my_tuple = (1, 2, 3, 4)
a, b, _, c = my_tuple

print(a)
print(b)
print(c)
