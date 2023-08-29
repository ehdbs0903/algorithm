def star(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]

    ret = star(n // 2)
    for i in range(len(ret)):
        ret.append(ret[i] + ' ' + ret[i])
        ret[i] = ' ' * (n // 2) + ret[i] + ' ' * (n // 2)

    return ret


n = int(input())
print('\n'.join(star(n)))
