#Write a program to sort ArrayList in descending order

l = [3, 7, 95, 16, 52, 44, 1, 100]


# #---Method1----
# print(sorted(l, reverse=True))

# ---Method1----

def swapVal(index):
    tmp = l[index]
    l[index] = l[index+1]
    l[index+1] = tmp


for j in range(len(l)):
    for i in range(len(l)):
        if i < (len(l) - 1) and l[i] < l[i + 1]:
            swapVal(i)

print(l)
