# ----------------------------
#       Assignment 1
# ----------------------------

my_list = [1, 2, 3, 3, 4, 5, 1]

my_list = set(my_list)
unique_list = list(my_list)
print(unique_list)
print(type(unique_list))
print(unique_list[:len(unique_list) - 1])

# ----------------------------
#       Assignment 2
print("="*90)
# ----------------------------

nums = {1, 2, 3}
letters = {"A", "B", "C"}

f1 = nums | letters
f2 = nums.union(letters)
nums.update(letters)
print(f1)
print(f2)
print(nums)

# ----------------------------
#       Assignment 3
print("="*90)
# ----------------------------

my_set = {1, 2, 3}
letters = {"A", "B", "C"}

print(my_set)
my_set.clear()
print(my_set)
my_set.update(letters)
my_set.discard("C")
print(my_set)

# ----------------------------
#       Assignment 4
print("="*90)
# ----------------------------

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))

# ----------------------------
#       Assignment 5
print("="*90)
# ----------------------------

Programming = {
    "HTML": "90%",
    "CSS": "80%",
    "Python": "30%"
}
print("HTML Progress Is " + Programming["HTML"])
print("CSS Progress Is " + Programming["CSS"])
print("Python Progress Is " + Programming["Python"])
Programming.update({"AI": "20%"})
print("AI Progress Is " + Programming["AI"])