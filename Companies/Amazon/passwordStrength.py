def passwordStrength(password):
    last = {chr(97 + i): -1 for i in range(26)}
    # print(last)
    ret = 0
    for i,ch in enumerate(password):
        print(i, ch)
        left = i - last[ch]
        right = len(password) - i
        ret += left * right
        last[ch] = i
    print(last)
    print(ret)
    return ret


# passwordStrength("good")
last = {}
for i in range(26):
  last[chr(97 + i)] = -1


print(last)

