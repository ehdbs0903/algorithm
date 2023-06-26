s1 = input()
s2 = input()

len_s1 = len(s1)
len_s2 = len(s2)

prev = [0] * (len_s2 + 1)
max_value = 0

for i in range(len_s1):
    temp = [0] * (len_s2 + 1)

    for j in range(len_s2):
        if s1[i] == s2[j]:
            temp[j+1] = prev[j] + 1

    max_value = max(max_value, max(temp))
    prev = temp[:]

print(max_value)
