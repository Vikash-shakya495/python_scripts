word = "Python Programming"
n = len(word)
word1 = word.upper()
word2 = word.lower()
convertword = ""
for i in range(n):
    if i % 2==0:
        convertword += word2[i]
    else:
        convertword += word1[i]
print(convertword)
            