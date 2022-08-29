"""Write a program for reverse middle text of a sentence? Output should be same as mentioned below.
Input: I am the strongest man.
Output: I am the tsegnorts man.
"""

str1 = 'I am the strongest man.'

def reverseMe(word):
    reverseWord = ''
    i = len(word) - 1
    while i >= 0:
        reverseWord = reverseWord + word[i]
        i = i - 1
    return reverseWord

middle = len(str1)/2
middleWord = str1[int(middle):].split()[0]
for i in str1.split():
    if middleWord in i:
        middleWord = i
        print(middleWord)

print(str1.replace(middleWord,reverseMe(middleWord)))


