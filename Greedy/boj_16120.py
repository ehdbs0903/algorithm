s = input()

p_cnt = 0
a_flag = 0
for i in range(len(s)):
    if s[i] == 'P':
        a_flag = 0
        p_cnt += 1
    else:
        if a_flag:
            break

        a_flag = 1
        p_cnt -= 2

    if p_cnt < 0:
        break

if p_cnt == 1 and a_flag == 0:
    print("PPAP")
else:
    print("NP")
