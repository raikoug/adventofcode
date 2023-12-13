

input_list = open("../input", "r").read().split("\n")

def is_int(ch):
    try:
        int(ch)
        return True
    except:
        return False

res = 0
for row in input_list:
    n = ""
    for ch in row:
        if is_int(ch):
            n += ch
    if len(n) == 1:
        value = int(n+n)
    else:
        value = int(n[0]+n[-1])

    res += value

print(res)
