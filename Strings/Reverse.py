#Reverse Words in a String

#bruteforce

s=input()
words = []
word = ""

for ch in s:
    if ch != " ":
        word += ch
    elif word:
        words.append(word)
        word = ""

if word:
    words.append(word)

words.reverse()
return " ".join(words)

#optimal

result = ""
i = len(s) - 1

while i >= 0:
    while i >= 0 and s[i] == " ":
        i -= 1

    if i < 0:
        break

    end = i

    while i >= 0 and s[i] != " ":
        i -= 1

    word = s[i+1:end+1]

    if result != "":
        result += " "

    result += word
