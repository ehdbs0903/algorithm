import sys
from collections import deque
from collections import defaultdict

inputs = sys.stdin.readline

graph = dict()
inDegree = defaultdict(int)
time = dict()

try:
    while True:
        temp = list(input().rstrip().split())
        time[temp[0]] = int(temp[1])
        graph[temp[0]] = ""

        if len(temp) == 3:
            graph[temp[0]] = temp[2]
            for c in temp[2]:
                inDegree[c] += 1

except:
    n = len(time)

    q = deque()
    for c in time:
        if not inDegree[c]:
            q.append(c)

    ans = defaultdict(int)
    while q:
        v = q.popleft()
        ans[v] += time[v]

        for g in graph[v]:
            inDegree[g] -= 1
            ans[g] = max(ans[g], ans[v])

            if not inDegree[g]:
                q.append(g)

    max_ans = 0
    for c in time:
        max_ans = max(max_ans, ans[c])

    print(max_ans)

