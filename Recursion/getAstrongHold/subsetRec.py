def subset(i, s, sub):
    if i == len(s):
        print(sub)
        return

    subset(i + 1, s, sub + s[i])
    
    subset(i + 1, s, sub)

s = input()
generate(0, s, '')
