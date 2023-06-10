# ----------------------------
#       Assignment 1
# ----------------------------

name = "Madara"
Age = "120"
Country = "Konoha"

print(' "Hello" ' + "'" + name + "', How You Doing \ " '"""  ' '"' +
      Age + '"" + And Your Country Is: ' + Country)

# ----------------------------
#       Assignment 2
print("="*90)
# ----------------------------

print(' "Hello ' + "'" + name + "', How You Doing \ " + "\n"
      ' """ Your Age Is "' + Age + '"" +' + "\n"
      " And Your Country Is: " + Country)

# ----------------------------
#       Assignment 3
print("="*90)
# ----------------------------

name = "Elzero"
print("Second Letter Is " + '"' + name[1] + '"')
print("Third Letter Is " + '"' + name[2] + '"')
print("Last Letter Is " + '"' + name[-1] + '"')

# ----------------------------
#       Assignment 4
print("="*90)
# ----------------------------

print('"' + name[1:4] + '"')
print('"' + name[0::2] + '"')
print('"' + name[-2::-2] + '"')

# ----------------------------
#       Assignment 5
print("="*90)
# ----------------------------

name = "#@#@Elzero#@#@"

print(name.strip("#@"))

# ----------------------------
#       Assignment 6
print("="*90)
# ----------------------------

num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))

# ----------------------------
#       Assignment 7
print("="*90)
# ----------------------------

name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))

# ----------------------------
#       Assignment 8
print("="*90)
# ----------------------------

name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase())

# ----------------------------
#       Assignment 9
print("="*90)
# ----------------------------

msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))

# ----------------------------
#       Assignment 10
print("="*90)
# ----------------------------

name = "Elzero"
print(name.find("z"))

# ----------------------------
#       Assignment 11
print("="*90)
# ----------------------------

msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love", 1))

# ----------------------------
#       Assignment 12
print("="*90)
# ----------------------------

msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love"))

# ----------------------------
#       Assignment 13
print("="*90)
# ----------------------------

name = "Madara"
age = 120
country = "Konoha"

print(f"My Name Is {name}, And My Age Is {Age}, And My Country Is {Country}")