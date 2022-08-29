#Write a program to reverse ArrayList

l = [3, 7, 95, 16, 52, 44, 1, 100]

# ----Method 1-----
# # using python Slicing
# print(l[::-1])


# ----Method 2-----
i = len(l) - 1
# new array list
newList = []
while i >= 0:
    newList.append(l[i])
    i = i - 1

print(newList)
